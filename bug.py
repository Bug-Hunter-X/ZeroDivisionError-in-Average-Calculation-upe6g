def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# This will throw an exception
my_list = []
result = calculate_average(my_list)
print(f"The average is: {result}")