# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# ask the user to input 10 numbers


for number_count in range(10):
    number = int(input(f"Enter number {number_count + 1}: "))

# identify which numbers are inputted only once
# print the numbers with no duplicate