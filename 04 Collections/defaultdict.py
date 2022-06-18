# Demonstrate the usage of defaultdict objects
# Helps with common scenarios where the normal dict will need more code
# Can make your code simpler to read and test

from collections import defaultdict


def main():
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    # use a dictionary to count each element
    fruitCounter = defaultdict(int)
    # Inside the bracket (int) you put in a factory method
    # This is how the default keys are chosen. This time using an integer
    # You can also define your own factory methods e.g. a lambda function

    # Count the elements in the list
    for fruit in fruits:
        # The below lines is what you would need if FruitCounter was a normal dictionary e.g. '{}'
        # if fruit in fruitCounter.keys():
        #     fruitCounter[fruit] += 1
        # else:
        #     fruitCounter[fruit] = 1
        fruitCounter[fruit] += 1



    # print the result
    for (k, v) in fruitCounter.items():
        print(k + ": " + str(v))

    # LIMITATIONS
    # Do not use this structure when it's important to know if you're missing a key


if __name__ == "__main__":
    main()
