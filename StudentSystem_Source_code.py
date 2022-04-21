# -*- coding=utf-8 -*-
# 作者:ouyanghongqian(其他名称:ouyhq2011,ouyhq0709,ouyanghongqian.top)
# 这是作者没有使用autopep8工具格式化的版本,不建议使用这个版本!
import requests
import os
import sys
debug=False
flag=0
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
def main(savefile):#最开始是打算用全局变量存储保存文件名的,后来发现自己不太会,就作为参数传入吧
    print_menu()
    global flag
    if not os.path.exists(os.getcwd()+"\data.ssdata"):
        print("您似乎是第一次使用\删除了默认数据文件,需要创建默认数据文件吗?(使用是和不回答)")
        userinput=input()
        if userinput=="不":
            print("好的,那么请手动设置,但是程序还是会创建一个名为data.ssdata的空文件,防止下次使用本系统时再次询问以及部分程序发生bug")
            open("data.ssdata", mode='x',encoding="utf-8")
            select()
        elif userinput=="是":open("data.ssdata", mode='x',encoding="utf-8");savefile="data.ssdata"
        else:
            print("您的输入不正确,将自动为您创建数据文件,您在本文件下的工作目录中删除data.ssdata即可")
            open("data.ssdata", mode='x',encoding="utf-8")
            savefile="data.ssdata"
    else:
        if flag==1:
            pass
        else:
            savefile="data.ssdata"
    if flag==0:
        flag=1
    flag=True
    while flag:
        userinput=input(">>>")# -*- coding=utf-8 -*-
# 作者:ouyanghongqian(其他名称:ouyhq2011,ouyhq0709,ouyanghongqian.top)
# 这是作者没有使用autopep8工具格式化的版本,不建议使用这个版本!
# 版本-0.1.0
from asyncore import write
from posixpath import split
import requests
import os
import sys
import ctypes
import json
import urllib
safeText=["用户尝试录入学生信息","用户正在查找学生信息","用户正在删除学生信息","用户正在显示所有学生信息","用户正在选择/从网络上导入文件","用户正在修改学生信息","用户正在修改安全模块配置"]
def is_admin():#管理员权限判断
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
safesettingfile="C:/safesetting.ssdata"
debug=False
flag=0
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
    7 安全功能设置
    0 退出学生系统
    """)
def main(savefile):#最开始是打算用全局变量存储保存文件名的,后来发现自己不太会,就作为参数传入吧
    print_menu()
    global flag
    if not os.path.exists(os.getcwd()+"\data.ssdata"):
        print("您似乎是第一次使用\删除了默认数据文件,需要创建默认数据文件吗?(使用是和不回答)")
        userinput=input()
        if userinput=="不":
            print("好的,那么请手动设置,但是程序还是会创建一个名为data.ssdata的空文件,防止下次使用本系统时再次询问以及部分程序发生bug")
            open("data.ssdata", mode='x',encoding="utf-8")
            select()
        elif userinput=="是":open("data.ssdata", mode='x',encoding="utf-8");savefile="data.ssdata"
        else:
            print("您的输入不正确,将自动为您创建数据文件,您在本文件下的工作目录中删除data.ssdata即可")
            open("data.ssdata", mode='x',encoding="utf-8")
            savefile="data.ssdata"
    else:
        if flag==1:
            pass
        else:
            savefile="data.ssdata"
    if flag==0:
        flag=1
    flag=True
    while flag:
        userinput=input(">>>")
        try:
            userinput=int(userinput)
        except Exception as e:
            print('您输入的不是数字,请输入数字\n报错信息:',e)
            if userinput=="debug":
                debug=True
                if debug==True:
                    pass
            else:
                continue
        if userinput==1:insert(savefile,0)
        elif userinput==2:find(savefile)
        elif userinput==3:delete(savefile,input("请输入ID:"),0)
        elif userinput==4:show(savefile,0,0,0)
        elif userinput==5:select(savefile)
        elif userinput==6:edit(savefile)
        elif userinput==7:safeConfigFile(savefile)
        elif userinput==0:flag=False
        else:
            if debug:
                exec(input())
            else:
                print("您输入的有误,请重新输入");continue
    print("您已退出学生信息管理系统!")
    sys.exit()
def select(savefile):
    print("当前使用文件:",savefile)
    print("是否更改使用文件?(使用y和n回答)")
    send_request(safeText[4])
    userinput=input()
    if userinput=="y":
        userinput=input("请选择更改模式\n1 从网络上导入\n2 选择目录下已有的文件")
        try:
            userinput=int(userinput)
        except Exception as e:
            print('您输入的不是数字,请输入数字\n报错信息:',e)
            select()
        if userinput==1:
            flag=True
        else:
            flag=False
        while flag:
            try:
                userinput=int(userinput)
            except Exception as e:
                print('您输入的不是数字,请输入数字\n报错信息:',e)
                select()
            if userinput==1:
                userinput=input("请输入网址(带http\https):")
                try:
                    getdata=requests.get(userinput)
                except Exception as e:
                    print("您输入的网址可能不正确\没有http头\网页不存在\没有安装requests库,请确认网址后再次输入")
                    print("报错信息",e)
                    try:
                        print(getdata.status_code,"\n",getdata.text,'\n',getdata.encoding)
                        select(savefile)
                    except Exception as e:
                        print("在尝试输出select函数内的requests错误时发生错误,原因可能是没有安装python库")
                        print("报错信息:",e)
                        select(savefile)
                print("成功获取到了数据!")
                getdata=getdata.text
                userinput=input("请输入文件名(留空则为downloadfile.ssdata)")
                if userinput=="":
                    userinput="downloadfile.ssdata"
                else:
                    pass
                try:
                    path=os.getcwd()+"/"+userinput
                    f = open(path,"w")
                    f.write(getdata)
                    f.close()
                except Exception as e:
                    print("在尝试读取获取到的文件并写入进本地磁盘时发生错误")
                    print("报错信息:",e)
                    select(savefile)
                print("成功写入!请不要重复使用同一个文件名!否则下次写入时会合并已有数据和获取数据")
                if input("请问是否需要更改使用文件?(需要的话就输y,不需要随便输)")=="y":
                    main(userinput)
                main("data.ssdata")
        userinput=input("请输入选择的文件名:")
        main(userinput)
    elif userinput=="n":
        main(savefile)
    else:
        print("您的输入不正确,请使用全小写字母回答")
        select(savefile)
def insert(savefile,mode):
    flag=True
    while flag:
        userinput_ID=input('请输入ID:')
        userinput_NAME=input("请输入名称:")
        userinput_chinese=input("请输入语文分数:")
        userinput_english=input("请输入英语分数:")
        userinput_math=input("请输入数学分数:")
        try:
            userinput_ID=int(userinput_ID)
            userinput_chinese=int(userinput_chinese)
            userinput_english=int(userinput_english)
            userinput_math=int(userinput_math)
        except Exception as e:
            print('您输入的不是数字,请输入数字\n报错信息:',e)
            continue
        info_={"id":userinput_ID,"name":userinput_NAME,"chinese":userinput_chinese,"english":userinput_english,"math":userinput_math}
        save(info_,savefile)
        if mode==0:
            if input("添加成功!\n是否继续添加?(y/n):")=="y":
                pass
            else:
                flag=False
        main(savefile)
def save(info,savefile):
    send_request(safeText[0]+" 添加的数据为："+info)
    if os.path.exists(os.getcwd()+"/"+savefile):
        savefile_=open(savefile,"a")
    else:
        savefile_=open(savefile,"w")
    savefile_.write(str(info)+"\n")
    savefile_.close()
def show(savefile,mode,id,mode_2):
    list_=[]
    with open(savefile,"r") as file:
        studentdata1=file.readlines()
    for list_2 in studentdata1:
        list_.append(eval(list_2))
    if mode==0:
        for i in list_:
            send_request(safeText[3])
            print("ID:%s   名称:%s   语文成绩:%s   英语成绩:%s   数学成绩:%s" % (i["id"],i["name"],i["chinese"] ,i["english"], i["math"]))
        main(savefile)
    elif mode==1:
        for i in list_:
            if id==i["id"]:
                send_request(safeText[1]+" 查询的数据为："+str(i))
                if mode_2==0:
                    print("找到ID为",id,"的学生!其信息为:",'名称:',i["name"],'语文成绩:',i["chinese"] ,'   英语成绩:',i['english'], '   数学成绩:',i['math'])
                else:
                    return (i["id"],i["name"],i["chinese"] ,i["english"], i["math"])
        main(savefile)
def find(savefile):
    userinput=input("请输入学生ID:")
    try:
        userinput=int(userinput)
    except Exception as e:
        print("您输入的不是数字!\n报错信息:",e)
        find(savefile)
    show(savefile,1,userinput,0)
    main(savefile)
def delete(savefile,id,mode):
    list_=[]
    try:
        id=int(id)
    except Exception as e:
        print("您输入的不是数字!")
    with open(savefile,"r") as file:
        studentdata1=file.readlines()
    for list_2 in studentdata1:
        list_.append(eval(list_2))
    for i in list_:
        if id==i["id"]:
            list_.remove(i)
    with open(savefile,"w") as f:
        f.truncate()
        for i in list_:
            save(i,savefile)
    send_request(safeText[2]+" 删除的数据为："+str(id))
    if mode==1:
        pass
    else:
        main(savefile)
def edit(savefile):
    id_=input("请输入要修改的学生ID:")
    send_request(safeText[5]+" 修改的数据为："+str(id_))
    delete(savefile,id_,1)
    insert(savefile,1)
    main(savefile)
def safeLoadConfigFile():
    if not os.path.exists("C:\\safeconfig.ssdata"):
        return ["未设置密码","未设置webhook"]
    with open("C:\\safeconfig.ssdata",mode="r") as safeFile:
        file_safe=safeFile.readlines()
    safeFileList=LoadStrToList(file_safe)
    return safeFileList
def LoadStrToList(list_):
    list_2=[]
    for i in list_:
        list_2.append(i.split("\n")[0])
    return list_2
def safeConfigFile(savefile):
    if is_admin():
        send_request(safeText[6])
        if not os.path.exists("C:\\safeconfig.ssdata"):
            with open("C:\\safeconfig.ssdata",mode="x") as f:
                f.write("未设置密码\n")
                f.write("未设置webhook")
        safeFileList=safeLoadConfigFile()
        if not safeFileList[0] == "未设置密码":
            if not hash(input("请输入密码验证身份："))==safeFileList[0]:
                print("密码错误！")
                sys.exit()
        print("当前webhook为:%s\n当前密码为:%s"%(safeFileList[1],safeFileList[0]))
        if input("是否修改数据?(y/n):")=="y":
            userinput=input("请选择要修改的数据(webhook/密码 reset重置)：")
            if userinput=="密码":
                userinput=input("请输入密码：")
                userinput2=input("请再次输入密码，确认是否是正确的密码：")
                if not userinput==userinput2:
                    print("输入密码不一致，自动退出")
                    main(savefile)
                safeFileList[0]=hash(userinput)
                writeSafeConfig(safeFileList)
                main(savefile)
            elif userinput=="webhook":
                userinput=input("请输入webhook(当前只支持钉钉群聊机器人):")
                safeFileList[1]=userinput
                writeSafeConfig(safeFileList)
                print("添加成功！请在钉钉机器人管理界面添加关键词'[学生信息管理系统]'，让此系统可以正常的发送消息")
                main(savefile)
            elif userinput=="reset":
                safeFileList=["未设置密码","未设置webhook"]
                writeSafeConfig(safeFileList)
    else:
        print("没有检测到管理员权限，此功能需要管理员权限，请使用管理员权限运行")
def send_request(datas):
    if not safeLoadConfigFile()[1]=="未设置webhook":
        header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }
        sendData = json.dumps(datas)
        sendDatas = sendData.encode("utf-8")  
        request = urllib.request.Request(url=safeLoadConfigFile()[1], data=sendDatas, headers=header)
        opener = urllib.request.urlopen(request)
def writeSafeConfig(safeFileList):
    with open("C:\\safeconfig.ssdata",mode="w") as f:
        f.truncate()
        for i in safeFileList:
            f.write(i+"\n")
def userInputPwd(return_,savefile):
    if os.path.exists("C:\\safeconfig.ssdata"):
        if safeLoadConfigFile()[0]=="未设置密码":
            if hash(input("请输入密码:"))==safeLoadConfigFile()[0]:
                return_(savefile)
def ifHaveNewVer():
    try:
        internetCode=requests.get("https://gitee.com/oyhqnbnb/studentsystem/raw/main/StudentSystem.py")
        internetCode=internetCode.text.split("\n")[3]
        for i in internetCode:
            with open(os.path.abspath(__file__),"r") as f:
                if i==f.readlines().split("\n")[3]:
                    return False
                else:
                    return True
    except Exception as e:
        print("没有网络，将无法检查新版本，错误代码：%s"%e)
def update():
    updateCode=requests.get("https://gitee.com/oyhqnbnb/studentsystem/raw/main/StudentSystem.py").text
    with open(os.path.abspath(__file__),"w") as f:
        f.truncate()
        for i in updateCode.split("\n"):
            f.write(i+"\n")
if __name__=="__main__":
    try:
        if not is_admin():
            print("没有检测到管理员权限，将无法使用安全配置功能，请使用管理员权限运行，以启用安全配置等其他功能")
        if ifHaveNewVer():
            print("发现新版本，是否更新？(y/n)")
            if input()=="y":
                print(" 正在更新...请确保网络畅通")
                update()
                os.system("python3 %s"%os.path.abspath(__file__))
        userInputPwd(main,"未选择")
    except Exception as e:
        print("发生无法预料的错误，请把错误信息和发生错误时的状态发送至ouyanghongqian@qq.com，错误信息为：%s"%e)
        try:
            userinput=int(userinput)
        except Exception as e:
            print('您输入的不是数字,请输入数字\n报错信息:',e)
            if userinput=="debug":
                debug=True
                if debug==True:
                    pass
            else:
                continue
        if userinput==1:insert(savefile,0)
        elif userinput==2:find(savefile)
        elif userinput==3:delete(savefile,input("请输入ID:"),0)
        elif userinput==4:show(savefile,0,0,0)
        elif userinput==5:select(savefile)
        elif userinput==6:edit(savefile)
        elif userinput==0:flag=False
        else:
            if debug:
                exec(input())
            else:
                print("您输入的有误,请重新输入");continue
    print("您已退出学生信息管理系统!")
    sys.exit()
def select(savefile):
    print("当前使用文件:",savefile)
    print("是否更改使用文件?(使用y和n回答)")
    userinput=input()
    if userinput=="y":
        userinput=input("请选择更改模式\n1 从网络上导入\n2 选择目录下已有的文件")
        try:
            userinput=int(userinput)
        except Exception as e:
            print('您输入的不是数字,请输入数字\n报错信息:',e)
            select()
        if userinput==1:
            flag=True
        else:
            flag=False
        while flag:
            try:
                userinput=int(userinput)
            except Exception as e:
                print('您输入的不是数字,请输入数字\n报错信息:',e)
                select()
            if userinput==1:
                userinput=input("请输入网址(带http\https):")
                try:
                    getdata=requests.get(userinput)
                except Exception as e:
                    print("您输入的网址可能不正确\没有http头\网页不存在\没有安装requests库,请确认网址后再次输入")
                    print("报错信息",e)
                    try:
                        print(getdata.status_code,"\n",getdata.text,'\n',getdata.encoding)
                        select(savefile)
                    except Exception as e:
                        print("在尝试输出select函数内的requests错误时发生错误,原因可能是没有安装python库")
                        print("报错信息:",e)
                        select(savefile)
                print("成功获取到了数据!")
                getdata=getdata.text
                userinput=input("请输入文件名(留空则为downloadfile.ssdata)")
                if userinput=="":
                    userinput="downloadfile.ssdata"
                else:
                    pass
                try:
                    path=os.getcwd()+"/"+userinput
                    f = open(path,"w")
                    f.write(getdata)
                    f.close()
                except Exception as e:
                    print("在尝试读取获取到的文件并写入进本地磁盘时发生错误")
                    print("报错信息:",e)
                    select(savefile)
                print("成功写入!请不要重复使用同一个文件名!否则下次写入时会合并已有数据和获取数据")
                if input("请问是否需要更改使用文件?(需要的话就输y,不需要随便输)")=="y":
                    main(userinput)
                main("data.ssdata")
        userinput=input("请输入选择的文件名:")
        main(userinput)
    elif userinput=="n":
        main(savefile)
    else:
        print("您的输入不正确,请使用全小写字母回答")
        select(savefile)
def insert(savefile,mode):
    flag=True
    while flag:
        userinput_ID=input('请输入ID:')
        userinput_NAME=input("请输入名称:")
        userinput_chinese=input("请输入语文分数:")
        userinput_english=input("请输入英语分数:")
        userinput_math=input("请输入数学分数:")
        try:
            userinput_ID=int(userinput_ID)
            userinput_chinese=int(userinput_chinese)
            userinput_english=int(userinput_english)
            userinput_math=int(userinput_math)
        except Exception as e:
            print('您输入的不是数字,请输入数字\n报错信息:',e)
            continue
        info_={"id":userinput_ID,"name":userinput_NAME,"chinese":userinput_chinese,"english":userinput_english,"math":userinput_math}
        save(info_,savefile)
        if mode==0:
            if input("添加成功!\n是否继续添加?(y/n):")=="y":
                pass
            else:
                flag=False
        main(savefile)
def save(info,savefile):
    if os.path.exists(os.getcwd()+"/"+savefile):
        savefile_=open(savefile,"a")
    else:
        savefile_=open(savefile,"w")
    savefile_.write(str(info)+"\n")
    savefile_.close()
def show(savefile,mode,id,mode_2):
    list_=[]
    with open(savefile,"r") as file:
        studentdata1=file.readlines()
    for list_2 in studentdata1:
        list_.append(eval(list_2))
    if mode==0:
        for i in list_:
            print("ID:%s   名称:%s   语文成绩:%s   英语成绩:%s   数学成绩:%s" % (i["id"],i["name"],i["chinese"] ,i["english"], i["math"]))
        main(savefile)
    elif mode==1:
        for i in list_:
            if id==i["id"]:
                if mode_2==0:
                    print("找到ID为",id,"的学生!其信息为:",'名称:',i["name"],'语文成绩:',i["chinese"] ,'   英语成绩:',i['english'], '   数学成绩:',i['math'])
                else:
                    return (i["id"],i["name"],i["chinese"] ,i["english"], i["math"])
        main(savefile)
def find(savefile):
    userinput=input("请输入学生ID:")
    try:
        userinput=int(userinput)
    except Exception as e:
        print("您输入的不是数字!\n报错信息:",e)
        find(savefile)
    show(savefile,1,userinput,0)
    main(savefile)
def delete(savefile,id,mode):
    list_=[]
    try:
        id=int(id)
    except Exception as e:
        print("您输入的不是数字!")
    with open(savefile,"r") as file:
        studentdata1=file.readlines()
    for list_2 in studentdata1:
        list_.append(eval(list_2))
    for i in list_:
        if id==i["id"]:
            list_.remove(i)
    with open(savefile,"w") as f:
        f.truncate()
        for i in list_:
            save(i,savefile)
    if mode==1:
        pass
    else:
        main(savefile)
def edit(savefile):
    delete(savefile,input("请输入ID:"),1)
    insert(savefile,1)
    main(savefile)
if __name__=="__main__":
    main("未选择")
