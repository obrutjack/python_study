setAlpha = set(map(chr,range(97,123)))

print(setAlpha)

print("Please input sentences for testing, use end to exit")

while True:
    temp = input()
    if temp=="end":
        break
    set1 = set(temp.lower())
    if len(set1 & setAlpha) == 26:
        print("They are all 全字母句")
    else:
        print("They are not 全字母句")