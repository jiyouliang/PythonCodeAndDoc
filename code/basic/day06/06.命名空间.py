"""
locals()：包含所有局部变量的命名空间，格式是字典类型
globals()：包含所有全局变量的命名空间，格式也是字典类型
"""

name = "张三"
age = 18


def test1():
    myname = "test1"
    print(myname)
    print(locals())
    print(globals())

test1()
