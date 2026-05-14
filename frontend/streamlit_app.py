import streamlit as st

from components.sidebar import sidebar_menu

from views.dashboard import show_dashboard
from views.add_employee import show_add_employee
from views.view_employees import show_view_employees
from views.search_employee import show_search_employee
from views.update_salary import show_update_salary
from views.delete_employee import show_delete_employee
from views.sort_employees import show_sort_employees


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


elif menu == "View Employees":

    show_view_employees()


elif menu == "Search Employee":

    show_search_employee()


elif menu == "Update Salary":

    show_update_salary()


elif menu == "Delete Employee":

    show_delete_employee()


elif menu == "Sort Employees":

    show_sort_employees()