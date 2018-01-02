##################################################
# _str_ 魔法函数，相当于java中的toString()
##################################################


class Phone(object):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def __str__(self):
        return "Phone(width=%d,height=%d)" % (self._width, self._height)


p = Phone(320, 480)
print(p)

print(Phone.__doc__)
