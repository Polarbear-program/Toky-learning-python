class Char:
    def __init__(self, name, stats, levels):
        self.name = name
        self.stats = stats
        self.level = levels
    def show(self):
        print(f"Hello player, I am {self.name}, and my stat is: {self.stats}." 
              f" I'm currently level {self.level}")

class North_Char(Char):
    # This __init__ will override the parents function's inheritance
    def __init__(self, name, stats, levels, power):

        # New property of the North_Char class
        self.power = power

        # super method will act as a bridge for the child's class to gain access
        # to the methods and properties of parent class(maybe sibling class too).
        # In this case it took the self.name = name, self.stats = stats, self.level = levels
        super().__init__(name, stats, levels)

    def speak(self):
        print("Ahhh, so cold")

    def show(self):
        print(f"Alrighty, my name is {self.name}, my stats is: {self.stats}, "  
              f"my level is {self.level}, and my power is: {self.power}")

class South_Char(Char):
    def speak(self):
        print("Ahhh, so hot")
    pass

c1 = North_Char("Aaron", "strong and reliable", 34, "Ice slide")
c1.show()
c1.speak()