class Dog:
    # species = "Canine" # Class attribute
    # sound = "bark"
    def __init__(dog_self, name: str = "Dog", age: int = 1):  # Application of using __init__() method
        dog_self.name = name
        dog_self.age = age

    def speak(dog_self):
        print(f"This is {dog_self.name}, I'm {dog_self.age} years old. Bark bark.")


# dog_Tom = Dog("Tommy", 3)
# print(dog_Tom.name + ",", dog_Tom.species)
dog_1 = Dog("Mark", 10)
dog_1.speak()

dog_2 = Dog()
dog_2.speak()