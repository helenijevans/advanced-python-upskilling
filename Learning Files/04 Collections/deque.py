# deque objects are like double-ended queues
# designed to be memory efficient when accessing it from either end
# If you need to be able to operate and work with data from both sides of a list
# e.g. restaurant waiting list/reservations

import collections
import string


def main():
    # initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # deques support the len() function
    print("Item count: {}".format(len(d)))

    # deques can be iterated over
    for elem in d:
        print(elem.upper(), end=",")

    # manipulate items from either end
    d.pop()  # removes last element of the queue
    d.popleft()  # removes first element of the queue
    d.append(2)  # adds X to the back of the queue
    d.appendleft(1)  # adds X to the front of the queue
    print(d)

    # rotate the deque
    print(d)
    d.rotate()  # positive numbers rotate X numbers to right, negative X numbers to left -> default = 1
    print(d)


if __name__ == "__main__":
    main()
