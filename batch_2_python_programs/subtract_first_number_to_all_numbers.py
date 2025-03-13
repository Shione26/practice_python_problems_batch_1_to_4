# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

# ask user for 10 imputs
# ask for the first number 
total = int(input("Enter number 1: "))

# loop to ask user for the rest of the inputs
for number_count in range(1, 10):
    number = int(input(f"Enter number {number_count + 1}: "))
    total -= number    # subtract every inputted number from the difference in each loop iteration
    
# print the result
print(total)