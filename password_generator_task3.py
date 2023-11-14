import string as s
from random import choice
def create(n):
    password=""
    list=[]
    while(n>=4):
        list+=choice(s.ascii_lowercase)
        list+=choice(s.ascii_uppercase)
        list+=choice(s.digits)
        list+=choice(s.punctuation)
        n-=4
    for i in range(n):
        list+=choice(s.ascii_letters+s.digits+s.punctuation)
    for i in list:
        password+=i
    print(password)
    save(password)
def save(s):
    f=open("password_history.txt","a")
    f.write(s+"\n")
    f.close()
def view():
    try:
        f=open("password_history.txt","r")
        s=f.read()
        if(f.tell()==0):
            return "\nNO PASSWORDS FOUND"
        return s
    except:
        clear()
        return "\nNO PASSWORDS FOUND"
def clear():
    f=open("password_history.txt","w")
    f.write("")
    f.close()
print("PASSWORD GENERATOR")
while(True):
    x=int(input("\n1. GENERATE PASSWORD\n2. VIEW PASSWORD HISTORY\n3. CLEAR PASSWORD HISTORY\n4. EXIT\nenter your choice: "))
    if(x==1):
        print("\nGENERATE PASSWORD\n")
        n=int(input("enter number of passwords: "))
        size=int(input("enter number of characters: "))
        print("\nGENERATED SUCCESFULLY\n")
        for i in range(n):
            create(size)
    elif(x==2):
        print("\nPASSWORD HISTORY")
        print(view())
    elif(x==3):
        clear()
        print("\nPASSWORD HISTORY CLEARED")
    elif(x==4):
        print("\nTHANK YOU!!!!!")
        break
    else:
        print("\nINVALID CHOICE")
    print('-'*50)
