a = 10
b = 100


def test1():
    a = -10
    print("局部变量a=%d" % a)


def test2():
    # 修改全局变量
    global b
    b += 10
    print("修改全局变量b=%d" % b)


test1()
test2()
print("修改后的全局变量b=%d" % b)
