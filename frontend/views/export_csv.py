import streamlit as st
import requests


def show_export_csv():

    st.title("Export Employees CSV")

    if st.button("Download CSV"):

        try:

            response = requests.get(
                "http://127.0.0.1:8000/employees/export"
            )

            if response.status_code == 200:

                st.download_button(

                    label="Click Here to Download",

                    data=response.content,

                    file_name="employees.csv",

                    mime="text/csv"
                )

            else:

                st.error("Export failed")

        except Exception as e:

            st.error(f"Error: {e}")