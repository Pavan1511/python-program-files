# move_to_end()
from collections import OrderedDict


def moving_key_ordDict():
    student = OrderedDict([('usn', '1ms09cs415'), ('name', 'Arjun'), ('cgpa', 8.35), ('sem', 8)])
    print(f"The original OrderedDict:{student}")
    print()

    # move_to_end('key',bool)-->True --->move the key to end of the orderedDict
    student.move_to_end('cgpa', last=True)
    print(f'OrderedDict after moving to the end:{student}')
    print()

    #--->move the key to start of the orderedDict
    student.move_to_end('name', last=False)
    print(f'OrderedDict after moving to the start:{student}')
    print()


def main():
    moving_key_ordDict()


if __name__ == "__main__":
    main()

'''
Output:
The original OrderedDict: OrderedDict([('usn', '1ms09cs415'), ('name', 'Arjun'), ('cgpa', 8.35), ('sem', 8)])
OrderedDict after moving to the end: OrderedDict([('usn', '1ms09cs415'), ('name', 'Arjun'), ('sem', 8), ('cgpa', 8.35)])

OrderedDict after moving to the start: OrderedDict([('name', 'Arjun'), ('usn', '1ms09cs415'), ('sem', 8), ('cgpa', 8.35)])
'''
