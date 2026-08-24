class Login:
    def __init__(self, username: str, password: str, id: int, score: float):
        self.username = username
        self.password = password

        # These are private variable that can only be access within class
        # Or by calling a function that return the private variables
        self.__id = id
        self.__score = score

        display = self.Output(self)
        display.show()

    def getID(self):
        return self.__id

    def checkScore(self):
        return self.__score

    def checkStatus(self):
        if self.__score > 5.5:
            return "You're pass"
        else:
            return "You're failed"

    class Output:
        def __init__(self, login):
            self.login = login

        def show(self):
            print(f"Your username is: {self.login.username}")
            print(f"Your password is: {self.login.password}")


account1 = Login("Toky", "123", 20218147, 7.6)
print("Your ID is:", account1.getID())
print("Your score is:", account1.checkScore())
print(account1.checkStatus())
