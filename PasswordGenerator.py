import random #imports pseudo-random function random.choice()

length_satisfied = False

number = list(range(0,10)) #creates 0,1,2,...,9 list

def lowercaseAlphabets(): #creates lowercase_alphabet list
    lowercase_alphabet = []
    for c in range(97, 123):
        lowercase_alphabet.append(chr(c))
    return lowercase_alphabet

def uppercaseAlphabets(): #creates uppercase_alphabet list
    uppercase_alphabet = []
    for c in range(65, 90):
        uppercase_alphabet.append(chr(c))
    return uppercase_alphabet

all_options = uppercaseAlphabets() + lowercaseAlphabets() + number #list of 0-9 and all lower and uppercase letters

def check_lower(password): #ensures password has a lowercase letter
    if any(character in password for character in lowercaseAlphabets()):
        return True
    else:
        return False

def check_upper(password): #ensures password has an uppercase letter
    if any(character in password for character in uppercaseAlphabets()):
        return True
    else:
        return False

def check_number(password): #ensures password has a number
    if any(character in password for character in number):
        return True
    else:
        return False

def check_security(password): #ensures a lower, upper and number are present in our password
    if check_lower(password) == True and check_upper(password) == True and check_number(password) == True:
        return True
    else:
        return False

def password_generator(characters): #generates passwords until criteria is matched
    password = []
    while len(password) < characters:
        password.append(random.choice(all_options))
        print(*password, sep='')  # this prints the password without commas, brackets, quotes.
        if len(password) == characters:
            if check_security(password) is True:
                print("Your randomly generated password is ", end = '') #prints password on same line
                print(*password, sep='') #prints password without brackets/commas
            else:
                print("Password must contain at least one lowercase, one uppercase and one number.  Trying again.")
                password.clear()
        else:
            continue

while length_satisfied is False:
    try:
        password_length = int(input("Let's generate a secure and random password for you.\n"
                                "How many characters would you like your password to be? (Must be at least 3):  "))
        if password_length > 2:
            password_generator(password_length)
            length_satisfied = True
        else:
            print("Password must be at least 3 characters long.  Please try again.\n")
    except ValueError:
        print("You can only enter integers here.")
