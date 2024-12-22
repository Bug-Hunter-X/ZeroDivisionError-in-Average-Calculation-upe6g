def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list)  # This now handles the empty list correctly
print(f"The average is: {result}")

my_list = [10, 20, 30]
result = calculate_average(my_list)
print(f"The average is: {result}") 