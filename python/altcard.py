
import random

card1 = random.randint(1,52)
card2 = random.randint(1,52)
card3 = random.randint(1,52)
card4 = random.randint(1,52)
card5 = random.randint(1,52)


#if there is a duplicate
if card1 in (card2, card3, card4, card5) or card2 in (card3, card4, card5) or card3 in (card4, card5) or card4 in card5:
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