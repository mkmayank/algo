#!/usr/bin/env python
'''
    https://projecteuler.net/problem=4

    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    before optimization

    $ time ./4.py
    906609

    real    0m0.549s
    user    0m0.544s
    sys     0m0.004s

    after optimization
    $ time ./4.py
    906609

    real    0m0.016s
    user    0m0.004s
    sys     0m0.008s

'''

def is_palindrome(num):
    if num < 0 :
        return False

    orig = num
    reversed_num = 0
    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num / 10

    return reversed_num == orig

# mx = 0
# for i in range(999,99,-1):
#     for j in range(999,99,-1):
#         if is_palindrome(i*j):
#             if i*j > mx:
#                 mx = i*j
#
# print mx

mx = 0
i = 999
while i >= 100:
    if i % 11 == 0:
        j = 999
        diff = 1
    else:
        j = 990
        diff = 11

    while j >= i:
        if i * j < mx:
            break;

        if is_palindrome(i*j):
                mx = i * j

        j = j - diff

    i = i - 1

print mx
