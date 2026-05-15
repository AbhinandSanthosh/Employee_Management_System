import streamlit as st

from frontend.components.sidebar import sidebar_menu

from frontend.views.dashboard import show_dashboard
from frontend.views.add_employee import show_add_employee
from frontend.views.view_employees import show_view_employees
from frontend.views.search_employee import show_search_employee
from frontend.views.update_salary import show_update_salary
from frontend.views.delete_employee import show_delete_employee
from frontend.views.sort_employees import show_sort_employees
from frontend.views.export_csv import show_export_csv

from frontend.views.login import show_login
from frontend.views.login import logout

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

st.markdown(
    """
    <div style='padding:10px;'>
        <h1 style='color:white;'>
            Employee Management System
        </h1>
    </div>
    """,
    unsafe_allow_html=True
)

if "logged_in" not in st.session_state:

    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:

    show_login()

    st.stop()

if st.sidebar.button("Logout"):

    logout()


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

elif menu == "Export CSV":

    show_export_csv()
