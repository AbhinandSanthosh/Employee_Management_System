import streamlit as st

from db import get_connection


def show_update_salary():

    st.title("Update Salary")

    employee_id = st.number_input(
        "Employee ID",
        min_value=1,
        step=1
    )

    new_salary = st.number_input(
        "New Salary",
        min_value=0.0
    )

    if st.button("Update Salary"):

        try:

            connection = get_connection()

            cursor = connection.cursor()

            query = """
            UPDATE employees
            SET salary = %s
            WHERE id = %s
            """

            cursor.execute(
                query,
                (new_salary, employee_id)
            )

            connection.commit()

            if cursor.rowcount > 0:

                st.success(
                    "Salary updated successfully"
                )

            else:

                st.warning("Employee not found")

        except Exception as e:

            st.error(f"Error: {e}")

        finally:

            cursor.close()

            connection.close()