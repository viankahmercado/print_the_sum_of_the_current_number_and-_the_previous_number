# Assignment 5:
# Do the exercise 1-15 in https://pynative.com/python-basic-exercise-for-beginners/
# Try do challenge yourself by not checking the "solution"

# Exercise 2: 
# Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# assigned the previous number with stored value = 0
previous_number = 0

# create loop and range
for i in range(1, 11):
    sum_of_the_two_numbers = previous_number + i
    print("Current Number: ", i, "Previous_Number: ", previous_number, "Sum: ", sum_of_the_two_numbers)
# re-assigned the previous number to i
    previous_number = i