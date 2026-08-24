class Login:
    def __init__(self, username: str, password: str, id: int):
        self.username = username
        self.password = password
        self.__id = id
        
        display = self.Output(self)
        display.show()

    def getID(self):
        return self.__id
    
    class Output:
        def __init__(self, login):
            self.login = login

        def show(self):
            print(f"Your username is: {self.login.username}")
            print(f"Your password is: {self.login.password}")

account1 = Login("Toky", "123", 20218147)
print("Your ID is:",account1.getID())
