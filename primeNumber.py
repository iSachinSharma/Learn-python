n = 7

if n > 1:
    for i in range(2,int(n/2)+1):
        if n % i == 0:
            print("not a prime no")
            break
    else:
        print("prime no") 

else:
    print(" n not a prime no")       

