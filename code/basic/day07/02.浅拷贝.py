# Python万物皆对象，一切参数的传递都是对象的引用
# 操作的是同一个列表对象，id 相同，值相同，同时操作也同步
"""
list1 = ["张三", "李四"]
list2 = list1
print("list1=%s, list2=%s" % (list1, list2))
print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))

print("----------------------------")
list2.append("王五")
print("list1=%s, list2=%s" % (list1, list2))
print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))
"""

## 浅拷贝
list1 = ["A", "B"]
list2 = list1.copy()
print("list1=%s, list2=%s" % (list1, list2))
print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))

print("----------------------------")
list2.append("C")
print("list1=%s, list2=%s" % (list1, list2))
print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))

print("----------------------------")
dict1 = {"name": "张三"}
dict2 = dict1.copy()
print("dict1=%s, dict2=%s" % (dict1, dict2))
print("dict1 id=%d, dict2 id=%d" % (id(dict1), id(dict2)))

print("----------------------------")
dict2['age'] = 18
print("dict1=%s, dict2=%s" % (dict1, dict2))
print("dict1 id=%d, dict2 id=%d" % (id(dict1), id(dict2)))

print("----------------------------")
set1 = {"name": "张三"}
set2 = set1.copy()
print("set1=%s, set2=%s" % (set1, set2))
print("set1 id=%d, set2 id=%d" % (id(set1), id(set2)))
