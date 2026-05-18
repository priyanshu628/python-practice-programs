#take input as a string
num_str = input("Enter a number as a string: ")
#convert to diffrent type 
num_int = int(num_str)
num_float = float(num_str)
num_str = str(num_str)

#print result 
print("integer", num_int, "type:", type(num_int))
print("float", num_float, "type", type(num_float))
print("str", num_str, "type", type(num_str))