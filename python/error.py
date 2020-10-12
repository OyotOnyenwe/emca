# a = accepted value
# x = result
# d = absoulute error
# r = relative error
# p = relative error as a percent
# s = sigfigs
# sd = significant decimal places
# u = units

print('Accepted Value: ')
a = float(input())
print('Result: ')
x = float(input())
print('Units:')
u = input()
#print('Lowest number of Significant Figures: ')
#s = float(input())
#print('Lowest number of Significant Decimal Places: ')
#sd = float(input())

d = abs(x - a)
#d = int(d)
#round(d, sd)
r = d / a
#r = int(r)
#round(r, s)
p = r * 100

print('Absolute Error:')
print(d, u)
print('Relative Error:')
print(p,'%')

