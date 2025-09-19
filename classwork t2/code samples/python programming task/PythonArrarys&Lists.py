#Using lists as arrays

#######
#single dimension arrays
#######

#empty list
print("This is an array or list of fibonacci integers")
fib= []

#add a new element with the append function
fib.append(0)
fib.append(1)
x = 2
#populate array with fibonacci numbers
while (x <=20):
    fib.append(fib[x-1] + fib[x - 2])
    x +=1
print(fib)
print()

#########
#Two dimension arrays are created using a list of lists
#########

twoD = [[3,2,1],[6,5,4],[9,8,7]]
print("This is a list of lists with the inside sets of brackets each a set of lists")
print(twoD)

#Each individual number can be accessed by the index of the outside list then the index of the inside list

for x in range(3):
    for y in range(3):
        print (twoD[x][y])

print()

########
#Lists that contain multiple data types
########
mylist = ["Craig", 19, 34.5]
print(mylist[0])
print(mylist[1])
print(mylist[2])
