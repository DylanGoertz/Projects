# Dylan Goertz
# Program status: Complete
# This program takes a class and implements into the main function to
# show a name, id number, department, and job title

from employee import Employee

def main():
    employee_list = []
    for i in range(3):
        name = input('Enter employee name: ')
        id_number = input('Enter employee ID: ')
        department = input('Enter department: ')
        job_title = input('Enter position: ')

        emp = Employee(name, id_number, department, job_title)
        employee_list.append(emp)
        print()

    for count,emp in enumerate(employee_list,start=1):
        print(f'Employee {count} :')
        print(emp)
        print()

main()
