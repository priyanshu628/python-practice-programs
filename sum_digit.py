def sum_of_digits(n):
    total = 0
    
    while n != 0:
        digit = n % 10   # last digit
        total += digit   # sum me add
        n = n // 10      # last digit remove
    
    return total
print(sum_of_digits(312))