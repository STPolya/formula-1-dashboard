import pandas as pd
import plotly.express as px
import streamlit as st

def show_history(connection, func_get_queries, func_show_slider):
    st.set_page_config(
        page_title='Исторический обзор Формулы 1',
        layout='wide',
    )

    with st.container(gap=32):
        with st.container(gap=28):
            with st.container(gap=8):
                st.title('Исторический обзор Формулы 1')
                st.write('Основные показатели чемпионата и самые титулованные пилоты и команды за выбранный период')

            min_year, max_year = func_show_slider()

        queries = func_get_queries()
        dataframes = {name: pd.read_sql_query(sql, connection, params=(min_year, max_year)) for name, sql in
                      queries.items()}

        graph_drivers_titles = px.bar(
            data_frame=dataframes['drivers_titles'],
            x='titles',
            y='driver_name',
            color='driver_name',
            color_discrete_sequence=['#CE0303'],
            labels={
                'titles': 'Количество титулов',
                'driver_name': 'Пилоты',
            },
        )

        graph_constructors_titles = px.bar(
            data_frame=dataframes['constructors_titles'],
            x='titles',
            y='name',
            color='name',
            color_discrete_map={
                'Ferrari': '#CE0303',
                'McLaren': '#FF8C00',
                'Williams': '#006FFF',
                'Mercedes': '#0BE7D1',
                'Red Bull': '#006FFF',
                'Team Lotus': '#E3C629',
                'Renault': '#E3C629',
                'Cooper-Climax': '#093FB5',
                'Lotus-Climax': '#2AB814',
                'Brabham-Repco': '#2AB814',
            },
            labels={
                'titles': 'Количество титулов',
                'name': 'Команды',
            },
        )

        graph_drivers_titles.update_layout(showlegend=False)
        graph_constructors_titles.update_layout(showlegend=False)

        with st.container(gap=44):
            card1, card2, card3, card4, card5 = st.columns(5)
            card1.metric(label='Гонок', value=dataframes['count_races']['count_races'], border=True)
            card2.metric(label='Сезонов', value=dataframes['count_seasons']['count_seasons'], border=True)
            card3.metric(label='Команд', value=dataframes['count_teams']['count_teams'], border=True)
            card4.metric(label='Пилотов', value=dataframes['count_drivers']['count_drivers'], border=True)
            card5.metric(label='Спринтов', value=dataframes['count_sprints']['count_sprints'], border=True)

            with st.container(gap=0):
                st.subheader('Топ 10 пилотов и команд по количеству титулов')
                left_column, right_column = st.columns(2)
                with left_column:
                    st.plotly_chart(graph_drivers_titles)
                with right_column:
                    st.plotly_chart(graph_constructors_titles)