def prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

numbers = [2, 4, 5, 6, 7, 8, 11]

primes = [n for n in numbers if prime(n)]
updated = [0 if prime(n) else n for n in numbers]

print("Original list:", numbers)
print("Prime numbers found:", primes)
print("Updated list:", updated)