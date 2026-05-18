def get_largest(a, b, c):
    if(a > b and a > c):
        return a
    elif(b > c):
        return b
    else:
        return c
print(get_largest(3,10,5))