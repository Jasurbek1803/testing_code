def custom_range(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

# Example: Use the custom_range generator function
for num in custom_range(1, 20):
    print(num)
