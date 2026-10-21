import streamlit as st
import pandas as pd
import plotly.express as px

def show_teams(connection, func_get_queries, func_show_select):
    st.set_page_config(
        page_title='Детализация по командам',
        layout='wide',
    )

    data = pd.read_sql_query("""
        SELECT DISTINCT constructors.name
        FROM constructors
        JOIN constructor_standings ON constructors.constructorId = constructor_standings.constructorId
        JOIN races ON constructor_standings.raceId = races.raceId
        WHERE races.year = 2021
        ORDER BY constructors.name
    """, connection)

    selected_team = func_show_select('Выберите команду', data['name'])

    queries = func_get_queries()
    dataframes = {name: pd.read_sql_query(sql, connection, params=(selected_team, )) for name, sql in
                  queries.items()}

    team_points_dynamic = px.line(
        dataframes['dynamic_teams_points'],
        x='date_place',
        y='points',
        color_discrete_sequence=['#CE0303'],
        markers=True,
    )

    team_points_dynamic.update_layout(
        xaxis_title='Дата и трасса',
        yaxis_title='Очки',
    )

    with st.container(gap=52):
        with st.container(gap=32):
            with st.container(gap=8):
                st.title('Статистика команд за 2021')
                st.write('Показатели выбранной команды, вклад её пилотов и динамика результатов за сезон')

            card1, card2, card3, card4, card5 = st.columns(5)
            card1.metric(label='Очков в кубке конструкторов', value=dataframes['team_points_championship'].loc[0, 'points'], border=True)
            card2.metric(label='Место в кубке конструкторов', value=dataframes['team_points_championship'].loc[0, 'position'], border=True)
            card3.metric(label='Финишей в очках', value=dataframes['percent_points_races'].loc[0, 'percent_points_races'], border=True)
            card4.metric(label='Сходов', value=dataframes['percent_dnf_races'].loc[0, 'percent_dnf_races'], border=True)
            card5.metric(label='Количество пилотов', value=dataframes['team_points_championship'].loc[0, 'drivers_count'], border=True)

        with st.container(gap=28):
            st.subheader('Пилоты и места в гонках и квалификациях')
            left_column, right_column = st.columns([7, 3])
            with left_column:
                pir_charts_drivers = px.pie(
                    dataframes['drivers_points'],
                    names="surname",
                    values="points",
                    color_discrete_sequence=['#AC0000', '#840000', '#6D0000']
                )
                pir_charts_drivers.update_traces(
                    textinfo="percent+label",
                    insidetextorientation="radial",
                )
                st.plotly_chart(pir_charts_drivers)

            with right_column:
                st.metric(label='Количество подиумов команды', value=dataframes['count_podiums'].loc[0, 'count_podiums'], border=True)
                st.metric(label='Ср позиция в квалификации', value=dataframes['avg_quali_position'].loc[0, 'avg_quali_position'], border=True)
                st.metric(label='Ср позиция на финише', value=dataframes['avg_race_position'].loc[0, 'avg_race_position'], border=True)

        with st.container(gap=0):
            st.subheader('Динамика очков')
            st.plotly_chart(team_points_dynamic)