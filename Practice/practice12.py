correct_username = "udoy"
correct_password = "python123"

attempts = 0

while attempts < 3:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username:
        if password == correct_password:
            print("Login Successful!")
            break
        else:
            print("Wrong Password!")
    else:
        print("Wrong Username!")

    attempts += 1

if attempts == 3:
    print("Account Locked!")