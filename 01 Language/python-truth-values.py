# In general all python objects evaluate to True - this is where they don't

def isPalindrome(word):
    if not word:  # If string is empty -> False. This is also true of any type of collection e.g. (), [], {}
        return False
    else:
        if len(word) == 1:
            return True
        else:
            return word == word[::-1]


print(isPalindrome(""))


def boolNumber(num):
    return bool(num)


# Any number literal equivalent to 0 -> False
print(boolNumber(0))
print(boolNumber(0.0))
print(boolNumber(0j))  # Complex/Imaginary number
print(boolNumber(0 / 5))

# An empty set, aka set() or range(0) are also considered to be Boolean false
# This logic differs to other languages such as Javascript where empty sets and collections still evaluate to True
# Custom-defined objects are by default True however this can change if you override len (0 -> 1) or bool (to be False)


