import sys
print(sys.version)


print("Hello Wrold !")


if 5 > 5:
    print("first is greater then second")
else:
    print("second is greater then first")    


print("pring number",6,6677776666676, "hello")


print("hello", "world")
print("hello", "," , "world")


x = "John"
y = "Wick"
print(x +" "+ y)

a = str(3.0)
print(a)
print(type(a))

b = float(3.0)
print(b)
print(type(b))

c = int(3.0)
print(c)
print(type(c))







#multiple variables on single line

p, q, l = "orange", "Graps", "Apple"

print(p)
print(q)
print(l)

print()

j = p =s = "orange"

print(j)
print(p)
print(s)

print()


fruits = ["graps", "apple","mango"]

x,y,z = fruits

print(x)
print(y)
print(z)


print()

n = "Sharma"

def myfunc():
    n = "sachin"

    print("My name is : " ,n)

myfunc()



print(n)

print()


# using global into the function

def myglobalfunction():
    global  y 
    y = "Gautam"

    print(y)


myglobalfunction()

print(y)


g = -9j
print(type(g))


print()


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)