list1 = list()

count=1

while True:
    num = int (input("Please input "+str(count)+" number: "))
    if num == -9999:
        break
    list1.append(num)
    count+=1

tuple1 = tuple(list1)

print(tuple1)
print("Length:", len(tuple1))
print("Max:", max(tuple1))
print("Min:", min(tuple1))
print("Sum:", sum(tuple1))
