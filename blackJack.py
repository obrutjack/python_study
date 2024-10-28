import random

def printCard(c):
    for i in c:
        if i // 13 == 0: 
            print (chr(9824), end="")
        elif i // 13 == 1: 
            print (chr(9829), end="")
        elif i // 13 == 2: 
            print (chr(9830), end="")
        else: 
            print (chr(9827), end="")

        if i % 13 == 0:
            print('A', end=" ")
        elif i % 13 == 10:
            print('J', end=" ")
        elif i % 13 == 11:
            print('Q', end=" ")
        elif i % 13 == 12:
            print('K', end=" ")
        else:
            print(i%13+1, end=" ")
    print()

def printMessage():
    print("Player Card:", end="")
    printCard(playerCard)
    print("Player Point:", sum(playerPoint))
    print("Banker Card:", end="")
    printCard(bankerCard)
    print("Banker Point:", sum(bankerPoint))
    print("***********************************")

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
    gamerPoint.append(cardPoint(temp))

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

printMessage()
#print (playerCard)
#print (playerPoint)
#print (bankerCard)
#print (bankerPoint)

while True:
    ans = input("Player Add Card(Y/N)?")
    if ans == 'N' or ans == 'n':
        break
    deal(playerCard, playerPoint)
    if sum(playerPoint) > 21:
        if 11 in playerPoint:
            playerPoint [playerPoint.index(11)]=1
            printMessage()    
        else:
            printMessage()
            print("Player Dead, Banker WIN!!!")
            break
    else:
        printMessage()

if sum(playerPoint) < 22:
    while sum(bankerPoint) < 17:
        deal(bankerCard,bankerPoint)
        if sum(bankerPoint) > 21:
            if 11 in bankerPoint:
                bankerPoint[bankerPoint.index(11)]=1
            printMessage()
    
    if sum(bankerPoint) > 21:
        print("Banker Dead, Player WIN!!!")
    elif sum(playerPoint) > sum(bankerPoint):
        print("Player WIN!!!")
    elif sum(playerPoint) < sum(bankerPoint):
        print("Banker WIN!!!")
    elif sum(playerPoint) == sum(bankerPoint):
        print("Player and Banker tie")