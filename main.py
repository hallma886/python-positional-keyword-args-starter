# Matthew Hall
# November 13, 2024
# Practice: Positional & Keyword Arguments in Python


# POSITIONAL ARGUMENTS
# Start by writing the code to create the three functions outlined below
# You'll use only positional arguments in the first three functions
# Test your code and correct any errors

# Greet The User
# Write a function that takes two parameters -- first name and age
# Use an f-string to welcome the user by first name and to display his/her age
def greet(first_name, age):
    print(f'Hello, {first_name}! You are {age} years old.')

greet('Matt', 17)
greet('Ethan', 17)
print()
# Area of a Rectangle
# Write a function to calculate the area (in square feet) of a rectangle
# Your two parameters will be length and width
# The print statement in the function should display the length, width and area (in square feet) of your rectangle
def area(length, width):
    rectangle_area = length * width
    print(f'The area of a rectangle with a length of {length:.2f} and a width of {width:.2f} is {rectangle_area}')

area(46.8, 64.4)
print()
# Sum of Numbers
# Write a function that finds the sum of three numbers
# Your three parameters will be num1, num2, and num3
# The print statement in the function should display the sum of the three numbers
def sum_of_numbers(num_1, num_2, num_3):
    total_sum = num_1 + num_2 + num_3
    print(f'The sum of {num_1}, {num_2}, and {num_3} is {total_sum}')

sum_of_numbers(54, 75, 29)
print()
# KEYWORD ARGUMENTS
# Create the three functions outlined below
# In these last three functions, you'll use only keyword arguments 
# Test your code and correct any errors


# Greet By Title
# Write a function that greets the user by title, first name and last name
# Examples of titles include: Mr., Ms., Mrs. and Dr.
# When calling your function, change the order of your keyword arguments so that they don't match the order of your function parameters
def greet_by_title(title, first_name, Last_name):
    print(f'Hello {title}{first_name} {Last_name}')

greet_by_title(Last_name='Hall',first_name='Matthew', title='Mr.')
print()
# Describe Your Pet
# Write a function that says what type of pet you have and what your pet's name is
# Your function parameters will be pet_type and pet_name
def my_pet(pet_name, pet_type):
    print(f'I have a {pet_type}, and their name is {pet_name}.')

my_pet(pet_name='Roxy', pet_type='Dog')
print()
# Updated Function
# Choose any ONE of the first three functions from this project and rewrite it below using keyword arguments
def greet(first_name, age):
    print(f'Hello, {first_name}! You are {age} years old.')

greet(age=17, first_name='Matt')
greet(age=17,first_name='Ethan')
print()