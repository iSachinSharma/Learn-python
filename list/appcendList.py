carsList = ["BMW","Audi","Mustang","Thar","Benz"]

newlist = []

for x in carsList:
    if "B" in x:
        newlist.append(x)

print(newlist)

carsListTow = ["BMW","Audi","Mustang","Thar","Benz","Fortuner"]

carsListTow.sort()

print(carsListTow)


print("-----------------------------------------------------")


carsListTow.sort(reverse= True)

print(carsListTow)