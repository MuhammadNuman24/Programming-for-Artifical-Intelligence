import itertools as it
import sympy as sp

def check_prime(x):
    return sp.isprime(x)

def get_primes_in_list(nums):
    return [x for x in nums if check_prime(x)]

def get_first_n_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if check_prime(num):
            primes.append(num)
        num += 1
    return primes

list_nums = (23, 4, 27, 17, 13, 10, 21, 29, 3, 32, 11, 19)

print('\nList of primes in the list:')
print(set(get_primes_in_list(list_nums)))

print('\nList of first 7 prime numbers:')
print(get_first_n_primes(7))