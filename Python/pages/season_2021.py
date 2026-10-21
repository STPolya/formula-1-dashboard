import streamlit as st
import pandas as pd
import plotly.express as px

def show_2021(connection, func_get_queries):
    st.set_page_config(
        page_title='Обзор 2021 года',
        layout='wide',
    )

    queries = func_get_queries()
    dataframes = {name: pd.read_sql_query(sql, connection) for name, sql in queries.items()}

    graph_drivers_titles = px.bar(
        data_frame=dataframes['drivers_count_wins'],
        x='podiums',
        y='surname',
        color='surname',
        color_discrete_sequence=['#CE0303'],
        labels={
            'podiums': 'Количество подиумов',
            'surname': 'Пилоты',
        },
    )

    graph_teams_titles = px.bar(
        data_frame=dataframes['teams_count_wins'],
        x='podiums',
        y='name',
        color='name',
        color_discrete_map={
            'Ferrari': '#CE0303',
            'McLaren': '#FF8C00',
            'Williams': '#006FFF',
            'Mercedes': '#0BE7D1',
            'Red Bull': '#006FFF',
            'Alpine F1 Team': '#F67ED4',
            'AlphaTauri': '#999999',
            'Aston Martin': '#16B98D',
            'Alfa Romeo': '#FF0000',
            'Haas F1 Team': '#FF0000',
        },
        labels={
            'podiums': 'Количество подиумов',
            'name': 'Команды',
        },
    )

    graph_drivers_titles.update_layout(showlegend=False)
    graph_teams_titles.update_layout(showlegend=False)

    drivers_points_dynamic = px.line(
        dataframes['drivers_points_dynamic'],
        x='date_place',
        y='points',
        color='surname',
        markers=True,
        title='По пилотам',
        color_discrete_map={
            'Verstappen': '#006FFF',
            'Hamilton': '#0BE7D1',
            'Bottas': '#00D2BE'
        }
    )

    drivers_points_dynamic.update_layout(
        xaxis_title='Дата и трасса',
        yaxis_title='Очки',
        legend_title='Пилот',
    )

    teams_points_dynamic = px.line(
        dataframes['teams_points_dynamic'],
        x='date_place',
        y='points',
        color='name',
        markers=True,
        title='По командам',
        color_discrete_map={
            'Ferrari': '#CE0303',
            'Mercedes': '#0BE7D1',
            'Red Bull': '#006FFF'
        }
    )

    teams_points_dynamic.update_layout(
        xaxis_title='Дата и трасса',
        yaxis_title='Очки',
        legend_title='Команда',
    )

    geography = px.choropleth(
        locations=dataframes['geography']['country'],
        locationmode='country names',
        color=dataframes['geography']['country'],
        color_continuous_scale='Reds',
    )

    geography.update_geos(
        showcountries=True,
        countrycolor='#444444',
        showcoastlines=True,
        coastlinecolor='#555555',
        showocean=True,
        oceancolor='#111116',
        showland=True,
        landcolor='#222228',
    )

    geography.update_layout(
        showlegend=False,
        margin={'r': 0, 't': 40, 'l': 0, 'b': 0},
        height=600
    )



    with st.container(gap=52):
        with st.container (gap=32):
            with st.container(gap=8):
                st.title('Обзор 2021 года')
                st.write('Итоги сезона, турнирные таблицы, динамика очков и география гонок')

            card1, card2, card3, card4 = st.columns(4)
            card1.metric(label='Чемпион', value=dataframes['driver_champions'].loc[0, 'surname'], border=True)
            card2.metric(label='Очков у чемпиона', value=dataframes['driver_champions'].loc[0, 'points'], border=True)
            card3.metric(label='Чемпион команда', value=dataframes['team_champions'].loc[0, 'name'], border=True)
            card4.metric(label='Очков у команды', value=dataframes['team_champions'].loc[0, 'points'], border=True)

        with st.container(gap=28):
            st.subheader('Кубок конструкторов и личный зачет')
            left_column, right_column = st.columns(2)
            with left_column:
                st.dataframe(dataframes['team_champions'], hide_index=True)
            with right_column:
                st.dataframe(dataframes['driver_champions'], hide_index=True)

        with st.container(gap=0):
            st.subheader('Количество подиумов у команд и пилотов')
            left_column, right_column = st.columns(2)
            with left_column:
                st.plotly_chart(graph_teams_titles)
            with right_column:
                st.plotly_chart(graph_drivers_titles)

        with st.container(gap=0):
            st.subheader('Динамика очков')
            st.plotly_chart(drivers_points_dynamic)
            st.plotly_chart(teams_points_dynamic)

        with st.container(gap=0):
            st.subheader('География Гран-при')
            st.plotly_chart(geography, width='stretch')







