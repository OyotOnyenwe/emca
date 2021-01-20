# speed checker

speed = float(input('What is the speed in km? '))

if speed <= 70:
    print('Ok!')
else:
    
    diff = speed - 70
    
    points = diff // 5

    if points >= 12:
        print('Your license has expired.')
    else:
        print('You have accrued', points, 'points.')
    