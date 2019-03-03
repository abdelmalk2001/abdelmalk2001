#Db
db_username="admin"
db_password="123456"

user=input("username:")
password=input("password:")

if user==db_username and password==db_password:
    print("welcome")
else:
    print("errour")

