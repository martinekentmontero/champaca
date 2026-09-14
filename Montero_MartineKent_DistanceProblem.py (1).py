import math

# Ask the user to enter the coordinates for the first point.
x1 = float(input("Enter x1:"))
x2 = float(input("Enter x2:"))
# Ask the user to enter the coordinates for the second point.
y1 = float(input("Enter y1:"))
y2 = float(input("Enter y2:"))

# Compute the distance using the distance formula
distance = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))

# Display the distance rounded up to two decimal places
print ("The distance:", distance)
