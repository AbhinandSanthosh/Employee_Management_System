from db import get_connection
from utils.validations import *
import csv

def add_employee():
    
    connection = None
    cursor = None

    name = input("Enter employee name: ")
    department = input("Enter department: ")
    salary = input("Enter salary: ")
    email = input("Enter email: ")

    if not validate_name(name):
           print("Invalid employee name")
           return
        
    if not validate_salary(salary):
        print("Invalid salary")
        return
        
    if not validate_email(email):
        print("Invalid email format")
        return
        
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
        print("Employee added successfully")
        
    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
              cursor.close()
        if connection:
              connection.close()
              
def view_employees():
      connection = None
      cursor = None
      
      try:
            connection = get_connection()
            cursor = connection.cursor()

            query = "SELECT * FROM employees"

            cursor.execute(query)
            employees = cursor.fetchall()

            if not employees:
                  print("No employees found")
                  
                  return
            
            print("\n===== Employee Records =====")

            for employee in employees:
                  print(f"""
                        ID: {employee[0]}
                        Name: {employee[1]}
                        Department: {employee[2]}
                        Salary: {employee[3]}
                        Email: {employee[4]}
                        Created At: {employee[5]}
                        """)
                  
      except Exception as e:
            print("Error:", e)

      finally:
            if cursor:
                  cursor.close()
            if connection:
                  connection.close()

def search_employee():
          
          connection = None
          cursor = None

          employee_id = input("Enter employee ID: ")

          if not employee_id.isdigit():
                print("Invalid employee ID")
                return
          
          try:
                connection = get_connection()
                cursor = connection.cursor()
                
                query = """
                SELECT * FROM employees
                WHERE id = %s
                """

                cursor.execute(query, (employee_id,))

                employee = cursor.fetchone()

                if not employee:
                      print("Employee not found")
                      return
                
                print(f"""
                      Employee Found
                      
                      ID: {employee[0]}
                      Name: {employee[1]}
                      Department: {employee[2]}
                      Salary: {employee[3]}
                      Email: {employee[4]}
                      Created At: {employee[5]}
                      """)
                
          except Exception as e:
                print("Error:", e)

          finally:
                if cursor:
                      cursor.close()
                if connection:
                      connection.close()

#search_employee()     

def update_employee_salary():
      connection = None
      cursor = None

      employee_id = input("Enter employee ID: ")

      if not employee_id.isdigit():
            print("Invalid employee ID")
            return
      
      new_salary = input("enter new salary: ")

      if not validate_salary(new_salary):
            print("Invalid salary")
            return
      
      try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            UPDATE employees
            SET salary = %s
            WHERE id = %s
            """
            cursor.execute(query, (new_salary, employee_id))

            if cursor.rowcount == 0:
                  print("Employee not found")
                  return
            
            connection.commit()

            print("Salary updated successfully")

      except Exception as e:
            print("Error:",e)

      finally:
            if cursor:
                  cursor.close()

            if connection:
                  connection.close()
                        
#update_employee_salary()    

def delete_employee():
      connection = None
      cursor = None

      employee_id = input("Enter employee ID to delete: ")

      if not employee_id.isdigit():
            print("Invalid employee ID")
            return
      
      try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            DELETE FROM employees
            WHERE id = %s
            """

            cursor.execute(query, (employee_id))

            if cursor.rowcount == 0:
                  print("Employee not found")
                  return
            
            connection.commit()

            print("employee deleted successfully")

      except Exception as e:
            print("Error:",e)

      finally:
            if cursor:
                  cursor.close()
            
            if connection:
                  connection.close()

def export_to_csv():
      
      connection = None
      cursor = None

      try:
            connection = get_connection()
            cursor= connection.cursor()

            query = "SELECT * FROM employees"
            cursor.execute(query)

            employees = cursor.fetchall()

            if not employees:
                  print("no employee data found")
                  return
            
            with open("exports/employees.csv", mode="w", newline="") as file:
                  writer = csv.writer(file)

                  writer.writerow([
                        "ID",
                        "Name",
                        "Department",
                        "Salary",
                        "Email",
                        "Created At"
                  ])

                  writer.writerows(employees)
                  print("Employee data exported successfully")

      except Exception as e:
            print("Error:",e)

      finally:
            if cursor:
                  cursor.close()
            
            if connection:
                  connection.close()


def search_by_department():
      connection = None
      cursor = None

      department = input("Enter department name: ")

      if not department.strip():
            print("Department Cannot be empty")
            return
      
      try:
            connection = get_connection()
            cursor = connection.cursor()

            query = """
            SELECT * FROM employees
            WHERE department = %s
            """
            cursor.execute(query, (department,))
            employees = cursor.fetchall()

            if not employees:
                  print("no employees found in this department")
                  return
            
            print(f"\nEmployees in {department} Department")

            for employee in employees:
                  print(f"""
                        ID: {employee[0]}
                        Name: {employee[1]}
                        Department: {employee[2]}
                        Salary: {employee[3]}
                        Email: {employee[4]}
                        Created At: {employee[5]}
                        """)
                  
      except Exception as e:
            print("Error:", e)

      finally:
            if cursor:
                  cursor.close()
            if connection:
                  connection.close()


def sort_employees_by_salary():
      connection =  None
      cursor = None

      print("\nSort Employees By Salary")
      print("1. Ascending")
      print("2. Descending")

      choice = input("Enter your choice: ")
      
      if choice not in ["1", "2"]:
            print("Invalid choice")
            return
      
      try:
            connection = get_connection()
            cursor = connection.cursor()

            if choice == "1":
                  query = """
                  SELECT * FROM employees
                  ORDER BY salary ASC
                  """

            else:
                  query = """
                  SELECT * FROM employees
                  ORDER BY salary DESC
                  """

                  cursor.execute(query)
                  employees = cursor.fetchall()

                  if not employees:
                        print("No employees found")
                        return
                  
                  print("\nEmployees sorted by salary")

                  for employee in employees:
                        
                        print(f"""
                              ID: {employee[0]}
                              Name: {employee[1]}
                              Department: {employee[2]}
                              Salary: {employee[3]}
                              Email: {employee[4]}
                              Created At: {employee[5]}
                              """)     
                        
      except Exception as e:
            print("Error:", e)

      finally:
            if cursor:
                  cursor.close()

            if connection:
                  connection.close()

