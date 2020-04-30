#Program: 6
# If we modify regular dict it will affect ChainMap as well
from collections import ChainMap


def update_chainmap():
    emp = {'id': 101234, 'name': 'Ramesh', 'salary': 75000}
    emp_101234 = {'age': 35, 'salary': 80000, 'role': 'SE', 'company': 'facebook'}

    # mapping emp & emp_101234
    employee = ChainMap(emp, emp_101234)

    emp_101234['role'] = 'Python_Developer'
    emp['salary'] = 76000

    print(employee)


def main():
    update_chainmap()


if __name__ == "__main__":
    main()
