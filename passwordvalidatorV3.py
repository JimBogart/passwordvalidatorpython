password = str(input("What is your password?:"))

def passwordValidator(password):

    passwordlength = len(password)

    if passwordlength <= 8 and password.isnumeric() == True:
        passwordstrengthscore = 1
    elif passwordlength <= 8 and password.isalpha()== True:
        passwordstrengthscore = 2
    elif passwordlength >= 8 and password.isalnum() == True:
        passwordstrengthscore = 3
    elif passwordlength >= 8 and password.isalnum() == False:
        passwordstrengthscore = 4

    if passwordstrengthscore == 4:
        return("The password " + password + " is a very strong password")
    elif passwordstrengthscore == 3:
        return("The password " + password + " is a strong password")
    elif passwordstrengthscore == 2:
        return("The password " + password + " is a weak password")
    elif passwordstrengthscore == 1:
        return("The password " + password + " is a very weak password")

print(passwordValidator(password))
