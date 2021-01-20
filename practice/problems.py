# problems 1-3 on practice packet

#problem 1
num = -3

num += 5

if num >= 0:
    print('Positive or Zero')
else:
    print('Negative Number')

#problem 2
t = float(input('What is your true value?'))
x = float(input('What is your experimental value?'))

error = (abs(t-x)/t)*100

percent = round(error,1)
print('Your percent error is', percent, '%')

#problem 3
a = float(input('Number 1:'))
b = float(input('Number 2:'))
c = float(input('Number 3:'))

max = max(a, b, c)

print('The maximum is ', max)
