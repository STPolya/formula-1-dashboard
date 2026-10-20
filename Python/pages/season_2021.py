import streamlit as st

def show_2021(connection, queries):
    st.set_page_config(
        page_title='Обзор 2021 года',
        layout='wide',
    )

    st.title('Обзор 2021 года')
    st.write('Итоги сезона, турнирные таблицы, динамика очков и география гонок')