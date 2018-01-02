f = open("python.md", "a+", encoding='utf-8')

print(f.encoding)   # 文件编码
print(f.name)   # 文件名
print(f.mode)   # 操作权限
f.close()
print(f.closed)   # 操作是否已关闭