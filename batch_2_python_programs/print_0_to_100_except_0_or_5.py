# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

# print 0-100

for number in range(0, 101):
    if number % 5 != 0:
        print(number)
# check condition if ending zero or 5
# print output