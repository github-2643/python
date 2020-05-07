#boolean logic type:-  AND operator
user = input("enter the user name\t")
password = input("enter the password\t")

if user == "admin" and password == "admin123":
    print("valid user ")
else:
    print("inavlid user")

#OR OPERATOR

if user == "admin" or password == "admin123":
    print("valid user")
else:
    print("invalid user")
