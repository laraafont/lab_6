# option 1 that takes password and stores it
def encode():
    # global passwords to allow use of variables in other functions
    global new_password
    global password
    new_password = ""
    password = input("Please enter your password to encode:")
    # to make sure password is 8 digits
    if len(password) > 8:
        print("Must be 8 digits!")

    # to shift all digits up by 3
    for digit in password:
        new_digit = int(digit) + 3
        new_password = new_password + str(new_digit)
    print("Your password has been encoded and stored!")
    return new_password


# option 2 to print decoded password
def decode(new_password):
    pass


# main function with menu
def main():
    while input != "3":
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        # takes in user option
        option = input("Please enter an option:")

        # encode
        if option == "1":
            encode()
        # decode
        elif option == "2":
            decode(new_password)
        # quit
        elif option == "3":
            break


if __name__ == '__main__':
    main()