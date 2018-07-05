#!/usr/bin/env python
'''
    https://projecteuler.net/problem=1

    If we list all the natural numbers below 10
    that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.

    $ time ./1.py
    n : 1000
    233168

    real    0m0.021s
    user    0m0.020s
    sys     0m0.000s
'''

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-n', action='store', dest='n',
                    default=1000,
                    help='n, number')

cmd_args = parser.parse_args()
N = int(cmd_args.n)

print("n : {}".format(N))

def sum_of_first_n_number(n):
    return n * (n + 1) / 2

N -= 1 # below

print 3 * sum_of_first_n_number(N / 3) + 5 * sum_of_first_n_number(N / 5) - 15 * sum_of_first_n_number(N / 15)
