import random as r

card = int(r.random() * 52)

rank = card // 4 + 1
suit = card % 4

cardName = ""

if rank == 1:
    cardName += "Ace"
elif rank == 2:
    cardName += "Two"
elif rank == 3:
    cardName += "Three"
elif rank == 4:
    cardName += "Four"
elif rank == 5:
    cardName += "Five"
elif rank == 6:
    cardName += "Six"
elif rank == 7:
    cardName += "Seven"
elif rank == 8:
    cardName += "Eight"
elif rank == 9:
    cardName += "Nine"
elif rank == 10:
    cardName += "Ten"
elif rank == 11:
    cardName += "Jack"
elif rank == 12:
    cardName += "Queen"
elif rank == 13:
    cardName += "King"

cardName += " of "

if suit == 0:
    cardName += "Spades"
elif suit == 2:
    cardName += "Hearts"
elif suit == 3:
    cardName += "Diamonds"
elif suit == 4:
    cardName += "Clubs"


print(f"the card is a {cardName}")