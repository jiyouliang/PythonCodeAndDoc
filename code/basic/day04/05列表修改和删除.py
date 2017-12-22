"""
 list1[index] = 新的数据    # 修改
"""

list1 = ["张三", "李四", "王五", 18]

## 修改指定位置列表数据
list1[1] = "赵六"

## 判断数据是否存在于列表中
if "赵六" in list1:
    print("赵六在列表中")
else:
    print("不存在数据")

print(list1)

## 删除指定数据，如果数据不存在则报错
list2 = ["张三", "李四", "王五", "赵六"]
list2.remove("王五")
print(list2)

## pop()    根据下标删除数据，并返回该数据（没有index参数默认删除末尾数据）,如果下标index大于列表长度抛出pop index out of range异常
list3 = ["张三", "李四", "王五", "赵六"]
print(list3.pop(1))
print(list3.pop())

## clear() 清空所有数据，但不删除列表
list4 = ["张三", "李四", "王五", "赵六"]
print(list4.clear())    # None
print(list4)            # []


## del :Python提供的删除方式,可以删除任何数据，或者列表中某个下标元素
list4 = ["张三", "李四", "王五", "赵六"]
del list4[1]
print(list4)    # ['张三', '王五', '赵六']
del list4
# print(list4)    # 报错'list4' is not defined，因为列表页被删除了



