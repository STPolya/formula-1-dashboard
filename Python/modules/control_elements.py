import streamlit as st

def show_year_slider():
    return st.slider(
        'Выберите временной отрезок',
        min_value=1950,
        max_value=2024,
        value=(1950, 2024)
    )

def show_selectbox(text, filter_column):
    return st.selectbox(
        text,
        options=filter_column.tolist(),
    )