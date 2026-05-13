from services.employee_services import *

def menu():

    while True:
         print("\n===== Employee Mnagement System =====")

         print("1. Add Employee")
         print("2. View Employees")
         print("3. Search Employee")
         print("4. Update Employee Salary")
         print("5. Delete Employee")
         print("6. Export Employees to CSV")
         print("7. serach by department")
         print("8. sort employee by salary")
         print("9. Exit")

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
             export_to_csv()
        
         elif choice == "7":
            search_by_department()

         elif choice =="8":
             sort_employees_by_salary()
            
         elif choice == "9":
            print("Exiting program...")
             
            break 

         else:
             print("Invalid choice")

menu()