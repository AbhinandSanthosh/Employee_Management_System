import streamlit as st
import requests


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
              headers = {
                   
                   "Authorization":
                   f"Bearer {st.session_state['token']}"
                   }
              
              response = requests.put(
                   
                   f"http://127.0.0.1:8000/employees/{employee_id}",
                   
                   params={
                        "new_salary": new_salary
                        },
                        
                        headers=headers
                        )
              
              data = response.json()
              
              if "message" in data:
                   if data["message"] == "Employee not found":

                    st.warning(data["message"])

              else:

                    st.success(data["message"])

         except Exception as e:

            st.error(f"Error: {e}")