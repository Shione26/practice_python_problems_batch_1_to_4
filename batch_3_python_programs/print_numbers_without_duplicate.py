# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# ask the user to input 10 numbers
numbers = []

for number_count in range(10):
    number = int(input(f"Enter number {number_count + 1}: "))
    numbers.append(number)

# identify which numbers are inputted only once
for num in numbers:
    if numbers.count(num) == 1:
        print(num)    # print the numbers with no duplicate
