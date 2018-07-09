#!/usr/bin/env python
'''
    https://projecteuler.net/problem=5

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

    $ time ./5.py -n 20
    n : 20
    232792560

    real    0m0.045s
    user    0m0.040s
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

factors = []

for i in range(2,N+1):
    j = i
    for f in factors:
        if j % f == 0:
            j = j / f

    factors.append(j)

num = 1
for n in factors:
    num = num * n

print num
