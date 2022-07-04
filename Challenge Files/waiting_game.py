from datetime import datetime
import random


def waiting_game():
    random_no = random.randint(2, 5)
    start = input(f"Your target time is {random_no} seconds.\n"
                  "---Press Enter to Begin---")
    if start == "":
        start_time = datetime.now()
        end = input(f"...Press Enter again after {random_no} seconds")
        if end == "":
            end_time = datetime.now()
            diff_obj = end_time - start_time
            time = float(
                "{seconds}.{milliseconds}".format(seconds=diff_obj.seconds, milliseconds=diff_obj.microseconds))
            print("\nElapsed time: {} seconds\n({} seconds too {})".format(time, round(abs(random_no - time), 3),
                                                                           "fast" if time < random_no else "slow" if time > random_no else "...perfect. Well done!"))


waiting_game()

"""
GIVEN SOLUTION
"""
import time
import random


def waiting_game():
    target = random.randint(2, 4)
    print(f"\nYour target time is {target} seconds")
    input("---Press Enter to Begin---")
    start = time.perf_counter()
    input(f"...Press Enter again after {target} seconds")
    elapsed = time.perf_counter() - start
    print("\nElapsed time: {0:.3f} seconds".format(elapsed))
    if elapsed == target:
        print("Unbelievable, perfect timing")
    elif elapsed < target:
        print("{0:.3f} seconds too fast".format(target - elapsed))
    else:
        print("{0:.3f} seconds too slow".format(target - elapsed))

### REFLECTION
# I honestly prefer my solution, only thing I did not include initially was if it's exactly on time
# This was not specified in the brief but has been addressed now.
