import streamlit as st

def show_drivers(connection, queries):
    st.set_page_config(
        page_title='Детализация по пилотам',
        layout='wide',
    )

    st.title('Детализация по пилотам')
    st.write('Показатели выбранного пилота и его результаты на каждом этапе сезона')