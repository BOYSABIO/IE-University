# When Pi is out of the attribute METHOD then it will not change
class circle:
    pi = 3.14159 # Class attribute (not an object attribute)
    def __init__(self, radius):
        self.radius = radius #Instance or object attribute
    
    def area(self):
        return circle.pi * self.radius ** 2
    
c1 = circle(2)
c2 = circle(3)

print(c1.area())
print()
print(c2.area())
