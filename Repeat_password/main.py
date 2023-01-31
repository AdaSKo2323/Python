# Please write a program which asks the user for a password.
# The program should then ask the user to type in the password again.
# If the user types in something else than the first password,
# the program should keep on asking until the user types the first password again correctly.

password_1 = input('Password: ')
while True:
    password_2 = input('Repeat password: ')
    if password_1 != password_2:
        print('They do not match!')
    else:
        print('User account created!')
        break



