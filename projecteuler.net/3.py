#!/usr/bin/env python
'''
    https://projecteuler.net/problem=3

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

    $ time ./3.py -n 600851475143
    n : 600851475143
    6857

    real    0m0.131s
    user    0m0.116s
    sys     0m0.012s
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

for p in reversed(get_first_n_primes(int(math.sqrt(N))+1)):
    if N % p == 0:
        print p
        break;
