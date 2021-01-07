
import random

card1 = random.randint(0,52)
card2 = random.randint(0,52)
card3 = random.randint(0,52)
card4 = random.randint(0,52)
card5 = random.randint(0,52)

if card1 == card2 or card3 or card4 or card5:
    print('equal')
elif card2 == card1 or card3 or card4 or card5:
    print('equal')
elif card3 == card1 or card2 or card4 or card5:
    print('equal')
elif card4 == card1 or card2 or card3 or card5:
    print('equal')
elif card5 == card1 or card2 or card3 or card4:
    print('equal')
else:

    print("The first card is:", card1)
    print("The second card is:", card2)
    print("The third card is:", card3)
    print("The fourth card is:", card4)
    print("The fifth card is:", card5)

