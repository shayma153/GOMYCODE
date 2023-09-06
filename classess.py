class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_coordinates(self):
        return (self.x, self.y, self.z)

# Create an instance of Point3D
mypoint = Point3D(1, 2, 3)

# Print the coordinates of my_point
print(mypoint.get_coordinates())
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create an instance of Rectangle
myrectangle = Rectangle(4, 3)

# Calculate and print the area and perimeter of my_rectangle
print("Area:", myrectangle.area())
print("Perimeter:", myrectangle.perimeter())
import math

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def is_inside(self, x, y):
        distance = math.sqrt((x - self.center_x)**2 + (y - self.center_y)**2)
        return distance <= self.radius

# Create an instance of Circle
my_circle = Circle(0, 0, 5)

# Calculate and print the area and perimeter of my_circle
print("Area:", my_circle.area())
print("Perimeter:", my_circle.perimeter())

# Check if a point is inside the circle
x = 3
y = 4
if my_circle.is_inside(x, y):
    print(f"Point ({x}, {y}) is inside the circle.")
else:
    print(f"Point ({x}, {y}) is outside the circle.")
class Bank:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

# Create an instance of Bank
my_bank = Bank(1000)

# Deposit and withdraw from the account
my_bank.deposit(500)
print("Balance after deposit:", my_bank.balance)

my_bank.withdraw(200)
print("Balance after withdrawal:", my_bank.balance)

my_bank.withdraw(1500)




