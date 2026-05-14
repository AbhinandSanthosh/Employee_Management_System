import streamlit as st

from db import get_connection


def show_search_employee():

    st.title("Search Employee")

    employee_id = st.number_input(
        "Employee ID",
        min_value=1,
        step=1
    )

    if st.button("Search"):

        try:

            connection = get_connection()

            cursor = connection.cursor()

            query = """
            SELECT * FROM employees
            WHERE id = %s
            """

            cursor.execute(query, (employee_id,))

            employee = cursor.fetchone()

            if employee:

                st.success("Employee Found")

                st.write(f"ID: {employee[0]}")
                st.write(f"Name: {employee[1]}")
                st.write(f"Department: {employee[2]}")
                st.write(f"Salary: {employee[3]}")
                st.write(f"Email: {employee[4]}")

            else:

                st.warning("Employee not found")

        except Exception as e:

            st.error(f"Error: {e}")

        finally:

            cursor.close()

            connection.close()