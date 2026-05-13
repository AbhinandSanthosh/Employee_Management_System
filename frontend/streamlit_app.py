import streamlit as st
from db import get_connection
import pandas as pd

st.title("Employee Management System")
menu = [
    "Add Employee",
    "View Employees",
    "Search Employee",
    "Update Salary",
    "Delete Employee",
    "Sort Employees",
    "Export CSV"
]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Employee":
    st.subheader("Add New Employee")

elif choice == "View Employees":

    st.subheader("All Employees")

    try:

        connection = get_connection()

        query = "SELECT * FROM employees"

        df = pd.read_sql(query, connection)

        st.dataframe(df)

    except Exception as e:

        st.error(f"Error: {e}")

    finally:

        connection.close()


elif choice == "Search Employee":

    st.subheader("Search Employee")

    employee_id = st.number_input(
        "Enter Employee ID",
        min_value=1,
        step=1
    )

    if st.button("Search"):

        try:

            connection = get_connection()

            cursor = connection.cursor()

            query = """
            SELECT * FROM employees
            WHERE id = %s
            """

            cursor.execute(query, (employee_id,))

            employee = cursor.fetchone()

            if employee:

                st.success("Employee Found")

                st.write(f"ID: {employee[0]}")
                st.write(f"Name: {employee[1]}")
                st.write(f"Department: {employee[2]}")
                st.write(f"Salary: {employee[3]}")
                st.write(f"Email: {employee[4]}")

            else:

                st.warning("Employee not found")

        except Exception as e:

            st.error(f"Error: {e}")

        finally:

            cursor.close()

            connection.close()

elif choice == "Update Salary":

    st.subheader("Update Employee Salary")

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

            connection = get_connection()

            cursor = connection.cursor()

            query = """
            UPDATE employees
            SET salary = %s
            WHERE id = %s
            """

            cursor.execute(query, (new_salary, employee_id))

            connection.commit()

            if cursor.rowcount > 0:

                st.success("Salary updated successfully")

            else:

                st.warning("Employee not found")

        except Exception as e:

            st.error(f"Error: {e}")

        finally:

            cursor.close()

            connection.close()

elif choice == "Delete Employee":

    st.subheader("Delete Employee")

    employee_id = st.number_input(
        "Employee ID to Delete",
        min_value=1,
        step=1
    )

    if st.button("Delete Employee"):

        try:

            connection = get_connection()

            cursor = connection.cursor()

            query = """
            DELETE FROM employees
            WHERE id = %s
            """

            cursor.execute(query, (employee_id,))

            connection.commit()

            if cursor.rowcount > 0:

                st.success("Employee deleted successfully")

            else:

                st.warning("Employee not found")

        except Exception as e:

            st.error(f"Error: {e}")

        finally:

            cursor.close()

            connection.close()

elif choice == "Sort Employees":

    st.subheader("Sort Employees By Salary")

    sort_order = st.radio(
        "Select Order",
        ["Ascending", "Descending"]
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

        st.dataframe(df)

    except Exception as e:

        st.error(f"Error: {e}")

    finally:

        connection.close()

    name = st.text_input("Employee Name")

    department = st.text_input("Department")

    salary = st.number_input("Salary", min_value=0.0)

    email = st.text_input("Email")

    if st.button("Add Employee"):
        try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            INSERT INTO employees
            (employee_name, department, salary, email)

            VALUES (%s, %s, %s, %s)
            """          
            values = (name, department, salary, email) 
            cursor.execute(query, values)

            connection.commit()

            st.success("Employee added successfully")

        except Exception as e:
            st.error(f"error: {e}")

        finally:
            cursor.close()

            connection.close()