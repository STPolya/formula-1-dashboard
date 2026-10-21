# python -m streamlit run "D:\Пет проекты\formula-1-dashboard\Python\main.py"

import sqlite3
from pathlib import Path
import streamlit as st
from pages import history, season_2021, drivers, teams
from modules.queries import history_sql_queries, season_21_sql_queries, drivers_sql_queries, teams_sql_queries
from modules.control_elements import show_year_slider, show_selectbox

PARENT_FOLDER = Path(__file__).parent.parent
BD_PATH = PARENT_FOLDER / 'database' / 'f1.db'

connection = sqlite3.connect(BD_PATH)

try:
    pages = [
        st.Page(lambda: history.show_history(connection, history_sql_queries, show_year_slider), title='Исторический обзор Формулы 1', url_path='history'),
        st.Page(lambda: season_2021.show_2021(connection, season_21_sql_queries), title='Обзор 2021 года', url_path='2021'),
        st.Page(lambda: drivers.show_drivers(connection, drivers_sql_queries, show_selectbox), title='Статистика пилотов за 2021', url_path='drivers'),
        st.Page(lambda: teams.show_teams(connection, teams_sql_queries, show_selectbox), title='Статистика команд за 2021', url_path='teams'),
    ]

    pg = st.navigation(pages)
    pg.run()

finally:
    connection.close()