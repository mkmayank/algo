#!/usr/bin/env python
'''
    https://projecteuler.net/problem=7

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

    What is the 10001st prime number

    $ time ./7.py -n 10001
    n : 10001
    104743

    real    0m0.070s
    user    0m0.060s
    sys     0m0.008s
'''
import argparse
import math

parser = argparse.ArgumentParser()

parser.add_argument('-n', action='store', dest='n',
                    default=10,
                    help='n, number')

cmd_args = parser.parse_args()
N = int(cmd_args.n)

print("n : {}".format(N))

#Sieve_of_Eratosthenes
def get_first_n_primes(n):

    n = n * 20

    n_list = [True] * n
    n_list[0] = False
    n_list[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n_list[i]:
            for j in range(i * i, n, i):
                n_list[j] = False

    p_list = []

    for n, val in enumerate(n_list):
        if val:
            p_list.append(n)

    return p_list

p_list = get_first_n_primes(N)
print p_list[N-1]
