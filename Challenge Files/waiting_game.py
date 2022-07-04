from datetime import datetime
import random

def waiting_game():
    random_no = random.randint(2,5)
    start = input(f"Your target time is {random_no} seconds.\n"
          "---Press Enter to Begin---")
    if start == "":
        start_time = datetime.now()
        end = input(f"...Press Enter again after {random_no} seconds")
        if end == "":
            end_time = datetime.now()
            diff_obj = end_time - start_time
            time = float("{seconds}.{milliseconds}".format(seconds=diff_obj.seconds, milliseconds=diff_obj.microseconds))
            print("\nElapsed time: {} seconds\n({} seconds too {})".format(time, round(abs(random_no-time), 3),
                  "fast" if time < random_no else "slow"))

waiting_game()