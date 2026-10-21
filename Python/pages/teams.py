import streamlit as st
import pandas as pd

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

    selected_driver = func_show_select('Выберите команду', data['name'])

    queries = func_get_queries()
    dataframes = {name: pd.read_sql_query(sql, connection, params=(selected_driver, )) for name, sql in
                  queries.items()}

    st.title('Детализация по командам')
    st.write('Показатели выбранной команды, вклад её пилотов и динамика результатов за сезон')