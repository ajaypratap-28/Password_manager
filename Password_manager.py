
from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("key.key" , "wb") as keyfile:
    keyfile.write(key)

new_keyfile = open("key.key" , "rb")
new_keyfile1 = new_keyfile.read()

fer = Fernet(new_keyfile1)

def view():
    with open('details.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())

    

def add():
    username = input("Enter your username : ")
    password = input("Enter your password : ")

    with open("details.txt", "a") as file:
        file.write("Username :" + username + "|" + "Password :" + fer.encrypt(password.encode()).decode() + "\n")
    
if __name__ == "__main__" :

 while True:
    choice = input("What do you want to do? view/ add/ quit : ").lower()

    if choice == "quit":
        break

    if choice == "view":
        view()

    if choice == "add":
        add()

    else:
        print("You have enterd wrong choice. Please choose again")
        continue    




