name1 = "张三"
name2 = name1
print("name1=%s, name2=%s" % (name1, name2))
print("name1 id=%d,name2 id=%d" % (id(name1), id(name2)))

print("----------------------------")

name2 = "李四"
print("name1=%s, name2=%s" % (name1, name2))
print("name1 id=%d,name2 id=%d" % (id(name1), id(name2)))
