import userFavourites

class notifyApp:
    def __init__(self):
        self.isStarted = True
        self.userFavourites = []

    def runApplication(self):
        while self.isStarted:
            print("Please provide your username (max 10 letters): ")
            option = str(input(": ").strip())

            if option <= 10:
                # User checking here
                print("Thank you for signing in!")
                self.runApplicationFor(option)




    def runApplicationFor(self, user):
        while True:
            print("Chose an Option!")
            print("1 - Add RSS")
            print("2 - Show All")
            print("0 - Exit")

            option = int(input(": ").strip())

            if option == 0:
                self.isStarted = False
            elif option == 1:
                addRSS()
            elif option == 2:
                continue
            else:
                print("Chose an option from the menu!")