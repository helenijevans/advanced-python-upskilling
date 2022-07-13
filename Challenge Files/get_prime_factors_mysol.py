import numpy

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

factors = []
def get_prime_factors(num):
    for i in range(2, num):
        if num % i == 0:
            if is_prime(i):
                factors.append([i, int(num / i)])
            else:
                get_prime_factors(i)
    prime_factors = list(set([pf for sublist in factors for pf in sublist if is_prime(pf)]))
    return prime_factors

print(get_prime_factors(360))

"""
GIVEN SOLUTION
"""
def get_prime_factors(num):
    factors = list()
    divisor = 2
    while (divisor <= num):
        if (num % divisor) == 0:
            factors.append(divisor)
            num /= divisor
        else:
            divisor += 1
    return factors


print(get_prime_factors(36))

### REFLECTION ###
# More simple solution was out there
# Although it feels very much brute force it does has a better complexity
# I was trying to be very efficient from the get go and that actually hindered the complexity
# by working in a way to abstract functionality
