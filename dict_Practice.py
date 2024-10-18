print("Please enter color dict, input end to close")

dict1 = dict()

while True:
    key = input("Key: ")
    if key == 'end':
        break
    value = input("Value: ")
    dict1[key] = value

for i in sorted(dict1.keys()):
    print(i,": ",dict1[i],sep="")