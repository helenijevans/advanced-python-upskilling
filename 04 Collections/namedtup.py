# Demonstrate the usage of namdtuple objects
# With tuples you can't have named attributes, access via index like point[0], point[1] which isn't as readable
# You could define a class, but that's a bit much if it's a very simple data structure like below


import collections


def main():
    # create a Point namedtuple
    Point = collections.namedtuple("Point", "x y z")

    p1 = Point(10, 20, 5)
    p2 = Point(30, 40, 0)

    print(p1, p2)
    print(p1.x, p1.y)

    # use _replace to create a new instance => replace always needs to be assigned to a new instance
    p1 = p1._replace(x=100)
    print(p1)

# LIMITATIONS:
# You can't use default values, so if the data has large number of optional properties, better to use a class

if __name__ == "__main__":
    main()
