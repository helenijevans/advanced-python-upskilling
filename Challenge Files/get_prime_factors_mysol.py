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
