import re
def phone_number(number):
     result=re.fullmatch(r'(\+91)?\s?[6-9][0-9]{9}$',number)
     if result:
         return f'{number} is Valid'
     return f"{number} is Invalid"
     
def username(name):
     result=re.fullmatch('^[a-z][a-z0-9._]{7,30}$',name)
     if result:
         return f'{name} is Valid'
     return f'{name} is Invalid'



def emails(email):
    result=re.fullmatch(r'^[a-z0-9][a-z0-9.]+@[a-z0-9]+\.[a-z]{2,4}$',email)
    if result:
        return f'{email} is Valid'
    return f'{email} is Invalid'




def pan(pan_number):
    result=re.fullmatch('^[A-Z]{5}[0-9]{4}[A-Z]$',pan_number)
    if result:
        return f"{pan_number} Is Valid"
    return f"{pan_number} is Invalid"



def Vehicle(vehicle_number):
    result=re.fullmatch('^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$',vehicle_number)
    if result:
        return f"{vehicle_number} is Valid"
    return f'{vehicle_number} is Invalid'



def passport(passport_number):
    result=re.fullmatch('^[A-Z]{1}[0-9]{9}$',passport_number)
    if result:
        return f'{passport_number} Is Valid'
    return f'{passport_number} Is Invalid'



def aadhaar(number):
    result=re.fullmatch(r'[0-9]{12}|[0-9]{4}\s[0-9]{4}\s[0-9]{4}',number)
    if result:
        return f'{number} Is Valid'
    return f"{number} Is Invalid"

def voter(voter_id):
    result=re.fullmatch('^[A-Z]{3}[0-9]{7}$',voter_id)
    if result:
        return f"{voter_id} Is Valid"
    return f"{voter_id} Is Invalid"




if __name__=="__main__":
    print("""
Welcome to the Validation Application.

This application validates different types of user information using Regular Expressions (Regex), including:

• Phone Number
• Username
• Email Address
• PAN Card Number
• Vehicle Registration Number
• Passport Number
• Aadhaar Number
• Voter ID Number

Select an option from the menu to validate your input.
""")
    
    while True:
        print("1Phone Number\n 2.Username \n 3.Email Address \n 4.PAN Card Number \n 5.Vehicle Registration Number \n 6.Passport Number \n 7.Aadhaar Number \n 8.Voter ID Number \n 9.Exit")
        try:
            choice=int(input("Enter your choice Here:-> "))
        except ValueError:
            print("Choose only integers")
            continue
        if choice==1:
            number=input("Enter the number:->")
            print(phone_number(number))
        elif choice==2:
            name=input("Enter the username:->")
            print(username(name))
        elif choice==3:
            email=input("Enter Your Email:->")
            print(emails(email))
        elif choice==4:
            pan_number=input("Enter your pan number:->")
            print(pan(pan_number))
        elif choice==5:
            vehicle_number=input("Enter the Vechile Number:->")
            print(Vehicle(vehicle_number))
        elif choice==6:
            passport_number=input("Enter the passport number:->")
            print(passport(passport_number))
        elif choice==7:
            number=input("Enter Your Aadhar Number:->")
            print(aadhaar(number))
        elif choice==8:
            voter_id=input("Enter Your voter ID:->")
            print(voter(voter_id))
        elif choice==9:
            print("THANK YOU")
            exit()
        else:
            print("Invalid choice")
        