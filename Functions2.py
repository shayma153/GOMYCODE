def calculator(num1, num2):
    operator = input("Enter the operator (+, -, *, /): ")

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

# Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the calculator function and print the result
result = calculator(num1, num2)
print("The result is:", result)
