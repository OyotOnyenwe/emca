#program to draw 5 cards from a standard 52 deck of cards

import random

number1 = random.choice(('ace  ','2    ','3    ','4    ','5    ','6    ','7    ','8    ','9    ','10    ','jack ','queen','king '))
number2 = random.choice(('ace  ','2    ','3    ','4    ','5    ','6    ','7    ','8    ','9    ','10    ','jack ','queen','king '))
number3 = random.choice(('ace  ','2    ','3    ','4    ','5    ','6    ','7    ','8    ','9    ','10    ','jack ','queen','king '))
number4 = random.choice(('ace  ','2    ','3    ','4    ','5    ','6    ','7    ','8    ','9    ','10    ','jack ','queen','king '))
number5 = random.choice(('ace  ','2    ','3    ','4    ','5    ','6    ','7    ','8    ','9    ','10    ','jack ','queen','king '))

suit1 = random.choice(('hearts','diamonds','clubs','spades'))
suit2 = random.choice(('hearts','diamonds','clubs','spades'))
suit3 = random.choice(('hearts','diamonds','clubs','spades'))
suit4 = random.choice(('hearts','diamonds','clubs','spades'))
suit5 = random.choice(('hearts','diamonds','clubs','spades'))

card1 = number1, suit1
card2 = number2, suit2
card3 = number3, suit3
card4 = number4, suit4
card5 = number5, suit5

#if the same card appears twice
if card1 in (card2, card3, card4, card5) or card2 in (card3, card4, card5) or card3 in (card4, card5) or card4 in card5:
    print('Error, regenerating...')
    
    number1 = random.choice(('ace  ','2    ','3    ','4    ','5    ','6    ','7    ','8    ','9    ','10    ','jack ','queen','king '))
    number2 = random.choice(('ace  ','2    ','3    ','4    ','5    ','6    ','7    ','8    ','9    ','10    ','jack ','queen','king '))
    number3 = random.choice(('ace  ','2    ','3    ','4    ','5    ','6    ','7    ','8    ','9    ','10    ','jack ','queen','king '))
    number4 = random.choice(('ace  ','2    ','3    ','4    ','5    ','6    ','7    ','8    ','9    ','10    ','jack ','queen','king '))
    number5 = random.choice(('ace  ','2    ','3    ','4    ','5    ','6    ','7    ','8    ','9    ','10    ','jack ','queen','king '))

    suit1 = random.choice(('hearts','diamonds','clubs','spades'))
    suit2 = random.choice(('hearts','diamonds','clubs','spades'))
    suit3 = random.choice(('hearts','diamonds','clubs','spades'))
    suit4 = random.choice(('hearts','diamonds','clubs','spades'))
    suit5 = random.choice(('hearts','diamonds','clubs','spades'))

    print(number1, 'of', suit1)
    print(number2, 'of', suit2)
    print(number3, 'of', suit3)
    print(number4, 'of', suit4)
    print(number5, 'of', suit5)
else: 
    print(number1, 'of', suit1)
    print(number2, 'of', suit2)
    print(number3, 'of', suit3)
    print(number4, 'of', suit4)
    print(number5, 'of', suit5)
