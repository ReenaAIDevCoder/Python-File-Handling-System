from pathlib import Path
import os

def readfileandfolder():
    path =Path('')
    items = list(path.rglob('*'))

    for i, items in enumerate(items):
        print(f"{i+1} : {items}")


# Created the file handling function for creating a file and reading a file.

def createfile():
    try:
        readfileandfolder()
        name = input("Enter the name of the file you want to create:- ")
        p = Path(name)

        if not p.exists():
            with open(p,'w') as fs:
                data = input("Enter the content of the file:- ")
                fs.write(data)


            print(f"FILE CREATED SUCCESSFULLY WITH NAME {name}")

        else:
            print("This file already exist")

    except Exception as err:
        print(f"An error occurred as:{err}")

# Reading the file handling function for reading a file and displaying the content of the file.

def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read:- ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("Readed successfully.")

        else:
            print("This file does not exist")

    except Exception as err:
        print(f"An error occurred as:{err}")


# Updating the file handling function for updating a file and displaying the content of the file.

def updatefile():
    try:
        readfileandfolder()
        name = input("Which file you want to update:- ")
        p = Path(name)

        if p.exists() and p.is_file():
            print("Press 1 for changing the file-name.")
            print("Press 2 for reading the file.")
            print("Press 3 for creating a new file.")
            print("Press 4 for overwriting the data in your file.")
            print("Press 5 for appending to the file.")

            choice = int(input("Enter your choice:- "))
            if choice == 1:
                name2 = input("Enter the new name of the file:- ")
                p2 = Path(name2)
                p.rename(p2)    
                print(f"FILE RENAMED SUCCESSFULLY FROM {name} TO {name2}")


            elif choice == 2:
                with open(p,'r') as fs:
                    data = fs.read()
                    print(data)
                print("FILE READ SUCCESSFULLY.")

            elif choice == 3:
                name2 = input("Enter the name of the new file:- ")
                p2 = Path(name2)

                if not p2.exists():
                    with open(p2,'w') as fs:
                        data = input("Enter the content of the new file:- ")
                        fs.write(data)
                    print(f"NEW FILE CREATED SUCCESSFULLY WITH NAME {name2}")  
                else:
                    print("This file already exist")

            elif choice == 4:
                with open(p,'w') as fs:
                    data = input("Enter the content of the file:- ")
                    fs.write(data)
                print(f"FILE OVERWRITTEN SUCCESSFULLY WITH NAME {name}")

            elif choice == 5:
                with open(p,'a') as fs:
                    data = input("Tell what you want to append in the file:- ")
                    fs.write("" +data)

                print(f"DATA APPENDED SUCCESSFULLY TO THE FILE WITH NAME {name}")

            else:
                print("Invalid choice.")


            print(f"FILE UPDATED SUCCESSFULLY WITH NAME {name}")

        else:
            print("This file does not exist")

    except Exception as err:
        print(f"An error occurred as:{err}")



# Deleting the file handling function for deleting a file and displaying the content of the file.

def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to delete:- ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)
            print(f"FILE DELETED SUCCESSFULLY WITH NAME {name}")

        else:
            print("This file does not exist")

    except Exception as err:
        print(f"An error occurred as:{err}")



print("press 1 for creating a file.")
print("press 2 for reading a file.")
print("press 3 for updating a file.")
print("press 4 for deleting a file.")


check = int(input("Enter your choice:- "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()