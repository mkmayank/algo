#!/usr/bin/env python
'''
    https://projecteuler.net/problem=9

    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2
    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

    $ time ./9.py
    31875000

    real    0m0.021s
    user    0m0.016s
    sys     0m0.004s

'''

import math

# Euclid's formula
#    m > n > 0
#   a=mm - nn
#   b=2mn
#   c=mm + nn
#
# So, m and n can go only to sqrt(N/2)

N = int(math.sqrt(1000/2)) + 1

for m in range(1, N):
    for n in range(m+1, N):
        a = n*n - m*m
        b = 2 * n * m
        c = n*n + m*m

        if ( a + b + c == 1000):
            print a * b * c
