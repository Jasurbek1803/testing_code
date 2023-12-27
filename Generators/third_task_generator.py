def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime_numbers():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

prime_generator = generate_prime_numbers()
for _ in range(10):
    prime_number = next(prime_generator)
    print(prime_number)
