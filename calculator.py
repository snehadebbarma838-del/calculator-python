# ----- FUNCTIONS -----
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero"
    return a / b

# ----- MAIN CALCULATOR -----
def calculator():
    while True:
        print("\n=============================")
        print("       CALCULATOR APP        ")
        print("=============================")
        print(" 1. Addition       (+)")
        print(" 2. Subtraction    (-)")
        print(" 3. Multiplication (*)")
        print(" 4. Division       (/)")
        print(" 5. Exit")
        print("=============================")

        choice = input("Choose operation (1-5): ")

        if choice == "5":
            print("Thanks for using Calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid! Please choose 1-5")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print(f"\n  {num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"\n  {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"\n  {num1} x {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"\n  {num1} / {num2} = {divide(num1, num2)}")

# ----- RUN -----
calculator()