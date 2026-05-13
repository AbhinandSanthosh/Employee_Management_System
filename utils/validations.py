import re

def validate_name(name):

    return len(name.strip()) > 0

def validate_salary(salary):

    try:

        salary = float(salary)

        return salary >= 0

    except ValueError:

        return False
    
def validate_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(pattern, email)

