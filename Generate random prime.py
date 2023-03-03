import random

def is_prime(n, k=5):
    """Test if a number is prime using the Miller-Rabin primality test."""
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n == p:
            return True
        if n % p == 0:
            return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_random_prime(digits):
    """Generate a random prime number with the given number of digits."""
    while True:
        n = random.randrange(10**(digits-1), 10**digits)
        if is_prime(n):
            return n
			
# Generate a random prime number with 50 digits
p = generate_random_prime(50)
print(p)

# Generate a random prime number with 100 digits
p = generate_random_prime(100)
print(p)