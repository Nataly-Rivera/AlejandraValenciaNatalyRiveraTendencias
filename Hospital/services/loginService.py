def SearchEmployee(Hospital,username):
    for Employee in Hospital.employees:
        if Employee.username==username:
           return Employee
    return None



