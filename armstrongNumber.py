num = 153
temp =0
compare = num
sum = 0

while num > 0:
    temp = temp * 10 + num % 10
    sum = sum + (temp * temp * temp)
    num = num // 10

if sum == compare:
    print("It's Armstrong number")
else:
    print("Palindrom number")