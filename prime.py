def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def filter_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes

# Example
print(filter_primes([7, 9, 3, 9, 10, 11, 27]))  # ➞ [7, 3, 11]
