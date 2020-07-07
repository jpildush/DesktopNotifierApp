'''
DesktopNotifierApp has been solely created by Joseph Pildush.

Third party modules have been imported and used, to enhance the application.
These third party modules listed below have NOT been tampered or altered in any way and I, Joseph Pildush, am NOT the original author.

Python/Third-Party Modules used:
time
notify2
requests
pickle
os
xml
'''


import pickle
import os

from userFavourites import UserFavourites

'''

'''
class notifyApp:
    '''

    '''
    def __init__(self):
        self.isStarted = True
        '''
        Other Variables created within the class:
        ----------------------------------------
        self.user
        self.favourites
        '''

    '''
    
    '''
    def loadUser(self):
        if os.path.exists("/users/" + self.user + "/favourites.pkl"):
            with open("/users/" + self.user + "/favourites.pkl", "rb") as path:
                loadFavourites = pickle.load(path)
            if isinstance(loadFavourites, UserFavourites):
                if self.favourites.userName == self.user:
                    self.favourites = loadFavourites
                    print("Thank you for signing in!")
                else:
                    raise Exception("UserLoadError1", "User error 1: problem with user load-in")
            else:
                raise Exception("ObjectLoadError", "Object error 1: load failed, not a favourite")
        else:
            raise Exception("UserLoadError2", "User not found")


    '''
    
    '''
    def createUser(self):
        os.mkdir("/users/" + self.user)
        self.favourites = UserFavourites(self.user)


    '''
    
    '''
    def runApplication(self):
        while self.isStarted:
            user = input("Please provide your username (max 10 letters - 0 to EXIT): ").strip()

            if int(user) == 0:
                self.isStarted = False
            else:
                if len(user) <= 10:
                    self.user = user
                    # User checking here - if exist login, if does not exist create account.

                    # Create private user later with GUI - display all non private users and
                    # then chose other login to manually enter in private user
                    try:
                        self.loadUser()
                        self.runApplicationFor()
                    except Exception as error:
                        if error.args[0] == "UserLoadError2":
                            self.createUser()
                            self.runApplicationFor()
                        else:
                            print(error.args[0] + ": " + error.args[1])
                            self.isStarted = False

                    # create a user folder and place an output of a favourite object in the folder
                    # import object if user exists, otherwise create new user directory and create a new favourite object for the user

    '''
    
    '''
    def runApplicationFor(self):
        while True:
            print("Chose an Option!")
            print("1 - Add New RSS")
            print("2 - Show RSS")
            print("0 - Exit")

            option = int(input(": ").strip())

            if option == 0:
                break
            elif option == 1:
                self.favourites.addRSS()
            elif option == 2:
                continue
            else:
                print("Error! Chose an option from the menu!")