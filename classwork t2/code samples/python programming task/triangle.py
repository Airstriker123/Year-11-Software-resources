def lengthsGreaterZero(a,b,c):
    return a > 0 and b > 0 and c > 0

def isValidTriangle(a,b,c):
    return (a + b >= c) and (b + c >= a) and (c + a >=b)

def typeTriangle(a,b,c):
    if a == b == c:
        return("Equilateral triangle")
    elif a != b != c:
        if c**2 == a**2 + b**2:
            return("Right angle triangle")
        else:
            return("Scalene triangle")
    elif a == b or b == c or a == c:
        return("Isosceles triangle")
    

print("Which triangle is it game")

testMoreLengths = True

while (testMoreLengths == True):
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))

    if lengthsGreaterZero(a,b,c) and isValidTriangle(a,b,c):
        print(typeTriangle(a,b,c))
    else:
        print ("This is not a triangle")
    response = input("Do you want to test more lengths (y/n): ")
    
    if response.lower() == "n":
        testMoreLengths = False
    

        
