username = input("enter a : username")
password = input("enter a password: ")
if (username == "admin" and password == "pass"):
    print("loggin")
else:
    if (username != "admin"):
        print("wrong username")
    else:
        print("wrong password")

