print("Hello Morning Students!")

a = 5
b = 6
c = 10
d = 20
a = 30

sum =  a+b
print(sum)

sum2 = c+d
print(sum2)

chor = "aashish"
fatah = "aarogya"


print(chor,fatah,str(sum))



print("---------------------")

def sum(a,b):
    return a+b

print(sum(5,6))
print(sum(10,20))
print(sum(30,40))
print(sum(50,60))

print("---------------------")

a = 5
b = 6
c = 10
d = 20
e = 30
f = 40
g = 50
h = 60

sum1 = a+b
sum2 = c+d
sum3 = e+f
sum4 = g+h

print(sum1)
print(sum2)
print(sum3)
print(sum4)




# Defining a function to loop from 1 to 50
def loopFunction():
    for i in range(1,10):
        print("MIT-"+str(i))

loopFunction()


#Defining a flag pattern generator function
def flagFunction():
    for i in range(6,1):
        print("*"*i)

print("----------------------")
print("Normal Flag")
flagFunction()
flagFunction()
print("----------------------")


# Defining a inverted flag pattern

def invertedFlagFunction():
    for i in range(5,0,-1):
        print("*"*i)

print("----------------------")
print("Inverted Flag")
invertedFlagFunction()
invertedFlagFunction()
print("----------------------")