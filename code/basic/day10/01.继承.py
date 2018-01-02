class Human(object):
    def __init__(self):
        print("Human _init_")
        self.name = "Human"


class Father(Human):

    def __init__(self):
        super().__init__()
        print("Father _init_")
        self.name = "Father"


human = Human()
father = Father()

print("human=%s,father=%s" % (human.name, father.name))
