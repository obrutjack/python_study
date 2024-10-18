isValid = "Password Correct"

pwd = input("Please enter password: ")

if len(pwd) < 8:
    isValid = "Password Incorrect"

if pwd.isalnum() != True:
    isValid = "Password Incorrect"

setAlpha = set(map(chr, range(65,91)))
set1 = set(pwd)
if len(setAlpha & set1)==0:
    isValid = "Password Incorrect"

print(isValid)