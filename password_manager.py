

master_pwd = input("What is the master password? ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            date = line.rstrip()
            user, passw = date.split("|")
            print("User:", user, "| Password:", passw)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to (Add) add a new password or (View) view existing ones? (Press q to quit) ").lower()
    if mode == "q":
        break
    if mode == "View":
        view()
    elif mode == "Add":
        add()
    else:
        print("Invalid mode.")
        continue