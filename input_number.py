while True:
    user_input = input("Enter a number (or type 'quit' to exit): ")
    
    if user_input.lower() == "quit":
        print("Program ended")
        break
    
    n = int(user_input)
    
    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")