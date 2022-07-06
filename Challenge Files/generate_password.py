diceware_dict = {}
import random


def generate_password(rolls):
    with open("diceware.txt", "r") as f:
        for line in f:
            (key, value) = line[:5], line[5:].strip()
            diceware_dict[int(key)] = value

    sequences = list()
    print("\n🔐 Generated password:")
    if rolls == 0:
        print("> No password can be generated with length 0")
    for _ in range(rolls):
        dice1 = str(random.randint(1, 6))
        dice2 = str(random.randint(1, 6))
        dice3 = str(random.randint(1, 6))
        dice4 = str(random.randint(1, 6))
        dice5 = str(random.randint(1, 6))
        sequences.append(int("".join([dice1, dice2, dice3, dice4, dice5])))

    password = str()
    for sequence in sequences:
        password += diceware_dict[sequence] + " "
    print(password)


print("Welcome to the Sequence Password Generator (powered by Diceware)")
try:
    dice_no = int(input("How many words do you want in your sequence? "))
    generate_password(dice_no)
except ValueError:
    print("Not a valid integer. Exiting program.")



"""
GIVEN SOLUTION
"""
# import secrets
#
# def generate_passphrase(num_words):
#     with open('diceware.wordlist.asc', 'r') as file:
#         lines = file.readlines()[2:7778]
#         word_list = [line.split()[1] for line in lines]
#
#     words = [secrets.choice(word_list) for i in range(num_words)]
#     return " ".join(words)


### REFLECTION ###
# A more concise solution was provided but it didn't reflect the inner workings of the diceware algorithm as the brief
# stated for us to use (using the secrets module to generate a random number instead of dice rolls)

