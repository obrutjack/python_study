list1 = input("Please input first LIST: ").split(" ")
tuple1 = tuple(map(int,list1))

list2 = input("Please input second LIST: ").split(" ")
tuple2 = tuple(map(int,list2))


print("tuple Merge: ",tuple1+tuple2)
print("tuple Merge with Sorted: ",sorted(tuple1+tuple2))


