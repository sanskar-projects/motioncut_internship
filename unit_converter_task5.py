def temp():
    print("\nTEMPERATURE CONVERTER")
    o=chr(176)
    while(True):
        x=int(input("\n1. Celsius\n2. Fahrenheit\n3. Main Menu\n"))
        if(x==3):
            break
        value=float(input("\nenter value: "))
        if(x==1):
            y=(value*(9/5))+32
            print(value,o,"Celsius = ",y,o,"Fahrenheit")
        elif(x==2):
            y=(value-32)*(5/9)
            print(value,o,"Fahrenheit = ",y,o,"Celsius")
        else:
            print("\nINVALID CHOICE")
        print("-"*50)
    return 0
def length():
    print("\nLENGTH CONVERTER")
    while(True):
        x=int(input("\n1. Meters\n 2. Feet\n3. Main Menu\n"))
        if(x==3):
            break
        value=float(input("\nenter value: "))
        if(x==1):
            y=value*3.281
            print(value,"Meters = ",y,"Feet")
        elif(x==2):
            y=value/3.281
            print(value,"Feet = ",y,"Meters")
        else:
            print("\nINVALID CHOICE")
        print("-"*50)
    return 0
def weight():
    print("\nWEIGHT CONVERTER")
    while(True):
        x=int(input("\n1. Kilograms\n2. Pounds\n3. Main Menu\n"))
        if(x==3):
            break
        value=int(input("\nenter value: "))
        if(x==1):
            y=2.205*value
            print(value,"Kilograms = ",y,"Pounds")
        elif(x==2):
            y=value/2.205
            print(value,"Pounds = ",y,"Kilograms")
        else:
            print("\nINVALID CHOICE")
        print("-"*50)
    return 0
print("UNIT CONVERTER")
while(True):
    X=int(input("\nMAIN MENU\n1. TEMPERATURE CONVERTER\n2. LENGTH CONVERTER\n3. WEIGHT CONVERTER\n4. EXIT\n"))
    if(X==1):
        temp()
    elif(X==2):
        length()
    elif(X==3):
        weight()
    elif(X==4):
        break
    else:
        print("\nINVALID CHOICE")
    print("-"*50)
print("\nTHANK YOU!!!!!")
