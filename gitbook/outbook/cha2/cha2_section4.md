
### 1.深拷贝例子

    import copy
    list1 = ["A", "B"]
    list2 = copy.deepcopy(list1)
    print("list1=%s, list2=%s" % (list1, list2))
    print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))
    
    print("----------------------------")
    list2.append("C")
    print("list1=%s, list2=%s" % (list1, list2))
    print("list1 id=%d, list2 id=%d" % (id(list1), id(list2)))

<br>
> **输出：**


    list1=['A', 'B'], list2=['A', 'B']
    list1 id=90687208, list2 id=90687448
    ----------------------------
    list1=['A', 'B'], list2=['A', 'B', 'C']
    list1 id=90687208, list2 id=90687448


<br>
> **分析：**

**深拷贝会创建一个和原来对象没有任何关系的对象。不仅id不同，连子对象的id也不同，操作也不会同步。**

