import pytest
from first_task_generator import fibonacci_generator
from second_task_generator import generate_palindromic_numbers
from third_task_generator import generate_prime_numbers
from fourth_task_generator import custom_range

def test_generator_values():
    gen = fibonacci_generator(5)
    
    assert next(gen) == 0
    assert next(gen) == 1
    assert next(gen) == 1
    assert next(gen) == 2
    assert next(gen) == 3

    with pytest.raises(StopIteration):
        next(gen)


def test_palindrome_numbers():
    gen = generate_palindromic_numbers()
    assert next(gen) == 0
    assert next(gen) == 1
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 4
    assert next(gen) == 5
    assert next(gen) == 6
    assert next(gen) == 7
    

def test_primes():
    gen = generate_prime_numbers()
    assert next(gen) == 2
    assert next(gen) == 3
    assert next(gen) == 5
    assert next(gen) == 7
    assert next(gen) == 11
    assert next(gen) == 13
    assert next(gen) == 17
    assert next(gen) == 19

def test_range():
    gen = custom_range(10,15)
    assert next(gen) == 10
    assert next(gen) == 11
    assert next(gen) == 12
    assert next(gen) == 13
    assert next(gen) == 14
    assert next(gen) == 15
