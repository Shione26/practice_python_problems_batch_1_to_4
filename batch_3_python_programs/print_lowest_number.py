# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

# create an empty list
input_numbers = []

# loop to ask user to input a number continuesly until invalid input
while True:
    user_input = input("Enter a number: ")

# check if input is invalid
    try:
        user_input = int(user_input)
        input_numbers.append(user_input)   # if yes, add the input to the list
    except ValueError:
        print("Invalid input")      # if no, break
        break

# print the lowest number using min() function
if input_numbers:
    print(min(input_numbers))

