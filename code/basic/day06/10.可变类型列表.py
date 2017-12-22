list1 = ['张三', '李四']
list2 = list1
print("list1=%s, list2=%s" % (list1, list2))
print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))

print("----------------------------")
list2.append('王五')
print("list1=%s, list2=%s" % (list1, list2))
print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))

print("----------------------------")
list2[2] = '赵六'
print("list1=%s, list2=%s" % (list1, list2))
print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))

