list_info = []  # 存储信息集合
filename = "user_info.txt"  # 缓存文件


def menu():
    print("-------------")
    print("--- 1. 添加名片 ---")
    print("--- 2. 删除名片 ---")
    print("--- 3. 修改名片 ---")
    print("--- 4. 查询名片 ---")
    print("--- 5. 显示全部 ---")
    print("--- 6. 显示操作菜单 ---")
    print("--- 7. 退出系统 ---")


def add_info():
    print("--- 添加名片 ---")
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    list_info.append([name, age])
    print("存储成功%s" % list_info)


def delete_info():
    print("--- 删除名片 ---")
    name = input("请输入姓名：")
    for info in list_info:
        if name in info:  # 姓名在list列表中存在
            list_info.remove(info)
            print("删除 %s 成功" % info)
            break  # 跳出
    else:
        print("姓名不存在")


def show_all_info():
    print("--- 5. 显示全部 ---")
    for info in list_info:
        print(info)


show_menu = True


def search_info():
    print("请输入需要查询的姓名")
    name = input()
    for info in list_info:
        if name in info:
            print("查询结果:%s" % info)
            break
    else:
        print("查询姓名不存在")


def modify_info():
    print("--- 请输入需要修改的姓名 ---")
    name = input()
    for info in list_info:
        if name in info:
            new_name = input("请输入新的姓名：")
            new_age = input("请输入新的年龄：")
            info[0] = new_name
            info[1] = new_age
            print("修改成功:%s" % info)
            break
    else:
        print("姓名不存在")


# 加载文件信息到列表中
def load_info():
    global list_info
    f = open(filename, "r", encoding='utf-8')
    list_info = eval(f.read())


# 保存信息到文件中
def save_info():
    f = open(filename, "w", encoding='utf-8')
    f.write(str(list_info))
    print("保存成功")


def main():
    import os
    if os.path.exists(filename):
        load_info()
    global show_menu
    while True:
        if show_menu:
            menu()
            show_menu = False
        print("请输入指令：", end="")
        command = int(input())
        if command == 1:
            add_info()
        elif command == 2:
            delete_info()
        elif command == 3:
            modify_info()
        elif command == 4:
            search_info()
        elif command == 5:
            show_all_info()
        elif command == 6:
            menu()
        elif command == 7:
            print("退出程序成功")
            save_info()
            break
        else:
            print("输入有误")


main()
