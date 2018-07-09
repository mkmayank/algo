#!/usr/bin/env python
'''
    https://projecteuler.net/problem=10

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million

    $ time ./10.py -n 2000000
    n : 2000000
    142913828922

    real    0m0.372s
    user    0m0.340s
    sys     0m0.028s
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

print sum(get_first_n_primes(N))
