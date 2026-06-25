class Animal:
    def __init__(self):
        self.eyes = 2
    
    def breathe(self):
        print("Inhale, exhale")

    
class Fish(Animal):
    def __init__(self):
        super().__init__()
    
    def breathe(self):
        super().breathe()
        print("but under water.")

    def swim(self):
        print("Moving in water")
    
    def swim_backwards(self):
        print("Moving backwards in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
nemo.swim_backwards()
print(nemo.eyes)

whales = Fish()
whales.swim()
whales.breathe()
whales.swim_backwards()
print(whales.eyes)