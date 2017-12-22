
### 1.浅拷贝例子

```
list1 = ["A", "B"]
list2 = list1.copy()
print("list1=%s, list2=%s" % (list1, list2))
print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))

print("----------------------------")
list2.append("C")
print("list1=%s, list2=%s" % (list1, list2))
print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))
```

<br>
> **输出：**

```
list1=['A', 'B'], list2=['A', 'B']
list1 id=88800472, list2 id=89224016
----------------------------
list1=['A', 'B'], list2=['A', 'B', 'C']
list1 id=88800472, list2 id=89224016
```

<br>
> **分析：**

list1.copy()、dict1.copy()、set1.copy()都是**浅拷贝**。以list为例，浅拷贝会创建新的列表对象，**id不一样**，但是里面子对象不拷贝，还是是同一个。

