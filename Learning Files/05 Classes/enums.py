# define enumerations using the Enum base class
# Common feature of many programming languages
# Easy to understand and maintain
# Constant values, not mutable like with namedtuples

from enum import Enum, unique, auto


@unique
class Fruit(Enum):
    # NAME = VALUE
    # can access this using Class.NAME.name -> to get 'NAME'
    # and Class.Name.value -> to get 'VALUE'
    # Duplicate names are not okay, duplicate values are
    # You can prevent duplicate values by importing the 'unique' decorator and adding it to the class
    # If you don't care about the values you can import the auto package from enum which will automatically create one
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()


def main():
    # enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))  # gets a string representation of the object

    # enums have name and value properties
    print(Fruit.APPLE.name, Fruit.APPLE.value)

    # print the auto-generated value
    print(Fruit.PEAR.value)  # Value is 5 which increments from the other values

    # enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Come Mr. Tally-man"
    print(myFruits[Fruit.BANANA])


if __name__ == "__main__":
    main()
