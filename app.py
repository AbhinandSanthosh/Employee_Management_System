from services.employee_services import *

def menu():

    while True:
         print("\n===== Employee Mnagement System =====")

         print("1. Add Employee")
         print("2. View Employees")
         print("3. Search Employee")
         print("4. Update Employee Salary")
         print("5. Delete Employee")
         print("6. Exit")

         choice = input("Enter your choice: ")

         if choice == "1":
              add_employee()

         elif choice == "2":
              view_employees()

         elif choice =="3":
             search_employee()

         elif choice == "4":
             update_employee_salary()

         elif choice == "5":
             delete_employee()

         elif choice == "6":
             print("Exiting program...")
             
             break 

         else:
             print("Invalid choice")

menu()