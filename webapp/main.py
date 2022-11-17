# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import *
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        inputPassword = request.form['title']
        if verifyPassword(inputPassword):
            return '<h1>' + request.form['title'] + '</h1><a href="/">Logout</a>'
        else:
            return '<form method="post"><input type="password" name="title" placeholder="Password"></input><button type="submit">Login</button>'

    return '<form method="post"><input type="password" name="title" placeholder="Password"></input><button type="submit">Login</button>'


# Definition derivied from guidelines from: https://owasp.org/www-project-proactive-controls/v3/en/c6-digital-identity
def verifyPassword(inputPassword):

    # Opens and reads the bad password text file from: https://github.com/danielmiessler/SecLists
    with open('10-million-password-list-top-1000.txt') as badPass:
        if inputPassword in badPass.read():

            # Prints error message if password found is bad password text file
            print("Password found in badPass textfile, please try again")
            return False # set return value to false

    # check is password input is at least 10 characters long
    # OWASP guideline: password to be 10 character long if no MFA enforced
    if len(inputPassword) < 10:
        print("Minimum password length must be 10 Characters")
        return False # Set return value to false

    # else accept password
    else:
        print(inputPassword, "password accepted")
        return True # set value to true


if __name__ == "__main__":
    app.run()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
