# 可变类型字典
dict1 = {'name': '张三', 'age': 18}
dict2 = dict1
print("dict1=%s, dict2=%s" % (dict1, dict2))
print("dict1 id=%d, dict2 id=%d" % (id(dict1), id(dict2)))

print("----------------------------")
dict2['age'] = 24  # 修改字典数据
print("dict1=%s, dict2=%s" % (dict1, dict2))
print("dict1 id=%d, dict2 id=%d" % (id(dict1), id(dict2)))
