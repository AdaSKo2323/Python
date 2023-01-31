# Please write a program which keeps asking the user for a PIN code until they type in the correct one, which is 4321.
# The program should then print out the number of times the user tried different codes.

attempts = 0

while True:
    code = input("PIN: ")
    attempts += 1

    if code == '4321':
        if attempts == 1:
            print('Correct! It only took you one single attempt!')
            break
        print(f'Correct! It took you {attempts} attempts')
        break

    print("Wrong")




