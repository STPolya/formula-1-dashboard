import streamlit as st
import pandas as pd
import plotly.express as px

def show_drivers(connection, func_get_queries, func_show_select):
    st.set_page_config(
        page_title='Детализация по пилотам',
        layout='wide',
    )

    data = pd.read_sql_query("""
        SELECT DISTINCT drivers.surname
        FROM drivers
        JOIN driver_standings ON drivers.driverId = driver_standings.driverId
        JOIN races ON driver_standings.raceId = races.raceId
        WHERE races.year = 2021
        ORDER BY drivers.surname
    """, connection)

    selected_driver = func_show_select('Выберите пилота', data['surname'])

    queries = func_get_queries()
    dataframes = {name: pd.read_sql_query(sql, connection, params=(selected_driver, )) for name, sql in
                  queries.items()}

    driver_points_dynamic = px.line(
        dataframes['dynamic_drivers_points'],
        x='date_place',
        y='points',
        color_discrete_sequence=['#CE0303'],
        markers=True,
    )

    driver_points_dynamic.update_layout(
        xaxis_title='Дата и трасса',
        yaxis_title='Очки',
    )

    with st.container(gap=52):
        with st.container(gap=32):
            with st.container(gap=8):
                st.title('Детализация по пилотам')
                st.write('Показатели выбранного пилота и его результаты на каждом этапе сезона')

            card1, card2, card3, card4, card5 = st.columns(5)
            card1.metric(label='Очков в личном зачете', value=dataframes['driver_points_championship'].loc[0, 'points'], border=True)
            card2.metric(label='Место в личном зачете', value=dataframes['driver_points_championship'].loc[0, 'position'], border=True)
            card3.metric(label='Финишей в очках', value=dataframes['percent_points_races'].loc[0, 'points_races_percent'], border=True)
            card4.metric(label='Сходов', value=dataframes['percent_dnf_races'].loc[0, 'dnf_races_percent'], border=True)
            card5.metric(label='Команда пилота', value=dataframes['driver_points_championship'].loc[0, 'team'], border=True)

        with st.container(gap=0):
            st.subheader('Динамика очков')
            st.plotly_chart(driver_points_dynamic)

        with st.container(gap=32):
            st.subheader('Места в квалификациях и гонках')

            card1, card2, card3, card4 = st.columns(4)
            card1.metric(label='Ср позиция в квалификации', value=dataframes['avg_quali_position'].loc[0, 'avg_quali_position'], border=True)
            card2.metric(label='Ср позиция на финише', value=dataframes['avg_race_position'].loc[0, 'avg_race_position'], border=True)
            card3.metric(label='Количество побед', value=dataframes['count_wins'].loc[0, 'count_wins'], border=True)
            card4.metric(label='Количество подиумов', value=dataframes['count_podiums'].loc[0, 'count_podiums'], border=True)

            st.dataframe(dataframes['table_results'], hide_index=True, height=800)