#hw.0 : მომხმარებელს შემოატანინეთ ორი რიცხვი, შემდეგ კი შეადარეთ ეს ორი რიცხვი ერთმენთს, მიღებული მნიშვნელობა შეინახეთ ცვლადში და შემდეგ დაბეჭდეთ მისი მონაცემთა ტიპი და მნიშვნელობა
num4 = int(input("enter any number: "))
num3 = int(input("enter any number again: "))

print (num4>num3)


#hw.1 :  შექმენით პროგრამა რომელსაც შეეძლება დიალოგი თქვენთან (აირჩიეთ ნებისმიერი თემა) input გამოყენებით

num = int(input("enter any number: "))
num2 = int(input("enter any number again: "))

if num > num2:
    print(num)
else:
    print(num2)


#hw.2 :აქამდე ნასწავლი მასალის გამოყენებით ივარჯიშეთ ძალიან ბევრი და მოიფიქრეთ რაიმე პროგრამა რომელსაც გააკეთებთ
print("what is your name?")
str(input())

print("what is your age?")
int(input())

print("where do you live?")
str(input())

print("what is your favorite food?")
str(input())