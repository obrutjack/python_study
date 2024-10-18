import random

lottoNumber = list()

for i in range(8):
    temp = random.randint(1,10)
    while temp in lottoNumber:
        temp = random.randint(1,10)
    lottoNumber.append(temp)

special = lottoNumber.pop()

print("Lotto Numbers are ",sorted(lottoNumber))
print("Lotto Special Number is ", special)

