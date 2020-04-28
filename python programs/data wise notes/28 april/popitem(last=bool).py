# popitem(last=bool)
from collections import OrderedDict


def rem_item_ordDict():
    employee = OrderedDict()
    # add items to my employee
    employee['id'] = 101234
    employee['name'] = 'Krish'
    employee['salary'] = 35000
    employee['loc'] = 'Bngaluru'
    print(employee)
    print()

    # to remove loc(last key) in my employee
    # popitem(last=bool)
    employee.popitem(last=1)
    print(f'After removing loc key in OrderedDict:{employee}')
    print()

    # to remove id(first key) from orderedDict
    employee.popitem(last=0)
    print(f'After removing id key in OrderedDict:{employee}')


def main():
    rem_item_ordDict()


if __name__ == "__main__":
    main()

'''
Output:
OrderedDict([('id', 101234), ('name', 'Krish'), ('salary', 35000), ('loc', 'Bngaluru')])
After removing loc key in OrderedDict: OrderedDict([('id', 101234), ('name', 'Krish'), ('salary', 35000)])
After removing id key in OrderedDict: OrderedDict([('name', 'Krish'), ('salary', 35000)])
'''
