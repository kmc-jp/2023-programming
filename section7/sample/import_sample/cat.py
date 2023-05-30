class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print("にゃーん")

    def get_name(self):
        return self.name


class BlackCat(Cat):
    def __init__(self, name):
        super().__init__(name)

    def meow(self):
        print("に゛ゃ!!!!")

    def get_name(self):
        return "黒猫の" + self.name
