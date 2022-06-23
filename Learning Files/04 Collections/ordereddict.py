# Demonstrate the usage of OrderedDict objects
# Dictionary object that remembers the order in which items are inserted
# Can substitute an ordereddict anywhere where you would a normal dictionary

# Intent signaling:
# If you use OrderedDict over dict, then your code makes it clear that the order of items in the dictionary is
# important. You’re clearly communicating that your code needs or relies on the order of items in the underlying
# dictionary.

# Control over the order of items:
# If you need to rearrange or reorder the items in a dictionary,
# then you can use .move_to_end() and also the enhanced variation of .popitem().

# Equality test behaviour:
# If your code compares dictionaries for equality,
# and the order of items is important in that comparison, then OrderedDict is the right choice.

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    # create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)
    print(teams)

    # Use popitem to remove the top item
    tm, wl = teams.popitem(False)
    print("Top team: ", tm, wl)

    # What are next the top 4 teams?
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    # test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    print("Equality test: ", a == b)


if __name__ == "__main__":
    main()
