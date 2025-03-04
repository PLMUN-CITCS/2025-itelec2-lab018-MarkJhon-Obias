# MARKJOHN OBIAS
# Week 05 - Working with Functions
# Laboratory # 18 - Guided Coding Exercise: Nested Functions and Reusing User-Defined Functions

def square(num):
    """Returns the square of the given number."""
    return num ** 2  # Alternative: return num * num

def sum_of_squares(numbers):
    """Returns the sum of the squares of the numbers in the list."""
    total = sum(square(n) for n in numbers)  # Using sum() with list comprehension
    return total

numbers_list = [2, 3, 4]
result = sum_of_squares(numbers_list)

print(f"The sum of squares is: {result}")
