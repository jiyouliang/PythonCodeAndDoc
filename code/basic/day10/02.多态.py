class Human(object):

    def show(self):
        print("Human show")


class Father(Human):

    def show(self):
        print("Father show")


class Mother(Human):
    def show(self):
        print("Mother show")


def test(human: Human):
    human.show()


human = Human()
father = Father()
mother = Mother()

test(human)
test(father)
test(mother)
