# Printing a string
print("Hello KMC")

a = 5
b = "5"

print(a+5)
print(b+"5")

# Casting a variable
c = str(5)
d = int(5)

number = 5
answer = number/3

print(answer)

x = "35"
y = "people"
z = "present"

totalStudent = x+" "+y+" "+z

print(totalStudent)

print(type(totalStudent))

p,q,r = 5,3.2,"Hello"

r = 10
print(p+q+r)

krishnaFavFruit = "orange"
swostikFavFruit = "orange"
utsargaFavFruit = "orange"


krishnaFavFruit = swostikFavFruit = utsargaFavFruit = krishnaFavFruit

print(krishnaFavFruit)
print(swostikFavFruit)
print(utsargaFavFruit)

a = 10
x = a
b = x

print(b)


g = 5
h = "People"
i = "Absent"

print(g,h,i)


fistName = "peshal"
currentYear = 2024
suffix = "@gmail.com"

email = fistName+str(currentYear)+suffix
print(email)



# Doing sum without function
a = 5
b = 6
sum = a+b
print(sum)

c = 10
d = 20
sum1 = c+d
print(sum1)

e = 30
f = 40
sum2 = e+f
print(sum2)

g = 50
h = 60
sum3 = g+h
print(sum3)

i = 70
j = 80
sum4 = i+j
print(sum4)

k = 90
l = 100
sum5 = k+l
print(sum5)


# Defining a function
def addFunction(a,b):
    return a+b

sum = addFunction(5,6)
sum1 = addFunction(10,20)
sum2 = addFunction(30,40)
sum3 = addFunction(50,60)
sum4 = addFunction(70,80)
sum5 = addFunction(90,100)
print(sum, sum1, sum2, sum3, sum4, sum5)

# Defining a function to loop from 1 to 50
def loopFunction():
    for i in range(1,100):
        print("MIT-"+str(i))

loopFunction()

# Defining a function to print star
def starFunction():
    for i in range(1,6):
        print("*"*i)

starFunction()
starFunction()