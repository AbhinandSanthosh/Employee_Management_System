import streamlit as st

from db import get_connection


def show_delete_employee():

    st.title("Delete Employee")

    employee_id = st.number_input(
        "Employee ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Employee"):

        try:

            connection = get_connection()

            cursor = connection.cursor()

            query = """
            DELETE FROM employees
            WHERE id = %s
            """

            cursor.execute(query, (employee_id,))

            connection.commit()

            if cursor.rowcount > 0:

                st.success(
                    "Employee deleted successfully"
                )

            else:

                st.warning("Employee not found")

        except Exception as e:

            st.error(f"Error: {e}")

        finally:

            cursor.close()

            connection.close()