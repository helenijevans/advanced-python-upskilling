# Use lambdas as in-place functions
# Otherwise it would needlessly increase code complexity and reduce readability

def CelsiusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsius(temp):
    return (temp-32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # Use regular functions to convert temps
    print(list(map(FahrenheitToCelsisus, ftemps)))
    print(list(map(CelsisusToFahrenheit, ctemps)))

    # Use lambdas to accomplish the same thing
    print(list(map(lambda t: (t-32) * 5/9, ftemps)))
    print(list(map(lambda t: (t * 9/5) + 32, ctemps)))


if __name__ == "__main__":
    main()
