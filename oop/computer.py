class Computer:
    def __init__(self, model: str, brand: str, status: bool):
        self.model = model
        self.brand = brand
        self.status = status

        # Condition properties
        self.ram = self.RAM()
        self.cpu = self.CPU()
        self.gpu = self.GPU()

    def show(self):
        print(f"Model: {self.model}")
        print(f"Brand: {self.brand}")
        print(f"Status: {self.status}")
        
        if self.status == True:

            self.ram.storing()
            self.cpu.processing()
            self.gpu.generating()

    class RAM:
        def storing(self):
            store: str = "Storing data"
            print(store, end=" - ")

    class CPU:
        def processing(self):
            process: str = "Processing data"
            print(process, end=" - ")

    class GPU:
        def generating(self):
            generate: str = "Generating graphic"
            print(generate)


pc1 = Computer("XYK-20", "PCTech", True)
pc1.show()