"""
关系运算符：返回值都是bool，要么True，要么False
>   大于
>=  大于等于
<   小于
<=  小于等于
==  等于
!=  不等于
"""

age = int(input("请输入年龄："))
if 18 <= age <= 20:
    print("大于18岁")
    print("成年人")
elif 21 < age <= 22:
    print("上大学")
    print("好好学习天天向上")
else:
    print("其他年龄阶段")