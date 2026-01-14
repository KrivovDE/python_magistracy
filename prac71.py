def euclid_gcd(m, n):
    while n:
        m, n = n, m % n
    return m

A = int(input())
B = int(input())
C = int(input())
D = int(input())

num = A * D
den = B * C

gcd_value = euclid_gcd(num, den)

num_simplified = num // gcd_value
den_simplified = den // gcd_value

print(f"{num_simplified}/{den_simplified}")