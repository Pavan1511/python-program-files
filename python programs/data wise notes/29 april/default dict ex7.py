#Program: 7
# using int as a default_factory fucntion in defaultdict

from collections import defaultdict


def demo_int_default_factory():
    animal = defaultdict(int)  # int as default_factory function -- int supplys 0 as default value

    animal['name'] = 'Tiger'
    animal['color'] = 'yellow'

    print(animal['name'])  # Tiger
    print(animal['color'])  # yellow

    print(animal['age'])  # 0


def main():
    demo_int_default_factory()


if __name__ == "__main__":
    main()
