numbers = [42, 17, 8, 99, 23, -5, 0]
smallest = min(numbers)

print(f"The smallest number is: {smallest}")

# Handles empty list by raising ValueError
try:
    empty_list = []
    min(empty_list)
except ValueError as e:
    print(f"Calling min() on an empty list raised an error: {e}")