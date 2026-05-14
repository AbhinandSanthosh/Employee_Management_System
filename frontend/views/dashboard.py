import streamlit as st
import pandas as pd

from db import get_connection


def show_dashboard():

    st.title("Employee Dashboard")

    st.markdown("---")

    try:

        connection = get_connection()

        query = "SELECT * FROM employees"

        df = pd.read_sql(query, connection)

        total_employees = len(df)

        total_salary = df["salary"].sum()

        average_salary = df["salary"].mean()

        highest_salary = df["salary"].max()

        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Total Employees",
                total_employees
            )

        with col2:

            st.metric(
                "Total Salary",
                f"₹ {total_salary:,.0f}"
            )

        with col3:

            st.metric(
                "Average Salary",
                f"₹ {average_salary:,.0f}"
            )

        with col4:

            st.metric(
                "Highest Salary",
                f"₹ {highest_salary:,.0f}"
            )

        st.markdown("---")

        st.subheader("Employee Records")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.markdown("---")
        
        st.subheader("Department Distribution")
        department_data = (
            df["department"]
            .value_counts()
            )
        st.bar_chart(department_data)

    except Exception as e:

        st.error(f"Error: {e}")

    finally:

        connection.close()