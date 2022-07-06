import random
from collections import Counter
from prettytable import PrettyTable

def roll_dice(*args):
    numbers = []
    rolls = 1000000
    for _ in range(rolls):
        sum = 0
        for dice in args:
            sum += random.randint(1, dice)
        numbers.append(sum)
    data = sorted(Counter(numbers).items())
    print("\n-- TABLE OF PROBABILITY --")
    print(f"When rolling dice with sides: {args}")
    myTable = PrettyTable(["Result", "Percentage (%)"])
    for record in data:
        myTable.add_row([record[0], round((record[1]/rolls)*100, 2)])

    print(myTable)

roll_dice(6,6)

"""
GIVEN SOLUTION
"""
# from random import randint
# from collections import Counter
#
# def roll_dice(*dice, num_trials = 1_000_000):
#     counts = Counter()
#     for roll in range(num_trials):
#         counts[sum((randint(1, sides) for sides in dice))] += 1
#
#     print("\nOUTCOME\tPROBABILITY")
#     for outcome in range(len(dice), sum(dice) + 1):
#         print('{}\t{:0.2f}%'.format(outcome, counts[outcome]*100/num_trials))
#
# roll_dice(20,6,4)


### REFLECTION ###
# Solution given has a better complexity
# The one I devised has in my opinion better formatting
# The main logic was very much the same, as we imported the same two modules to help
