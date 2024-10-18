set1 = set(input("Please input first set:").split(" "))
set2 = set(input("Please input second set:").split(" "))
set3 = set(input("Please input third set:").split(" "))

print("Set2 is subset of Set1:", set2<=set1)
print("Set3 is supersubset of Set1:", set3>=set1)