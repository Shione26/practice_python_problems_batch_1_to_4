# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

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

# get their sum then divide to the length of the input
average = sum(input_numbers) / len(input_numbers)
# print output
print(average)