import random

def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Parameters:
    - n: int
        The number to be checked.

    Returns:
    - bool:
        True if the number is prime, False otherwise.
    """

    # 1 and negative numbers are not prime
    if n <= 1:
        return False

    # Check for divisibility from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def generate_random_prime() -> int:
    """
    Generate a random prime number.

    Returns:
    - int:
        A random prime number.
    """

    # Generate a random number
    num = random.randint(2, 1000)

    # Keep generating until a prime number is found
    while not is_prime(num):
        num = random.randint(2, 1000)

    return num

# Example usage:
random_prime = generate_random_prime()
print(f"A random prime number: {random_prime}")
