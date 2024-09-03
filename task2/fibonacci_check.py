def is_fibonacci_number(num):
    a, b = 0, 1
    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    return False

number = 34
if is_fibonacci_number(number):
    print(f"{number} belongs to the Fibonacci sequence.")
else:
    print(f"{number} does not belong to the Fibonacci sequence.")