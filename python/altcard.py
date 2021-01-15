
import random

card1 = random.randint(1,52)
card2 = random.randint(1,52)
card3 = random.randint(1,52)
card4 = random.randint(1,52)
card5 = random.randint(1,52)


#if there is a duplicate
if card1 == card2 or card1 == card3 or card1 == card4 or card1 == card5 or card2 == card3 or card2 == card4 or card2 == card5 or card3 == card4 or card3 == card5 or card4 == card5:
    print('Error, regenerating...')
    card1 = random.randint(1,52)
    card2 = random.randint(1,52)
    card3 = random.randint(1,52)
    card4 = random.randint(1,52)
    card5 = random.randint(1,52)

    print(card1)
    print(card2)
    print(card3)
    print(card4)
    print(card5)
else:
    print(card1)
    print(card2)
    print(card3)
    print(card4)
    print(card5)