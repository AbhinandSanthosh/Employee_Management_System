import streamlit as st



def sidebar_menu():

    st.sidebar.markdown(
        """
        <div style='text-align:center;'>
            <h1 style='color:white;'>EMS Portal</h1>
            <p style='color:#94a3b8;'>
                Enterprise HR Dashboard
            </p>
        </div>
        """,
        unsafe_allow_html=True
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
            "Sort Employees",
            "Export CSV"
        ]
    )

    st.sidebar.markdown("---")

    st.sidebar.success(
        "System Status: Online"
        )

    return menu
