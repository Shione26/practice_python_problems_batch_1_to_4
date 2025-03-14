# Prog02: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

# create an empty list
input_numbers = []

# loop to ask user to input a number continuesly until invalid input
while True:
    user_input = input("Enter a number: ")
    
# check if input is valid
    try:
        user_input = int(user_input)  
        input_numbers.append(user_input)  # if yes, store input to the list
    except ValueError:
        print("Invalid input")
        break    # if no, break

# find which has the most number of duplicates
most_duplicate = None
highest_count = 0

for num in input_numbers:
    count = input_numbers.count(num)  # Count how many times num appears
    if count > highest_count:   # Update most frequent number
        highest_count = count
        most_duplicate = num

# print output
print(most_duplicate)
