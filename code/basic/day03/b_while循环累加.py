# 通过while循环，从1~10累加，只能累加偶数

num = 1
result = 0
while num <= 10:
    if num % 2 == 0:
        result += num
    num += 1
print(result)
