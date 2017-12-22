# Python万物皆对象，一切参数的传递都是对象的引用
# 操作的是同一个列表对象，id 相同，值相同，同时操作也同步
list1 = ["张三", "李四"]
list2 = list1
print("list1=%s, list2=%s" % (list1, list2))
print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))

print("----------------------------")
list2.append("王五")
print("list1=%s, list2=%s" % (list1, list2))
print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))
