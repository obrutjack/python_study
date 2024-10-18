import random

pwd = random.sample(range(0,10),4)

print(pwd)

A = 0
B = 0

while A!=4: # 當A=4 就跳出, 若A!=4 就執行
    num = input("Please enter 4 digitals within 0-9:")
    while len(num)!=4 or len(set(num))!=4: # 檢查是否四個數字都不一樣, 如果一樣就重複輸入到不一樣為止, 使用 set 特性來增加判斷.
        num = input("Please enter 4 digitals not repeated:")
    list1 = list(map(int,list(num))) # 利用 map 來做型態轉換, 再把 map 位址轉成 list
    print(list1)
    
    A = 0
    B = 0

    for i in list1: # 將 list1 的數值取出來
        if i in pwd: # 再把 pwd 裡的數值也取出來
            if list1.index(i)==pwd.index(i): # 比對兩個數值的位置是否一致
                A+=1 # 如果一樣就 A + 1
            else:
                B+=1 # 不一樣就 B + 1
    print(num,":",A,"A",B,"B",sep="")

print("Good job! The password is ",pwd)