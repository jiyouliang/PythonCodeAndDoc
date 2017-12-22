def test1():
    print("无参无返回值函数")


def test2(a):
    print("有参a=%s无返回值函数" % a)


def test3(a):
    print("有参a=%d有返回值函数" % a)
    return a + 10


def test4(a):
    print("无参a=%d有返回值函数" % a)


test1()
test2("hello")
test3(10)
test4(10086)
