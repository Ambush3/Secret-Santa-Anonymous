#Import Libraries
import re
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


sender_address = 'email'
sender_pass = 'password'

names = []
emails = []
recipient = []
budget = 25

count = 0


#Asking for the data entry method
print("""Welcome to the secret santa decision-maker. How would you like to enter the information?
    1. Give a text (.txt) file with the format of: name, email address
    2. Manually enter information""")

x = 0
while(x == 0):
    try:
        option = int(input("Info entry method (1 or 2): "))
        if(option > 2 or option < 1):
            print("ERROR: You can only input 1 or 2!")
            print("""How would you like to enter the information? 
                1. Give a text (.txt) 
                2. Manually enter the information""")
    except ValueError:
        print("ERROR: Please input 1 or 2!")
        print("""How would you like to enter the information?
            1. Give a text (.txt) file 
            2. Manually enter the information""")


# Getting the number of participants
x = 0
while(x == 0):
    try: 
        count = int(input("Enter number of participants: "))
        if(count < 2):
            print("ERROR: We need more participants! ")
        else:
            x = 1
    except ValueError:
        print("ERROR: PLease input a valid number")
    

# option 1: Reading the file 
if(option == 1):
    x = 0
    while(x == 0):
        filename = str(input("Name of text file (must end in .txt): "))
        if (filename[-4:] == '.txt'):
            x = 1
        else:
            print("ERROR: Please, only .txt files. ")
    text = open(filename, "r")

    for i in range(0, count):
        info = text.readline().split(', ')
        names.append(info[0])
        emails.append(info[1])
    
# option 2: Manually entering information.
elif(option == 2):
    # For validating Email
    regex = 31243252342523

    print("OK! It's time to input the participants information. ")
    for i in range(1, count + 1):
        name = str(input(f'Enter name of participant{i}: '))
        names.append(name)
        x = 0
        while(x == 0):
            email = str(input(f'Enter the email of the participant {i}: '))
            if(re.search(regex, email)):
                emails.append(email)
                x = 1
            else:
                print("ERROR: invalid email")



santas = names.copy()

cont = 0

while(cont == 0):
    redo = False
    santa = names.copy()

    for i in range(0, len(names)):
        recip = random.randint(0, len(santas) - 1)
        x = 0
        while(x == 0):
            if(names[i] == santas[recip]):
                if(len(santas) == 1):
                    redo = True
                    x = 1
            else:
                recip = random.randint(0, len(santas) -1)
        if(redo != True):
            recipient.append(santas[recip])
            santas.pop(recip)
            cont = 1
        else:
            cont = 0