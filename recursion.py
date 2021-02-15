# Write a function fib, that finds the nth fibonacci number

def fib(n):
    assert n >= 0 and int(n) == n, "n must be a positive integer"
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print("The 4th fibonacci number is: ", fib(4))  # 2
print("The 10th fibonacci number is: ", fib(10))  # 34


# Write a recursive function to find the sum all the digits in a positive number n
# For example: the number 223 shoudl return 7

def sum_digits(n):
    # Constraint
    assert n >= 0 and int(n) == n, "n must be a positive int"
    # Base case
    if n < 10:
        return n
    else:
        # recursion case
        return n % 10 + sum_digits(int(n/10))


print("The sum of digits in the number 100 is: ", sum_digits(100))  # 1
print("The sum of digits in the number 112 is: ", sum_digits(11234))  # 11
print("The sum of digits in the number 23 is: ", sum_digits(23))  # 5

# Write recursive function that finds the Greates Common Denominator using Euclidean Algorithm (https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm)


def gcd(n1, n2):
    assert int(n1) == n1 and int(n2) == n2, 'numbers must be integers'
    a = max(n1, n2)
    b = min(n1, n2)
    if a < 0:
        a = a*-1
    if b < 0:
        b = b*-1
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


print("The GCD for 8 and 12 is: ", gcd(8, 12))
print("The GCD for 10 and 85 is: ", gcd(20, 85))
print("The GCD for 48 and 18 is: ", gcd(48, 18))

# Write a function that uses recursion to find the binary representation of a number


def binary(n):
    if n == 0:
        return ""
    else:
        return binary(int(n/2)) + str(n % 2)


print("The binary representation of 10 is: ", binary(10))  # 1010
print("The binary representation of 13 is: ", binary(13))  # 1101


def binary2(n):
    if int(n/2) == 0:
        return n % 2
    else:
        return n % 2 + 10*binary2(int(n/2))


print("Using binary2: The binary representation of 10 is: ", binary2(10))  # 1010
print("Using binary2: The binary representation of 13 is: ", binary2(13))  # 1101

# Write a recursive function called power that returns the base raised to the exponent

# 2, 4 : 2 * power(2, 3)
# 2 * power(2, 2)
# 2 * power(2, 1)
#2* power(2, 0)
# 1


def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)


print("3 raised to the power of 0 is : ", power(3, 0))  # 1
print("2 raised to the power of 2 is : ", power(2, 2))  # 4
print("5 raised to the power of 4 is : ", power(2, 4))  # 625
