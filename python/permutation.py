# permutation & combination calculator

import math

print('Calculator Mode')
print('Input "1" for Permutation or "2" for Combination')
mode = float(input())


if mode == 1:
    print('P(n,r)')
    print('n:')
    n = float(input())
    print('r:')
    r = float(input())

    difference = n - r
    numerator = math.factorial(n)
    denominator = math.factorial(difference)
    result = numerator / denominator

    print('Number of Permutations:')
    print(result)
elif mode == 2:
    print('C(n,r)')
    print('n:')
    n = float(input())
    print('r:')
    r = float(input())

    difference = n - r
    numerator = math.factorial(n)
    denominator = math.factorial(difference)
    rfactorial = math.factorial(r)
    cdenominator = denominator * rfactorial
    result = numerator / denominator
    
    print('Number of Combinations:')
    print(result)
else:
    print('Invalid Input')

