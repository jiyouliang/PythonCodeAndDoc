def method1():
    print("函数A")
    print("调用函数B")
    method2()


def method2():
    print("函数B")


method1()
method2()
