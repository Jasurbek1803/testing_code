def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

def generate_palindromic_numbers():
    num = 0
    while True:
        if is_palindrome(num):
            yield num
        num += 1

# Example: Generate the first 5 palindromic numbers using the generator
palindrome_generator = generate_palindromic_numbers()
for _ in range(10):
    palindromic_number = next(palindrome_generator)
    print(palindromic_number)
