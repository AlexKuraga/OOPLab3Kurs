class Water:
    def __init__(self):
        self.boiled = 0

class Kettle:
    def __init__(self):
        self.water = None

    def isfull(self):
        return self.water is not None

    def boil(self):
        if self.water is not None:
            self.water.boiled = 1
            print("Water boil")
        else:
            print("No water")

    def removeW(self):
        self.water = None
        print("Kettle removed")

    def fullIt(self, water):
        self.water = water

class Match:
    def __init__(self, matches):
        self.matches = matches

    def use_one(self):
        if self.matches != 0:
            self.matches -= 1
            return 1
        return 0

class Sink:
    def __init__(self, all_water):
        self.all_water = all_water
        self.kettle = None

    def putK(self, kettle):
        self.kettle = kettle

    def removeK(self):
        self.kettle = None

    def fillK(self):
        if self.all_water and not self.kettle.isfull():
            self.kettle.fullIt(self.all_water[-1])
            print("Kettle filled")
        else:
            print("No water")

class Stove:
    def __init__(self, matches):
        self.matches = matches
        self.kettle = None

    def putK(self, kettle):
        self.kettle = kettle

    def removeK(self):
        self.kettle = None

    def boilK(self):
        if self.kettle is not None:
            self.kettle.boil()

def main():
    match = Match(10)
    kettle = Kettle()
    water = [Water()]
    sink = Sink(water)
    sink.putK(kettle)
    sink.fillK()
    sink.removeK()
    stove = Stove(match)
    stove.putK(kettle)
    stove.boilK()
    stove.removeK()
    kettle.removeW()

if __name__ == "__main__":
    main()
