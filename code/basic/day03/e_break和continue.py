"""
break   终止循环（比如for、while循环）
continue    结束本次循环，执行下一次循环
"""
"""
i = 0
while i <= 5:
    if i == 3:
        break
    print(i, end=",")
    i += 1
"""
# 输出：0,1,2,

# continue循环
i = 0
while i <= 5:
    if i == 3:
        i += 1  # 必须执行，否则只输出0,1,2
        continue
    print(i)
    i += 1
# 输出：1 2 4 5
