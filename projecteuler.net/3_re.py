#!/usr/bin/env python
'''
    https://projecteuler.net/problem=3

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?

    After solving , I got overview for problem 3, and found out that we don't need to
    find prime numbers first, only factoring will give us prime factor

    $ time ./3_re.py -n 600851475143
    n : 600851475143
    6857

    real    0m0.022s
    user    0m0.016s
    sys     0m0.004s

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

# to factor out 2 completely
if N % 2 == 0:
    last_factor = 2
    N = N / 2
    while N % 2 == 0 :
       N = N / 2
else:
    last_factor = 1

factor = 3
max_factor = math.sqrt(N)

while N > 1 and factor <= max_factor:
    if N % factor == 0:
        last_factor = factor
        while N % factor == 0:
           N = N / factor
        max_factor = math.sqrt(N)
    factor = factor + 2

if N == 1:
    print(last_factor)
else:
    print(N)
