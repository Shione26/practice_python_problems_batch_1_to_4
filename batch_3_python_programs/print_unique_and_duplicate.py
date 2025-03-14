# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

# create an empty set 
input_numbers = set()

# loop to ask user to input a number continuesly until invalid input
while True:
    user_input = (input("Enter a number: "))

    # check if input is valid
    try:
        user_input = int(user_input)
    except ValueError:                # if no, break
        print("Input is invalid")
        break
        
    # if yes, check if input already exists in the set
    if user_input in input_numbers:
        print("Duplicate")      # if Yes, print "Duplicate"
    else:
        print("Unique")         # if No, print "Unique" 
        input_numbers.add(user_input)    # then add the input to the set
        