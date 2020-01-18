class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print("draw")
    
    def move(self):
        print("move")

    def present(self):
        print(f"My values are x = {self.x} and y = {self.y}")

point1 = Point(10,20)
point1.draw()
print(point1.x)
print(point1.present())

# no constructor, but can still add x and y
class Point1: 
    def draw(self):
        print("draw")
    
    def move(self):
        print("move")

point2 = Point1()
point2.x = 10
point2.y = 20
point2.draw()
print(point2.x)