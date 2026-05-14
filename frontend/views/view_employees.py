import streamlit as st
import pandas as pd

from db import get_connection


def show_view_employees():

    st.title("View Employees")

    try:

        connection = get_connection()

        query = "SELECT * FROM employees"

        df = pd.read_sql(query, connection)

        st.dataframe(
            df,
            use_container_width=True
        )

    except Exception as e:

        st.error(f"Error: {e}")

    finally:

        connection.close()