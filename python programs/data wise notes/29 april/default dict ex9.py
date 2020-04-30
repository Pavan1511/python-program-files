#Program: 9
# using list as a default_factory in my defaultdict

from collections import defaultdict


def list_defaultdict():
    aadhar_info = defaultdict(list)  # default_factory
    lst = [('aaddar_no', 265482731827), ('name', 'Arjun'), ('address', 'Bengaluru')]
    # append items to aadhar_info
    for k, v in lst:
        aadhar_info[k].append(v)
    print(aadhar_info)


def main():
    list_defaultdict()


if __name__ == "__main__":
    main()

'''
1st k = aaddar_no , v = 265482731827
2nd k = name , v = Arjun
3rd k = address, v = Begaluru

'''
