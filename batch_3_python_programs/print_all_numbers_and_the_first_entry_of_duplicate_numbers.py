# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# ask user to input 10 numbers

numbers = []

for number_count in range(10):
    number = int(input(f"Enter number {number_count +1}: "))
    numbers.append(number)

duplicated_num = set(numbers)
print(duplicated_num)