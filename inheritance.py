class Plant:
    def grow(self):
        print("grow")

class Tree(Plant):
    pass

class Flower(Plant):
    def blossom(self):
        print("blossom")

apple = Tree()
apple.grow()

rose = Flower()
rose.blossom()
rose.grow()