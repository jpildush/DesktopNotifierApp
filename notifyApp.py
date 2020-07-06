import userFavourites
from os import path

class notifyApp:
    def __init__(self):
        self.isStarted = True
        self.userFavourites
        self.user = ""

    def runApplication(self):
        while self.isStarted:
            user = input("Please provide your username (max 10 letters - 0 to EXIT): ").strip()

            if int(user) == 0:
                self.isStarted = False
            else:
                if len(user) <= 10:
                    self.user = user
                    # User checking here - if exist login, if does not exist create account.
                    # path.exists("/users/")
                    # create a user folder and place an output of a favourite object in the folder
                    # import object if user exists, otherwise create new user directory and create a new favourite object for the user
                    print("Thank you for signing in!")
                    self.runApplicationFor(user)




    def runApplicationFor(self, user):
        while True:
            print("Chose an Option!")
            print("1 - Add New RSS")
            print("2 - Show All")
            print("0 - Exit")

            option = int(input(": ").strip())

            if option == 0:
                break
            elif option == 1:
                self.userFavourites.addRSS()
            elif option == 2:
                continue
            else:
                print("Chose an option from the menu!")