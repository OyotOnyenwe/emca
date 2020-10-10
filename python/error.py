# a = accepted value
# x = result
# d = absoulute error
# r = relative error
# p = relative error as a percent
# s = sigfigs
# sd = significant decimal places

print('Accepted Value: ')
a = int(input())
print('Result: ')
x = int(input())
print('Lowest number of Significant Figures: ')
s = int(input())
print('Lowest number of Significant Decimal Places: ')
sd = int(input())

d = abs(x - a)
round(d, sd)
r = d / a
round(r, s)
p = r * 100

print('Absolute Error:')
print(d)
print('Relative Error (%):')
print(p)
