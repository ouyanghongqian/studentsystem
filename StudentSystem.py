# -*- coding=utf-8 -*-
# 作者:ouyanghongqian(其他名称:ouyhq2011,ouyhq0709,ouyanghongqian.top)
import requests
import os
import sys
debug = False
flag = 0


def print_menu():
    print("""
    学生信息管理系统
    请使用阿拉伯数字选择功能
    1 录入学生信息
    2 查找学生信息
    3 删除学生信息
    4 显示学生信息
    5 选择读写文件
    6 修改学生信息
    0 退出学生系统
    """)


def main(savefile):  # 最开始是打算用全局变量存储保存文件名的,后来发现自己不太会,就作为参数传入吧
    print_menu()
    global flag
    if not os.path.exists(os.getcwd()+"\data.ssdata"):
        print("您似乎是第一次使用\删除了默认数据文件,需要创建默认数据文件吗?(使用是和不回答)")
        userinput = input()
        if userinput == "不":
            print("好的,那么请手动设置,但是程序还是会创建一个名为data.ssdata的空文件,防止下次使用本系统时再次询问以及部分程序发生bug")
            open("data.ssdata", mode='x', encoding="utf-8")
            select()
        elif userinput == "是":
            open("data.ssdata", mode='x', encoding="utf-8")
            savefile = "data.ssdata"
        else:
            print("您的输入不正确,将自动为您创建数据文件,您在本文件下的工作目录中删除data.ssdata即可")
            open("data.ssdata", mode='x', encoding="utf-8")
            savefile = "data.ssdata"
    else:
        if flag == 1:
            pass
        else:
            savefile = "data.ssdata"
    if flag == 0:
        flag = 1
    flag = True
    while flag:
        userinput = input(">>>")
        try:
            userinput = int(userinput)
        except Exception as e:
            print('您输入的不是数字,请输入数字\n报错信息:', e)
            if userinput == "debug":
                debug = True
                if debug == True:
                    pass
            else:
                continue
        if userinput == 1:
            insert(savefile, 0)
        elif userinput == 2:
            find(savefile)
        elif userinput == 3:
            delete(savefile, input("请输入ID:"), 0)
        elif userinput == 4:
            show(savefile, 0, 0, 0)
        elif userinput == 5:
            select(savefile)
        elif userinput == 6:
            edit(savefile)
        elif userinput == 0:
            flag = False
        else:
            if debug:
                exec(input())
            else:
                print("您输入的有误,请重新输入")
                continue
    print("您已退出学生信息管理系统!")
    sys.exit()


def select(savefile):
    print("当前使用文件:", savefile)
    print("是否更改使用文件?(使用y和n回答)")
    userinput = input()
    if userinput == "y":
        userinput = input("请选择更改模式\n1 从网络上导入\n2 选择目录下已有的文件")
        try:
            userinput = int(userinput)
        except Exception as e:
            print('您输入的不是数字,请输入数字\n报错信息:', e)
            select()
        if userinput == 1:
            flag = True
        else:
            flag = False
        while flag:
            try:
                userinput = int(userinput)
            except Exception as e:
                print('您输入的不是数字,请输入数字\n报错信息:', e)
                select()
            if userinput == 1:
                userinput = input("请输入网址(带http\https):")
                try:
                    getdata = requests.get(userinput)
                except Exception as e:
                    print("您输入的网址可能不正确\没有http头\网页不存在\没有安装requests库,请确认网址后再次输入")
                    print("报错信息", e)
                    try:
                        print(getdata.status_code, "\n",
                              getdata.text, '\n', getdata.encoding)
                        select(savefile)
                    except Exception as e:
                        print("在尝试输出select函数内的requests错误时发生错误,原因可能是没有安装python库")
                        print("报错信息:", e)
                        select(savefile)
                print("成功获取到了数据!")
                getdata = getdata.text
                userinput = input("请输入文件名(留空则为downloadfile.ssdata)")
                if userinput == "":
                    userinput = "downloadfile.ssdata"
                else:
                    pass
                try:
                    path = os.getcwd()+"/"+userinput
                    f = open(path, "w")
                    f.write(getdata)
                    f.close()
                except Exception as e:
                    print("在尝试读取获取到的文件并写入进本地磁盘时发生错误")
                    print("报错信息:", e)
                    select(savefile)
                print("成功写入!请不要重复使用同一个文件名!否则下次写入时会合并已有数据和获取数据")
                if input("请问是否需要更改使用文件?(需要的话就输y,不需要随便输)") == "y":
                    main(userinput)
                main("data.ssdata")
        userinput = input("请输入选择的文件名:")
        main(userinput)
    elif userinput == "n":
        main(savefile)
    else:
        print("您的输入不正确,请使用全小写字母回答")
        select(savefile)


def insert(savefile, mode):
    flag = True
    while flag:
        userinput_ID = input('请输入ID:')
        userinput_NAME = input("请输入名称:")
        userinput_chinese = input("请输入语文分数:")
        userinput_english = input("请输入英语分数:")
        userinput_math = input("请输入数学分数:")
        try:
            userinput_ID = int(userinput_ID)
            userinput_chinese = int(userinput_chinese)
            userinput_english = int(userinput_english)
            userinput_math = int(userinput_math)
        except Exception as e:
            print('您输入的不是数字,请输入数字\n报错信息:', e)
            continue
        info_ = {"id": userinput_ID, "name": userinput_NAME, "chinese": userinput_chinese,
                 "english": userinput_english, "math": userinput_math}
        save(info_, savefile)
        if mode == 0:
            if input("添加成功!\n是否继续添加?(y/n):") == "y":
                pass
            else:
                flag = False
        main(savefile)


def save(info, savefile):
    if os.path.exists(os.getcwd()+"/"+savefile):
        savefile_ = open(savefile, "a")
    else:
        savefile_ = open(savefile, "w")
    savefile_.write(str(info)+"\n")
    savefile_.close()


def show(savefile, mode, id, mode_2):
    list_ = []
    with open(savefile, "r") as file:
        studentdata1 = file.readlines()
    for list_2 in studentdata1:
        list_.append(eval(list_2))
    if mode == 0:
        for i in list_:
            print("ID:%s   名称:%s   语文成绩:%s   英语成绩:%s   数学成绩:%s" %
                  (i["id"], i["name"], i["chinese"], i["english"], i["math"]))
        main(savefile)
    elif mode == 1:
        for i in list_:
            if id == i["id"]:
                if mode_2 == 0:
                    print("找到ID为", id, "的学生!其信息为:", '名称:',
                          i["name"], '语文成绩:', i["chinese"], '   英语成绩:', i['english'], '   数学成绩:', i['math'])
                else:
                    return (i["id"], i["name"], i["chinese"], i["english"], i["math"])
        main(savefile)


def find(savefile):
    userinput = input("请输入学生ID:")
    try:
        userinput = int(userinput)
    except Exception as e:
        print("您输入的不是数字!\n报错信息:", e)
        find(savefile)
    show(savefile, 1, userinput, 0)
    main(savefile)


def delete(savefile, id, mode):
    list_ = []
    try:
        id = int(id)
    except Exception as e:
        print("您输入的不是数字!")
    with open(savefile, "r") as file:
        studentdata1 = file.readlines()
    for list_2 in studentdata1:
        list_.append(eval(list_2))
    for i in list_:
        if id == i["id"]:
            list_.remove(i)
    with open(savefile, "w") as f:
        f.truncate()
        for i in list_:
            save(i, savefile)
    if mode == 1:
        pass
    else:
        main(savefile)


def edit(savefile):
    delete(savefile, input("请输入ID:"), 1)
    insert(savefile, 1)
    main(savefile)


if __name__ == "__main__":
    main("未选择")
