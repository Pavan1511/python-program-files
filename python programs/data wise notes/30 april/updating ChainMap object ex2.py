#Program: 7
# updating ChainMap
from collections import ChainMap


def update_chainmap():
    emp = {'id': 101234, 'name': 'Ramesh', 'salary': 75000}
    emp_101234 = {'age': 35, 'salary': 80000, 'role': 'SE', 'company': 'facebook'}

    # mapping emp & emp_101234
    employee = ChainMap(emp, emp_101234)

    employee['salary'] = 76000

    print(employee)


def main():
    update_chainmap()


if __name__ == "__main__":
    main()
