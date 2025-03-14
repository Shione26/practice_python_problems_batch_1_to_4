# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

# create a list
numbers = []

# ask the user for 10 inputs
for number_count in range(10):
    number = int(input(f"Enter number {number_count + 1}: "))
    numbers.append(number)

# identify which numbers have duplicate
# print output
