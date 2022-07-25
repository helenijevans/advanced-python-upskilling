romInt = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def romanToInt(s: str) -> int:
    total = 0
    for char in s:
        try:
            previousVal = int(romInt.get(prev_char))
        except UnboundLocalError:
            previousVal = int(romInt.get(char))
        currentVal = int(romInt.get(char))
        total += romInt.get(char)
        if currentVal > previousVal:
            total -= 2 * (romInt.get(prev_char))
        prev_char = char

    return total


# print(romanToInt("CC"))



intRom = dict((v, k) for k, v in romInt.items())

def intToRoman(i: int) -> str:
    base = 1
    if i <= 0:
        return ""
    if i in intRom:
        result = intRom.get(i)
        return result
    length = len(str(i))
    potentialMax = base*10**length
    subtractive = base*10**(length-1)
    maxConversion = romInt.get(list(romInt)[-1])

    if potentialMax > maxConversion:
        result = ""
        repeat = i // maxConversion
        for _ in range(repeat):
            result += intRom.get(maxConversion)
    elif str(i)[0] == str(potentialMax - subtractive)[0]:
        result = intRom.get(subtractive) + intRom.get(potentialMax)
    elif potentialMax/2 < i < potentialMax:
        result = intRom.get(potentialMax/2)
    else:
        if str(i)[0] == str(potentialMax/2 - subtractive)[0]:
            result = intRom.get(subtractive) + intRom.get(potentialMax/2)
        else:
            result = intRom.get(subtractive)
    left = (i - romanToInt(result))
    return result + intToRoman(left)

print(intToRoman(1500))

