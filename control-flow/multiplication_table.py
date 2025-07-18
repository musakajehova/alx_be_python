#2. Multiplication Table Generator

number = int(input("Enter a number to see its multiplication table:"))

for multiple in range(1, 11):
    print(number, "*", multiple, "=", multiple * number)