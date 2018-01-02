# object 是Python 里所有类的最顶级父类，相当于java中的Object，Kotlin中的Any
# 类名命名规则： 遵循大驼峰命名法
# class A:        # 旧式类
# class A():


class Animal(object):

    # 实例方法
    def info(self):
        print("info()")
        print(self)


# 创建类对象
animal = Animal()

animal.info()


