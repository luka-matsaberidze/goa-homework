#შექმენით ბანკის სისტემა სადაც იქნება ძალიან ბევრი პირობები და გამოიყენებთ if, elif და else -ს, გამოიყენებთ ასევე განვლილ მასალასაც


import random
import time


def deposit(): 
    print("*************************")
    raodenoba = float(input("enter your deposit: "))
    print("*************************")

    if raodenoba <0:
        print("Insufficient deposit")
        return 0


    else:
        return raodenoba




def show_balance():
   print(f"YOUR BALANC IS {balance:.2f} LARI ")







def deposit_to_someone():
   print("*************************")
   deposit_someone1 = (input("first enter Name of the transferee: "))
   print("*************************")
   deposit_someone2 = (input("second enter lastName of the transferee: "))
   print("*************************")
   deposit_someone3 = (input("enter your transferee credit card number: "))
   if len(deposit_someone3) >16:
    print("its incorect!")
    return deposit_to_someone()
   elif len(deposit_someone3) <16:
    print("its incorrect! ")
    return deposit_to_someone()
   elif len(deposit_someone3) == 16:
    print("its correct")
    
   print("*************************")
   deposit_someone4= float(input("enter your deposit: "))
   if deposit_someone4 <=0:
      print("not enough money")
      return
   elif balance < deposit_someone4:
      print("you dont have enogh money for deposit to someone please try again later")
      return deposit_to_someone()
   print("*************************")
   sure= print("are you sure?")
   sure1=print("yes")
   sure2=print("no")
   sure3=input("write word: ")
   
   
   if sure3 == "yes":
      print("okey deposit is secsit!")
      
    
      
    
    
    


   elif sure3 == "no":
      print("DEPOSIT IS DICLAIND!")
      
      

b = random.randint(1000000000000000,9999999999999999)
   

def creat_credit_card():
    print("*****************************")
    name = str(input("first enter your name: "))
    if name == float or int:
       print("invalid")
    print("*****************************")
    lastname = str(input("second enter your lastName: "))
    print("*****************************")
    age = int(input("enter your age: "))
    if age<8 and age>=0:
       print("you are not enough age to have card")
       return proces
    elif age< 18 and age >=8:
       print("you are schoole boy :D")
       print("*****************************")
       gmail = input("enter your email: ")
       print("*****************************")
       print("do you want a schoolcard?: ")
       print("yes")
       print("no")
       creat_card =( input("enter your word: "))
       time.sleep(2)
       if   creat_card == "yes":
            print(name + " " + lastname + " you have schoolcard there is your card number: "+str(b) )
            return proces
       elif creat_card == "no":
        print("okey than bye <3")
        return proces
    
      

    
    else:
       print("you are adoult")
    print("*****************************")
    gmail = input("enter your email: ")
    print("*****************************")
    print("which card do you want?")
    creat_card= input("paypal, mastercard or visa: ")
    if creat_card == "visa":
        time.sleep(2)
        print(name + " " + lastname + " you have visa card there is your card number: "+str(b) )
    elif creat_card =="mastercard":
        print(name + " " + lastname + "  you have mastercard card there is your card number: "+str(b))
    elif creat_card == "paypal":
        print(name + " " + lastname + " you have paypal card there is your card number: "+str(b))


    
        
    
    
    














     
    




balance = 0
proces = True

while proces:
    print("*************************")
    print("Hello to GOA bank:3")
    print("*************************")
    print("BANK PROGRAM")
    print("*************************")
    print("1.deposit")
    print("2.deposit to someone")
    print("3.show balance")
    print("4.creat credit card")
    print("5.exsit")
    print("*************************")

    

    choose = input("please enter your choose: ")

    if choose =="1":
        balance += deposit()
    elif choose =="2":
        deposit_to_someone()
    elif choose == "3":
        show_balance()
    elif choose =="4":
        creat_credit_card()
    elif choose =="5":
        proces = False
        
        print("thank you have nice day :3")
        
    else:
        
        print("there not is that choose") 