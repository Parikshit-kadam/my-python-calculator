# simple calculator

print("Welcome to my calculator")
print("------------------------")

# get the two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nWhat do you want to do?")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice (1-4): ")
print()

if choice == "1":
    result = num1 + num2
    print(num1, "+", num2, "=", result)

elif choice == "2":
    result = num1 - num2
    print(num1, "-", num2, "=", result)

elif choice == "3":
    result = num1 * num2
    print(num1, "*", num2, "=", result)

elif choice == "4":
    # can't divide by 0 so check first
    if num2 == 0:
        print("Error: cannot divide by zero")
    else:
        result = num1 / num2
        print(num1, "/", num2, "=", result)

else:
    print("Invalid choice, please enter 1, 2, 3 or 4")

print("\nThanks for using my calculator!")