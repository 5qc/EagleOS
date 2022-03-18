# Import Modules
import json, os, time, random
from eagleos import *

# Setup Console
os.system("color f0")
os.system("cls")

# Main Code
def main():
    actionSetup = 1
    os.system("cls")
    print("Welcome to EagleOS! What would you like to do on this beautiful American day?")
    
    while actionSetup == 1:
        action = input("")
        
        if action.startswith("run"):
            if action == "run" or action == "run ":
                file = input("Which file do you want to run? ")

                if "." in file:
                    fileExt = file.split(".")[1]
                    if fileExt != "imp":
                        error(error.preset("notsupported"))
                    else:
                        convert(file)
                else:
                    convert(f"{file}.imp")
            else:
                file = action.split(" ")[1]
                
                if "." in file:
                    fileExt = file.split(".")[1]
                    if fileExt != "imp":
                        error(error.preset("notsupported"))
                    else:
                        convert(file)
                else:
                    convert(f"{file}.imp")
        elif action == "happy-birthday":
            name = input("Please input your so-desired name: ")
            print(f"Happy birthday to you!")
            time.sleep(4)
            print(f"Happy birthday to you!")
            time.sleep(4)
            print(f"Happy birthday, dear {name}!")
            time.sleep(4)
            print(f"Happy birthday to you!")
        elif action.startswith("name"):
            def getNames(gender):
                names = open(f"./eagleos/data/{gender}-names.txt")
                names = names.read()
                names = names.split("\n")
                print(random.choice(names))

            if action == "name" or action == "name ":
                gender = input("Please choose a gender: ")

                if gender == "male":
                    getNames("male")
                elif gender == "female":
                    getNames("female")
                else:
                    error("Invalid gender.")
            else:
                gender = action.split(" ")[1]

                if gender == "male":
                    getNames("male")
                elif gender == "female":
                    getNames("female")
                else:
                    error("Invalid gender.")
        elif action == "clear":
            os.system("cls")
        else:
            error(error.preset("invalidcmd"))


# Load Users
def login():
    users = open("users.json")
    users = json.load(users)

    loginPass = 1
    while loginPass == 1:
        inputUserName = input("Username: ")
        for user in users:
            username = user[0]
            if inputUserName != username:
                os.system("cls")
                error("Invalid username.")
                login()
                break
            else:
                break
        
        inputUserPass = input("Password: ")
        for user in users:
            userpass = user[1]

            if inputUserPass != userpass:
                os.system("cls")
                error("Invalid password.")
                break
            else:
                main()
login()
