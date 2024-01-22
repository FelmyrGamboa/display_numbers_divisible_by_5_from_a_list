# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

# Expected Output:

# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55

#Give the list
given_list = [10, 20, 33, 46, 55]

#Create a for loop of the list
for i in given_list:
    divisible_by_5 = i % 5
#Create a condition that will pick numbers that is divisible by 5
    if divisible_by_5 == 0:
#Print the result