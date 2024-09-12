password=input("enter password: ")
password2=input("repeat password: ")
while password:
    if password2 == password:
        print("correct")
        break
    else:
        print("error")
        password2=input("repeat password: ")


       

