import os

file_path = os.getcwd()
print("当前目录%s" % file_path)

files_list = os.listdir(file_path)
print(files_list)
file_name = input("请输入需要备份的文件：")
if file_name not in files_list:
    print("文件不存在")
else:
    position = file_name.rfind(".")  # 从右向左查询第一个.好位置
    postfix = file_name[position:]  # 文件后缀，比如.txt
    prefix = file_name[:position]  # 文件前缀music.mp3前缀为musci
    back_file_name = prefix + "_backup" + postfix  # 备份文件名
    print(back_file_name)
    source_file = open(file_name, "rb")  # 读取源文件
    backup_file = open(back_file_name, "wb")  # 写入目标文件

    while True:
        data = source_file.read(1024 * 1024)  # readline() 如果单行数据过大会失败
        print("读取文件数据")
        if len(data) == 0:
            break  # 读取结束，跳出循环
        backup_file.write(data)  # 写入目标文件
    # 关闭文件
    source_file.close()
    backup_file.close()
