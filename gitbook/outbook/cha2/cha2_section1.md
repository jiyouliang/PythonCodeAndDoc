
### 1.引用

**Python万物皆对象，一切参数的传递都是对象的引用**

### 2.例子

```
list2 = list1
print("list1=%s, list2=%s" % (list1, list2))
print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))

print("----------------------------")
list2.append("王五")
print("list1=%s, list2=%s" % (list1, list2))
print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))
```

<br>
> **输出：**

```
list1=['张三', '李四'], list2=['张三', '李四']
list1 id=88407256, list2 id=88407256
----------------------------
list1=['张三', '李四', '王五'], list2=['张三', '李四', '王五']
list1 id=88407256, list2 id=88407256
```

<br>
> **分析：**

**操作的是同一个列表对象，id 相同，值相同，同时操作也同步。不论修改哪个，另一个也发生改变，因为list为可变类型。**

