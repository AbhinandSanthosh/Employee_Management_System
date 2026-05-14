import streamlit as st

from db import get_connection


def show_add_employee():

    st.title("Employee Management System")

    st.markdown("### Add New Employee")

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

            try:

                connection = get_connection()

                cursor = connection.cursor()

                query = """
                INSERT INTO employees
                (employee_name, department, salary, email)

                VALUES (%s, %s, %s, %s)
                """

                values = (
                    name,
                    department,
                    salary,
                    email
                )

                cursor.execute(query, values)

                connection.commit()

                st.success(
                    "Employee added successfully"
                )

            except Exception as e:

                st.error(f"Error: {e}")

            finally:

                cursor.close()

                connection.close()