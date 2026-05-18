def print_digits(n):
    if n == 0:
        print(0)
        return
    
    while n != 0:
        digit = n % 10   # last digit nikalna
        print(digit)
        n = n // 10      # last digit remove karna
print_digits(312)
