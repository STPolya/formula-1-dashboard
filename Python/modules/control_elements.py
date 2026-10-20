import streamlit as st

def show_slider():
    return st.slider(
        'Выберите временной отрезок',
        min_value=1950,
        max_value=2024,
        value=(1950, 2024)
    )