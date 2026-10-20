import streamlit as st

def show_teams(connection, queries):
    st.set_page_config(
        page_title='Детализация по командам',
        layout='wide',
    )

    st.title('Детализация по командам')
    st.write('Показатели выбранной команды, вклад её пилотов и динамика результатов за сезон')