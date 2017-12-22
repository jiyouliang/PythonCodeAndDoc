# 不可变类型-元组
t1 = ("张三", "李四")
t2 = t1
print("t1=%s, t2=%s" % (t1, t2))
print("t1 id=%d, t2 id=%d" % (id(t1), id(t2)))
"""
print("t1[0]=%s,  t2[0]=%s" % (t1[0], t2[0]))
print("t1[0] id=%d,  t2[0] id=%d" % (id(t1[0]), id(t2[0])))
"""

print("----------------------------")

t2 = ("张三", "赵六")
print("t1=%s, t2=%s" % (t1, t2))
print("t1 id=%d, t2 id=%d" % (id(t1), id(t2)))
"""
print("t1[0]=%s,  t2[0]=%s" % (t1[0], t2[0]))
print("t1[0] id=%d,  t2[0] id=%d" % (id(t1[0]), id(t2[0])))
"""

