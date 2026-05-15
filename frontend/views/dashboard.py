import streamlit as st
import pandas as pd
import requests



def show_dashboard():

    st.title("Employee Analytics Dashboard")

    headers = {
        "Authorization": (
            f"Bearer {st.session_state['token']}"
        )
    }

    response = requests.get(
        "http://127.0.0.1:8000/employees",
        headers=headers
    )

    data = response.json()

    df = pd.DataFrame(data)

    total_employees = len(df)

    total_salary = df["salary"].sum()

    average_salary = df["salary"].mean()

    highest_salary = df["salary"].max()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Employees",
        total_employees
    )

    col2.metric(
        "Total Salary",
        f"₹ {total_salary:,.0f}"
    )

    col3.metric(
        "Average Salary",
        f"₹ {average_salary:,.0f}"
    )

    col4.metric(
        "Highest Salary",
        f"₹ {highest_salary:,.0f}"
    )

    st.markdown("---")

    left, right = st.columns([2,1])

    with left:

        st.subheader("Employee Database")

        st.dataframe(
            df,
            width="stretch"
        )

    with right:

        st.subheader("Department Distribution")

        department_data = (
            df["department"]
            .value_counts()
        )

        st.bar_chart(department_data)