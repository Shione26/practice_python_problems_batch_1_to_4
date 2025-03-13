# Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.

# print 0-100

for number in range(1, 101):
    if number % 10 != 0:       # check condition if number is ending in zero
        print (number)         # print output


