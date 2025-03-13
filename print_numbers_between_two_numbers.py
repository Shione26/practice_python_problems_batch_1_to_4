# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

# ask user for inputs of two numbers
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

# get all numbers in between two numbers
for output in range(num1 + 1, num2):
    print(output)    # print output