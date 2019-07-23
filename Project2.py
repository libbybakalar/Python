# Libby Bakalar
# 4/29/19
# This program will read in user ids and names from a file and 
# give the user the option to login in, create a new user, or
# reset their password. 

import os 
import time 
clear = lambda:os.system('cls')

dictionary = {}

def main():
    init(dictionary)

def init(dictionary):
    try:
        # opens input file 
        loginsFile = open('password.dat', 'r') 
        
        id = loginsFile.readline().strip()
        password = loginsFile.readline().strip()

        while id != "":
            dictionary[id] = password 
            id = loginsFile.readline().rstrip()
            password = loginsFile.readline().rstrip()

        menu(dictionary)

        # closes file 
        loginsFile.close()

    except:
        print("Error, program ending. ")
        time.sleep(2) # sleeps for 2 seconds so user can see message
        os._exit(0)


def menu(dictionary): # asking user what they want to do
    again = "Y"
    print("Enter 1 to sign in ")
    print("Enter 2 to create a new user ")
    print("Enter 3 reset password")
    choice = str(input("Anything else to exit \n"))
    if choice == "1" or choice == "2": 
        if choice == "1": # signing in 
            signIn(dictionary)
            time.sleep(2) # sleeps for 2 seconds 
            clear()
            menu(dictionary)
        else: # if choice = 2(create a new user)
            newUser(dictionary)
            time.sleep(2) # sleeps for 2 seconds
            clear()
            menu(dictionary)
    else:
        if choice == "3": # reseting password
            resetPass(dictionary)
            time.sleep(2) # sleeps for 2 seconds
            clear()
            menu(dictionary)
        else: # exiting
            print("You have been signed out. Have a good day! ")
            time.sleep(2) # sleeps for 2 seconds
            os._exit(0)


def signIn(dictionary): # choice = 1
    valid = True    
    id = (input("Please enter Login ID \n"))

    # ensure login id is in the password.dat file 
    if id in open('password.dat').read():
        valid = True
    else: 
        print("Username not found. \n") 
        time.sleep(2) # sleeps for 2 seconds
        clear()
        menu(dictionary)
        
    if valid == True:
        password = (input("Please enter password \n"))

    # validate password listed in the file - password.dat, for that login id
    # make sure the right password is right after if in password.dat
    if password == dictionary[id]:
        valid = True
    else: 
        valid = False
        print("Password does not match id \n")

    if valid == True:
        print("Welcome " + id  + "! \n")
        print("You have been logged in! \n")

def newUser(dictionary): # choice = 2
    func = 'new'

    id = (input("Please enter login ID \n"))
    # validate id 
    validLoginID(dictionary, id)
    
    password = (input("Please enter password \n"))      
    # validate password
    validPass(dictionary, password, id, func)

    # adds to dictionary
    dictionary[id] = password

    # opens file so its writable 
    loginsFile = open('password.dat', 'w') 

    # saves valid user id and password to password.dat file
    # store them on seperate lines
    for x, y in dictionary.items():
        loginsFile.write(x + '\n')
        loginsFile.write(y + '\n')

    print("New user ID and password have been created. \n")

def validLoginID(dictionary, 
                 id):
    alphaCtr = 0
    digitCtr = 0

    for ch in id:
        if ch.isalpha():
            alphaCtr += 1
        if ch.isdigit():
            digitCtr +=1 

    # must be 6-10 letters 
    if alphaCtr < 6 or alphaCtr > 10: 
        print("ID must have 6-10 letters \n")
        time.sleep(2) # sleeps for 2 seconds
        clear()
        newUser(dictionary)
        menu(dictionary)

    # must have 2 numbers 
    if digitCtr < 2:
        print("ID must have 2 numbers \n")
        time.sleep(2) # sleeps for 2 seconds
        clear()
        newUser(dictionary)
        menu(dictionary)

    # cannot have white spaces
    if "\n" in id or " " in id or "\t" in id:
        print("Invalid ID, cannot contain whitespaces \n")
        time.sleep(2) # sleeps for 2 seconds
        clear()
        newUser(dictionary)
        menu(dictionary)

    # cannnot be in password.dat file 
    if id in open('password.dat').read():
        print("Error, ID already taken \n")
        newUser(dictionary)
        time.sleep(2) # sleeps for 2 seconds
        clear()
        menu(dictionary)

def validPass(dictionary, password, id, func):
    upperCtr = 0
    lowerCtr = 0
    digitCtr = 0
    ok = True

    for ch in password:
        if ch.isdigit():
            digitCtr += 1 
        if ch.isupper():
            upperCtr += 1
        if ch.islower():
            lowerCtr += 1

    # length must be 6-12
    if len(password) >= 6 or len(password) <= 12:
        ok = True
    else: 
        print("Invalid Password, must be 6-12 in length \n")
        time.sleep(2) # sleeps for 2 seconds
        clear()
        if func == 'new': 
            newUser(dictionary)
            menu(dictionary)
        if func == 'reset': 
            resetPass(dictionary)
            menu(dictionary)

    # must have 1 number
    if digitCtr < 1:
        print("Invalid Password, must have 1 number \n")
        time.sleep(2) # sleeps for 2 seconds
        clear()
        if func == 'new': 
            newUser(dictionary)
            menu(dictionary)
        if func == 'reset': 
            resetPass(dictionary)
            menu(dictionary)            

    # must have upper and lower letters
    if upperCtr < 1 or lowerCtr < 1: 
        print("Invalid Password, must have an upper and lower case letter \n")
        time.sleep(2) # sleeps for 2 seconds
        clear()
        if func == 'new': 
            newUser(dictionary)
            menu(dictionary)
        if func == 'reset': 
            resetPass(dictionary)
            menu(dictionary)
            
    # cannot have white spaces
    if "\n" in password or " " in password or "\t" in password:
        print("Invalid Password, cannot contain white spaces \n")
        time.sleep(2) # sleeps for 2 seconds
        clear()
        if func == 'new': 
            newUser(dictionary)
            menu(dictionary)
        if func == 'reset': 
            resetPass(dictionary)
            menu(dictionary)

    # password cannot contain id 
    if id in password: 
        print("Invalid Password, ID cannot be in password \n")
        time.sleep(2) # sleeps for 2 seconds
        clear()
        if func == 'new': 
            newUser(dictionary)
            menu(dictionary)
        if func == 'reset': 
            resetPass(dictionary)
            menu(dictionary)
            
    # must be unique
    if password in open('password.dat').read():
        print("Error, Password already taken \n")
        time.sleep(2) # sleeps for 2 seconds
        clear()
        if func == 'new': 
            newUser(dictionary)
            menu(dictionary)
        if func == 'reset': 
            resetPass(dictionary)
            menu(dictionary)

def resetPass(dictionary): # choice = 3
    func = 'reset'

    id = (input("Please enter ID \n"))

    if id not in open('password.dat').read():
        print("User ID not found ")
        resetPass(dictionary)
        menu(dictionary)

    # validate password
    password = (input("Please enter password \n"))
    validPass(dictionary, password, id, func)

    # replace the existing password with the new value 
    dictionary[id] = password

    # opens file so its writable 
    loginsFile = open('password.dat', 'w')

    # writing out to file
    for x, y in dictionary.items():
        loginsFile.write(x + '\n')
        loginsFile.write(y + '\n')

    print("Password has been reset. \n")
    time.sleep(2) # sleeps for 2 seconds

# calls main
main()