from math import sqrt

# Distance Calculator Between 2 Points

x1 =int(input("Enter x1: "))
y1 =int(input("Enter y1: "))
x2 =int(input("Enter x2: "))
y2 =int(input("Enter y2: "))

distance =sqrt(pow((x2-x1),2)+pow((y2-y1),2))

print(f"the distance is: {distance:.2f} ")

# Reflection
# - The math library helped me by removing the need to write long formulas which helped me save time.
# It also provided alternatives compared to writing the formula manually.




