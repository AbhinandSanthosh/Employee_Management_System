import streamlit as st


def sidebar_menu():

    st.sidebar.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=90
    )

    st.sidebar.title("EMS Portal")

    st.sidebar.caption(
        "Employee Management Dashboard"
    )

    st.sidebar.markdown("---")

    menu = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Add Employee",
            "View Employees",
            "Search Employee",
            "Update Salary",
            "Delete Employee",
            "Sort Employees"
        ]
    )

    st.sidebar.markdown("---")

    st.sidebar.info(
        "Built with Streamlit + PostgreSQL"
    )

    return menu