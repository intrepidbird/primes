/**
 * Generates prime numbers up to a given limit.
 *
 * @param limit - The upper limit up to which prime numbers should be generated.
 *
 * @returns {number[]} - An array of prime numbers up to the given limit.
 */
function generatePrimeNumbers(limit: number): number[] {
    const primes: number[] = [];

    // Check if a number is prime
    function isPrime(num: number): boolean {
        if (num <= 1) {
            return false;
        }

        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) {
                return false;
            }
        }

        return true;
    }

    // Generate prime numbers
    for (let i = 2; i <= limit; i++) {
        if (isPrime(i)) {
            primes.push(i);
        }
    }

    return primes;
}

// Usage example
const limit = 20;
const primes = generatePrimeNumbers(limit);
console.log(`Prime numbers up to ${limit}: ${primes.join(", ")}`);
