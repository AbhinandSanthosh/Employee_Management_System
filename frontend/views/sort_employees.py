import streamlit as st
import pandas as pd
import requests


def show_sort_employees():

    st.title("Sort Employees By Salary")

    sort_order = st.radio(
        "Select Order",
        [
            "Ascending",
            "Descending"
        ]
    )

    if sort_order == "Ascending":

        order = "asc"

    else:

        order = "desc"

    try:

        response = requests.get(

            "http://127.0.0.1:8000/employees/sort",

            params={
                "order": order
            }
        )

        data = response.json()

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True
        )

    except Exception as e:

        st.error(f"Error: {e}")