username = input("enter your username:")
password = input("enter your password:")
if (username == "admin" and password == "pass"):
    print("loogin succesfully")
elif (username != "admin"):
    print("wrong username")
else:
    print("wrong password")
    