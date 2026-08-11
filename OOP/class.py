class Dog:
    species = "Canine" # Class attribute
    sound = "bark"

    def __init__(self, name, age): # Application of using __init__() method
        self.name = name
        self.age = age

dog_Tom = Dog("Tommy", 3)
print(dog_Tom.name + ",", dog_Tom.species)