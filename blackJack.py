import random

def cardPoint(x):
    if x % 13 == 0: # 代表A
        return 11
    elif x % 13 > 9: # 代表J,Q,K
        return 10
    else:
        return x % 13 + 1

def deal(gamerCard, gamerPoint):
    temp = card.pop()
    gamerCard.append(temp)
    gamerPoint(cardPoint(temp))

card = list(range(0,52))
random.shuffle(card)

#print(card)

playerCard = list()
playerPoint = list()
bankerCard = list()
bankerPoint = list()

for i in range(2):
    deal(playerCard, playerPoint)

deal(bankerCard, bankerPoint)

print (playerCard)
print (playerPoint)
print (bankerCard)
print (bankerPoint)