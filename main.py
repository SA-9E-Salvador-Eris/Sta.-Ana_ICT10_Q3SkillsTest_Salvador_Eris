# Skills Test 3rd Quarter
import random
from pyscript import display, document

#passwords the door will choose for you
preset_passwords = [
    "GoGreenGiants@1423412",
    "JibaroisABadGuy@124150555",
    "YURIII@123124322"
]


def new_password(e):
    e.preventDefault()  # prevent form submission
    doors(e)       # open door selection

def keep_password(e):
    e.preventDefault()
    document.getElementById("passoffer").innerHTML = ""
    display("You chose to keep your current password.", target="output")

#for the doors
def doors(e):
    door_div = document.getElementById("doorchoice")
    door_div.innerHTML = ""

    # shuffles the door
    door_numbers = [1, 2]
    random.shuffle(door_numbers)

    # randomly changes doors
    truth_door = random.choice(door_numbers)
    door_div.setAttribute("data-truth", str(truth_door))

    for door in door_numbers:
        door_div.innerHTML += f"""
        <img py-click="door_click" data-door="{door}"
             src="door.png"
             style="width:150px; height:auto; cursor:pointer;">
        """

    display("One of these doors tells the truth, the other only lies. Make sure to choose the right one.", target="output")


def door_click(e):
    clicked_door = int(e.target.getAttribute("data-door"))
    door_div = document.getElementById("doorchoice")
    truth_door = int(document.getElementById("doorchoice").getAttribute("data-truth"))

    if clicked_door == truth_door:
        new_pw = random.choice(preset_passwords)
        document.getElementById("pword").value = new_pw
        display(f"Here is your new password: {new_pw}", target="output")
    else:
        display(f"I am sorry, for I am the one that tells lies.", target="output")

    door_div.innerHTML = ""
    document.getElementById("passoffer").innerHTML = ""


def username_verification(e):
    document.getElementById('output').innerHTML = ' '

    username = document.getElementById('uname').value.lower()
    username_length = len(username)
    #now you need numbers
    digit = sum(char.isdigit() for char in username)

    if username_length < 7:
        display(f'Your username is too short. Add at least {7 - username_length} more character/s to proceed.', target='output')
        return False

    elif digit < 3:
        display(f'Your username needs at least 3 numbers. Just add {3 - digit} more numbers.', target='output')
        return False

    elif "123" in username or "chuck" in username or "67" in username or "69" in username:
        display('This username is taken. Choose a new one. This username may contain 67, 69, or 123.', target='output')
        return False

    #extra bit for some more rules
    elif 'jibaro' in username:
        display('I do not like that guy. Change your username.', target='output')
        return False

    else:
        return True


def password_verification(e):
    document.getElementById('output').innerHTML = ''

    password = document.getElementById('pword').value
    password_length = len(password)
    password_has_number = any(char.isdigit() for char in password)
    password_has_letter = any(char.isalpha() for char in password)

    if password_length < 10:
        display(f'Your password is too short. Add at least {10 - password_length} more character/s to proceed.', target='output')
        return False

    elif not password_has_letter:
        display('Password must contain at least one letter.', target='output')
        return False

    elif not password_has_number:
        display('Password must contain at least one number.', target='output')
        return False

    #most of the time i can't use these so added for realism
    elif any(char in "!#$%^&*()?,./;:" for char in password):
        display('Password contains unexpected character.', target='output')
        return False

    #added this as an outlier
    elif "@" not in password:
        display('Password must contain @ character.', target='output')
        return False

    #to operate an extra bit of the code
    elif '8' in password or "123" in password or "chuck" in password or "67" in password or "69" in password:
        display('Password is too easy. Do you want a new one?', target='output')
        document.getElementById("passoffer").innerHTML = """
            <button type="button" py-click="new_password" class="btn btn-success btn-sm">Yes</button>
            <button type="button" py-click="keep_password" class="btn btn-danger btn-sm">No</button>
        """
        return False

    else:
        return True

def account_creation(e):
    document.getElementById('output').innerHTML = ' '

    if username_verification(e) == True and password_verification(e) == True:
        display(f'Account created. You may now log in using your credentials.', target='output')
    else:
        display(f'Try again', target='output')
