class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_triangle_type(self):
        if self.side1 == self.side2 == self.side3:
            return "Equilateral"
        elif self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3:
            if self.is_right_triangle():
                return "Isosceles Right-Angled"
            else:
                return "Isosceles"
        elif self.is_right_triangle():
            return "Right-Angled"
        else:
            return "Scalene"

    def is_right_triangle(self):
        sides = sorted([self.side1, self.side2, self.side3])
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2


# Get user input for the three sides
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

# Create an instance of the Triangle class
triangle = Triangle(side1, side2, side3)

# Get the type of triangle
triangle_type = triangle.get_triangle_type()

# Print the type of triangle
print("The entered triangle is:", triangle_type)
