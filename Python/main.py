import streamlit as st
from pages import history, season_2021, drivers, teams

pages = [
    st.Page(history.show_history, title="Исторический обзор Формулы 1"),
    st.Page(season_2021.show_2021, title="Обзор 2021 года"),
    st.Page(drivers.show_drivers, title="Детализация по пилотам"),
    st.Page(teams.show_teams, title="Детализация по командам")
]

pg = st.navigation(pages)
pg.run()
