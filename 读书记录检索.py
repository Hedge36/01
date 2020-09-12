# 读书记录
#——————————文本读取———————————
file = open("D:/Study/Python/源代码/自编代码/杂七杂八/读书记录/读书记录.txt",
            "r", encoding='UTF-8')
lists = file.read()
file.close()
#—————————————————————————


#——————————数据读取———————————
lists = lists.split(" ")
list_all = []
for i in range(len(lists) // 6):
    list_one = lists[6 * i: 6 * i + 6]
    if "\n" in str(list_one[0]):
        list_one[0] = str(list_one[0]).replace("\n", "")   # 除去回车
    list_all.append(list_one)
#—————————————————————————


#——————————结果打印区——————————
def list_print(target_list):
    print("书籍序号：", target_list[0])
    print("书籍名称：《%s》" % (target_list[1]))
    print("书籍类别：", target_list[2])
    print("核心概括：", target_list[3])
    print("阅读进度：", target_list[4])
    print("复阅评估：", target_list[5], end="\n\n")
#-————————————————————————————


#——————————条件检索区——————————
print("检索条件提供：序号检索1，名称检索2，类别检索3，复阅检索4，全部检索5")
condition = input("请输入检索条件对应序号:")
#—————————————————————————————


#——————————序号检索区——————————
nums = [list_all[i][0] for i in range(len(list_all) // 1)]    # 序号整理
if condition == "1":
    print("————————————————————————————————")
    serial_number = input("请输入需要检索的序号:")
    if serial_number in nums:
        print("————————————————————————————————")
        print("检索结果如下：")
        list_print(list_all[int(serial_number) - 1])
    else:
        print("输入格式有误，请重新启动程序。")
#—————————————————————————————

#——————————名称检索区——————————

elif condition == "2":
    name = [list_all[i][1] for i in range(len(list_all) // 1)]    # 书籍整理
    print("————————————————————————————————")
    name_book = input("请输入需要检索的书籍名称(无需带书名号):")
    if name_book in name:
        a = 0
        for i in range(len(list_all) // 1):
            if list_all[i][1] == name_book:
                a = i
                break
        print("————————————————————————————————")
        print("检索结果如下：")
        list_print(list_all[a])
    else:
        print("输入格式有误，请重新启动程序。")
#—————————————————————————————

#——————————类别检索区——————————
elif condition == "3":
    category = list(set([list_all[i][2]
                         for i in range(len(list_all) // 1)]))    # 类别整理
    print("————————————————————————————————")
    print("现可供检索的类别：")
    for i in range(len(category) // 1):
        print(category[i], end=',')
    print("\n————————————————————————————————")
    category_book = input("请输入需要检索的书籍类别:")
    if category_book in category:
        print("————————————————————————————————")
        print("检索结果如下：")
        for i in range(len(list_all) // 1):
            if list_all[i][2] == category_book:
                list_print(list_all[i])
    else:
        print("输入格式有误，请重新启动程序。")
#—————————————————————————————

#——————————复阅检索区——————————
elif condition == "4":
    print("————————————————————————————————")
    print("提示：可供检索的复阅类型:\n是(推荐复阅)，否(不推荐复阅)，自选(可供选择复阅)")
    evaluation_book = input("\n请输入需要检索的复阅类型:")
    if evaluation_book in ["是", "否", "自选"]:
        print("————————————————————————————————")
        print("检索结果如下：")
        for i in range(len(list_all) // 1):
            if list_all[i][5] == evaluation_book:
                list_print(list_all[i])
    else:
        print("输入格式有误，请重新启动程序。")
#—————————————————————————————

#——————————全部检索区——————————
elif condition == "5":
    print("————————————————————————————————")
    print("检索结果如下：")
    for i in range(len(list_all) // 1):
        list_print(list_all[i])
    print("————————————————————————————————")
#—————————————————————————————

#——————————初期异常处理区————————————
else:
    print("输入格式有误，请重新启动程序。")
#—————————————————————————————

input("键入回车以退出程序。")
