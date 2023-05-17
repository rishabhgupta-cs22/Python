import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

print("The area of the cylinder is:", area)
