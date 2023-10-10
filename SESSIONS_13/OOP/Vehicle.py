class Vehicle:

    def __init__(self, name):
        self.name = name
        print("Vehicle Created, name: ", name)
    
    def move(self, optional):
        if optional == True:
            print("Moving")
        return "Moving"
    
    def stop(self, optional):
        if optional == True:
            print("Stopping")
        return "Stopping"
    
    def give_name(self, optional):
        if optional == True:
            print(self.name)
        return self.name
    
    def __del__(self): # No longer using the object? --> Remove it (Destructor)
        print("Destructor called", self.name, "deleted")
        print()

light_McQueen = Vehicle("Light McQueen")
light_McQueen.move(False)
light_McQueen.stop(True)
del light_McQueen


class Airplane(Vehicle):

    def __init__(self, name, wings, engines):
        self.engines = engines
        self.wings = wings

        Vehicle.__init__(self, name)

    def flying(self):
        print()
        self.move(True)
        print("Flying in the sky")
        self.stop(True)
        print()

airplane_1 = Airplane('F14', 2, 2)
airplane_1.flying()
del airplane_1