import math

def is_prime(n: int) -> bool:
    """
    Checks if a number is prime.

    Parameters:
    - n: int
        The number to check for primality.

    Returns:
    - bool:
        True if the number is prime, False otherwise.
    """

    # Handling special cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Checking divisibility by numbers up to the square root of n
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False

    return True

def generate_prime_numbers(num_digits: int) -> list:
    """
    Generates prime numbers based on the number of digits the primes have.

    Parameters:
    - num_digits: int
        The number of digits the prime numbers should have.

    Returns:
    - list:
        A list of prime numbers with the specified number of digits.
    """

    # Handling special cases
    if num_digits <= 0:
        return []

    # Calculating the range of numbers to check
    start = 10 ** (num_digits - 1)
    end = 10 ** num_digits

    # Generating prime numbers within the specified range
    primes = [n for n in range(start, end) if is_prime(n)]

    return primes

# Example usage of the generate_prime_numbers function

num_digits = 3
prime_numbers = generate_prime_numbers(num_digits)
print(f"Prime numbers with {num_digits} digits: {prime_numbers}")
