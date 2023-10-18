def find_smallest_multiple(n):
    multiple = 1
    factors = []

    for i in range(1, n + 1):
        if multiple % i != 0:
            for factor in factors:
                if i % factor == 0:
                    i //= factor
            multiple *= i
            factors.append(i)

    return multiple, factors

n = int(input("Enter the value of n: "))
smallest_multiple, factors = find_smallest_multiple(n)

print("Smallest multiple of the first", n, "numbers:", smallest_multiple)
print("Factors:", factors)