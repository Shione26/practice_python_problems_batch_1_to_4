# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

# create an empty list
input_numbers = []

# loop to ask user to input a number continuesly until invalid input
while True:
    user_input = (input("Enter a number: "))

# check if input is valid
    try:
        user_input = int(user_input)
        input_numbers.append(user_input)    # if yes, store input to the list
    except ValueError:               
        print("Input is invalid")           # if no, break
        break

# sort numbers from lowest to highest using sort() function
input_numbers.sort() 
# print output
print(input_numbers)
