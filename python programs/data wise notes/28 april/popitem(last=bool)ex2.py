# popitem(last=bool)
# removing a specific key in orderedDict
# pop()
from collections import OrderedDict


def rem_item_ordDict():
    employee = OrderedDict()

    # add items to my employee
    employee['id'] = 101234
    employee['name'] = 'Krish'
    employee['salary'] = 35000
    employee['loc'] = 'Bngaluru'
    print(f"OrderedDict before removing salary:{employee}")
    print()
    # pop('key')
    employee.pop('salary')
    print(f"OrderedDict after removing salary:{employee}")


def main():
    rem_item_ordDict()


if __name__ == "__main__":
    main()

'''
Output:
OrderedDict before removing salary: OrderedDict([('id', 101234), ('name', 'Krish'), ('salary', 35000), ('loc', 'Bngaluru')])
OrderedDict after removing salary: OrderedDict([('id', 101234), ('name', 'Krish'), ('loc', 'Bngaluru')])
'''
