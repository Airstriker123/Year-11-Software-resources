#Python simple data types
import datetime

#String
name = "Craig"
lastname = input("Enter your last name " + name + ": ")
fullname = name + " " + lastname 
print(fullname)

#Integer
# notice the need for casting between types with constructor functions str and int
age = 0
age = int(input("Now enter your age " + fullname + ": "))


#Date / Time with datetime constructor
x = datetime.datetime.now()
year = x.year
print(fullname + " you are " + str(age) + " in " + str(year))

#Real numbers with Floating Point
# not need to declare the type but based on the initialisation
score = 0.0
score = 23/30*100
print("Your score is: " + str(score))

#Boolean
if (score < 50):
    passed = False
else:
    passed = True
    
if passed:
    print("Yay, you passed")
    
#Date / Time
print(datetime.datetime.now())