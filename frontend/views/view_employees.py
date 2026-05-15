import streamlit as st
import pandas as pd
import requests


def show_view_employees():

    st.title("View Employees")

    try:
        headers = {
            
            "Authorization":
            f"Bearer {st.session_state['token']}"
            }
        
        response = requests.get(
            
            "http://127.0.0.1:8000/employees",
            
            headers=headers
            )
        
        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(data)

            st.dataframe(
                df,
                use_container_width=True
            )

        else:

            st.error(
                "Failed to fetch employees"
            )

    except Exception as e:

        st.error(f"Error: {e}")

    

