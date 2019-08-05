
numb_1 = input("What is your first number?:")
equa = input("Now enter what operation you want to do:")
numb_2 = input("Now enter the second number:")

if equa == "+":
    print(float(numb_1) + float(numb_2))

if equa == "*":
        print(float(numb_1) * float(numb_2))

if equa == "-":
        print(float(numb_1) - float(numb_2))

if equa == "/":
        print(float(numb_1) / float(numb_2))
else:
    print(" ")
    print("Invalid Operator.")

input("Press Enter to Exit the Program.")
