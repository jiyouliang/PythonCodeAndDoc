###############################
# _init_() 构造函数：
# Python 的类里提供的，两个下划线开始，两个下划线结束的方法，就是魔法方法
# 如果类面没有写构造函数，Python会自动创建一个构造函数，但是不执行任何操作。
# 所以，设计一个类，一定有一个构造函数。
###############################


class Person(object):

    # def __init__(self):
    #     self.name = "未命名"
    #     self._age = 18

    # 有参构造
    def __init__(self, name="未命名", age=18):
        self.name = name
        self._age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self._age


person = Person()

print(person.get_age())
print(person.name)

p = Person("张三", 24)
print("name=%s,age=%d" % (p.name, p.get_age()))
