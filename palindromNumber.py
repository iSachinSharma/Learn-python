num = 12321
hold = 0
temp = num
while num > 0:
    hold = hold * 10 + num % 10
    num = num // 10

if hold == temp:
    print("It's palindrom number")
else:
    print("Not a palindrom number")    

