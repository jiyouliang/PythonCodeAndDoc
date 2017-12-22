# 可变类型set集合
set1 = {'张三', '李四'}
set2 = set1
print("set1=%s, set2=%s" % (set1, set2))
print("set1 id=%d, set2 id=%d" % (id(set1), id(set2)))

print("----------------------------")
set2.add('王五')
print("set1=%s, set2=%s" % (set1, set2))
print("set1 id=%d, set2 id=%d" % (id(set1), id(set2)))
