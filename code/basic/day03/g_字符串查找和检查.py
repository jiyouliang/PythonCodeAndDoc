"""
字符串查找和检查
"""

##  index() 查找子串是否在整个字符串中，返回子串起始下标，否则报错
mystr = "hello world itcast Python itcast hello"
"""
print(mystr.index("world"))  # 6
print(mystr.index("itcast", 13))  # 从起始位置13开始查找，
print(mystr.index("itcast", 13, 28))  # 从起始位置13到结束卫视28查找，
"""

## find()和index功能一样，但是查询不到返回-1，不会报错
"""
print(mystr.find("itcast"))  # 12
print(mystr.find("itcast", 13))  # 26
print(mystr.find("itcast", 13, 25))  # -1
"""

# count() 统计字符串出现次数，查找不到返回0
"""
print(mystr.count("itcast"))  # 2
"""

# isdigit() 判断是否为整数，返回True/False
"""
str1 = input("输入内容，判断是否为整数：")
if str1.isdigit():
    print("输入%d为整数" % int(str1))
else :
    print("输入%s不为整数" %str1)
"""
# isalpha() 判断字符串是否为纯字母，是返回True，否则False
str1 = "abc"
str2 = "ab."

# isspace() 判断是否由空格组成，是返回True，否则False


# startswith() 判断字符串起始位置是否存在子串，返回True/False
netStr = "http://baidu.com"
print(netStr.startswith("http://")) # True

# endwith() 判断字符串是否以某个子串结束，返回True/False
print(netStr.endswith(".com")) # True