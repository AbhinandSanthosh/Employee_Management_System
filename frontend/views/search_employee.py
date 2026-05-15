import streamlit as st
import requests


def show_search_employee():

    st.title("Search Employee")

    employee_id = st.number_input(
        "Enter Employee ID",
        min_value=1,
        step=1
    )

    if st.button("Search"):

        try:

            response = requests.get(
                f"http://127.0.0.1:8000/employees/{employee_id}"
            )

            data = response.json()

            if "message" in data:

                st.warning(data["message"])

            else:

                st.success("Employee Found")

                st.write(f"ID: {data['id']}")

                st.write(
                    f"Name: {data['employee_name']}"
                )

                st.write(
                    f"Department: {data['department']}"
                )

                st.write(
                    f"Salary: {data['salary']}"
                )

                st.write(
                    f"Email: {data['email']}"
                )

        except Exception as e:

            st.error(f"Error: {e}")