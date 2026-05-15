import streamlit as st

from components.sidebar import sidebar_menu

from views.dashboard import show_dashboard
from view.add_employee import show_add_employee


st.set_page_config(
    page_title="Employee Management System",
    page_icon="💼",
    layout="wide"
)


with open("frontend/styles/custom.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )


menu = sidebar_menu()


if menu == "Dashboard":

    show_dashboard()


elif menu == "Add Employee":

    show_add_employee()