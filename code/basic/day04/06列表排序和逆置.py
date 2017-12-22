list1 = [8, 1, 3, 5, 6, 4]

## 正序排序
list1.sort()
print(list1)

list2 = [8, 1, 3, 5, 6, 4]
## reverse=True倒序，False正序
list2.sort(reverse=True)
print(list2)

## sorted(list)  Python提供丰富，返回正序排序后新列表，原列表不变
list3 = [8, 1, 3, 5, 6, 4]
result3 = sorted(list3)
print(list3)
print(result3)

## sorted(list, reverse=True)倒序排序，reverse=False正序排序，原列表不变，返回新列表
list4 = [8, 1, 3, 5, 6, 4]
print(sorted(list4, reverse=True))

## reverse() 列表翻转
list5 = [8, 1, 3, 5, 6, 4]
list5.reverse()
print(list5)
