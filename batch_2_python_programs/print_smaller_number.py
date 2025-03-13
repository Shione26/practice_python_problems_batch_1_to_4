# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

# ask user for inputs of two numbers

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

# check which is the smaller number
# print the smaller number

if num1 < num2:
    print(num1, "is the smaller number")
elif num1 > num2:
    print(num2, "is the smaller number")