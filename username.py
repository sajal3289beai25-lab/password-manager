login=input("Enter login or sign up: ")
if login.lower()=="sign up":
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    with open("file.txt","a") as file:
     file.write(username+":"+password +"\n")
    print("succesfull")
elif login.lower()=="login":
   username=input("enter your username:")
   password=input("enter your password:")
   with open("file.txt","r") as file:
      for line in file:
         username1,password1=line.strip().split(":")
         if username1==username and password1==password:
            print("login successfull")
         else:
            print("incorrect username or password")
            #1234
else:
    print("invalid option")   