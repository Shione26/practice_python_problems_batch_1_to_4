# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number

# create an empty list
input_numbers = []

# loop to ask user to input a number continuesly until invalid input
while True:
    user_input = input("Enter a number: ")

# check if input is valid
    try:
        user_input = int(user_input)
        input_numbers.append(user_input)   # if yes, store the input to the list
    except ValueError:
        print("Invalid input")      
        break      # if no, break

# print the highest number using max() function