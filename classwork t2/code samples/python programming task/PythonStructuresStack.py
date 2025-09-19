

myliststack = []

#adding elements using the append function
myliststack.append('a')
myliststack.append('b')
myliststack.append('c')

print('Initial myliststack')
#print whole list
print(myliststack)
#print first element
print(myliststack[0])

#Use the pop function to remove elements from the list 
print('\nElements popped from myliststack:')
print(myliststack)
print(myliststack.pop())
print(myliststack)
print(myliststack.pop())
print(myliststack)
print(myliststack.pop())

print('\nStack after elements are popped:')
print(myliststack)


