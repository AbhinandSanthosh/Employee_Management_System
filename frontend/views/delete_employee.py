import streamlit as st
import requests


def show_delete_employee():

    st.title("Delete Employee")

    employee_id = st.number_input(
        "Employee ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Employee"):

        try:

            headers = {

                "Authorization":
                f"Bearer {st.session_state['token']}"
            }

            response = requests.delete(

                f"http://127.0.0.1:8000/employees/{employee_id}",

                headers=headers
            )

            data = response.json()

            if data["message"] == "Employee not found":

                st.warning(data["message"])

            else:

                st.success(data["message"])

        except Exception as e:

            st.error(f"Error: {e}")