import streamlit as st

import requests


def show_add_employee():

    st.title("Add Employee")

    st.markdown("---")

    with st.container():

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Employee Name",
                placeholder="Enter employee name"
            )

            department = st.selectbox(
                "Department",
                [
                    "IT",
                    "HR",
                    "Finance",
                    "UI/UX",
                    "Marketing",
                    "Operations"
                ]
            )

        with col2:

            salary = st.number_input(
                "Salary",
                min_value=0.0,
                step=1000.0
            )

            email = st.text_input(
                "Email Address",
                placeholder="Enter email"
            )

        st.markdown("")

        if st.button("Add Employee"):
            response = requests.post(
                
                "http://127.0.0.1:8000/employees",
                
                json={
                    
                    "employee_name": name,
                    
                    "department": department,
                    
                    "salary": salary,
                    
                    "email": email
                    }
                )
            
            if response.status_code == 200:

                st.success(
                    "Employee added successfully"
                )

            else:
                st.error(
                    "Failed to add employee"
                )

            

