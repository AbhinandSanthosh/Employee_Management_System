import streamlit as st
import pandas as pd

from db import get_connection


def show_sort_employees():

    st.title("Sort Employees")

    sort_order = st.radio(
        "Sort Salary",
        [
            "Ascending",
            "Descending"
        ]
    )

    try:

        connection = get_connection()

        if sort_order == "Ascending":

            query = """
            SELECT * FROM employees
            ORDER BY salary ASC
            """

        else:

            query = """
            SELECT * FROM employees
            ORDER BY salary DESC
            """

        df = pd.read_sql(query, connection)

        st.dataframe(
            df,
            use_container_width=True
        )

    except Exception as e:

        st.error(f"Error: {e}")

    finally:

        connection.close()