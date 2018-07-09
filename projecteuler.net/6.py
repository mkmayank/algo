#!/usr/bin/env python
'''
    https://projecteuler.net/problem=6

    The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

    $ time ./6.py -n 100
    n : 100
    25164150

    real    0m0.023s
    user    0m0.012s
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

def sum_of_first_n_number(n):
    return n * (n + 1) / 2

def sum_of_first_square_n_number(n):
    return n * (n + 1) * (2*n + 1) / 6

print sum_of_first_n_number(N) * sum_of_first_n_number(N) - sum_of_first_square_n_number(N)
