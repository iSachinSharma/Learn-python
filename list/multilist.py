thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist)

print(thislist[2:5])

print(thislist[:5])

print(thislist[5:])

print(thislist[-1])

print("---------------------------------------")

print(thislist[:-1])

print("---------------------------------------")


#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[-4:-1])

print("---------------------------------------")


print(thislist[-1:-4])


print(thislist[5:2])


#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


if "apple" in thislist:
    print("apple into the list.")


thislist.remove("apple")

print(thislist)


thislist.pop(1)

print(thislist)


print("-------------------------------------------------------")

thislist.pop()

print(thislist)

print("-----------------------")


del thislist[0]

print(thislist)


print("-----------------------")


thislist.clear()

print(thislist)