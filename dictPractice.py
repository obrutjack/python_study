dict1 = dict()
dict2 = dict()

print("Please input first dict: ")
while True:
    key = input("Key: ")
    if key=='end':
        break  
    value = input("Value: ")
    dict1[key] = value

print("Please input second dict: ")
while True:
    key = input("Key: ")
    if key=='end':
        break  
    value = input("Value: ")
    dict2[key] = value

dict1.update(dict2)

for i in sorted(dict1.keys()):
    print(i,": ",dict1[i],sep="")