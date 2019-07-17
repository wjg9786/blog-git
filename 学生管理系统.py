#学生保存之后写到某个文件中，程序第一次启动的时候，学生列表从读取文件内容中来
import os
def read_stus():
    '''文件中存数据的格式
    zs\t23\t34324324
    ls\t34\t33434234
    ww\t32\t32423423
    '''
    if os.path.exists(file_name):
        f=open(file_name,"r")
        while True:
            student_str=f.readline()
            if student_str=="":
                break
            elif student_str.strip()!="" and student_str.strip()!="\n":
                student_info_list=student_str.split()
                student={"name":student_info_list[0],"age":student_info_list[1],"qq":student_info_list[2]}
                stus.append(student)
def write_stus_to_file():
    if os.path.exists(file_name):
        if os.path.exists(backup_file):
            os.remove(backup_file)
        os.rename(file_name,"backup-"+file_name)
    f=open(file_name,"w")
    for student in stus:
        student_str="%s\t%s\t%s"%(student["name"],student["age"],student["QQ"])
        f.write(student_str)
        f.write("\n")
    f.close()

def print_menu():
    print("-"*30)
    print("学生管理系统".center(30))
    print("输入1：添加学生")
    print("输入2：查找学生")
    print("输入3：修改学生")
    print("输入4：删除学生")
    print("输入5：查看所有学生")
    print("输入6：退出")

def add_student():
    name=input("请输入学生的姓名：")
    age=input("请输入学生的年龄：")
    qq=input("请输入学生的QQ号：")
    #一个学生包括三个信息，这三个信息存在一个字典中
    stu={}#申明 一个字典变量
    stu["name"]=name#往字典中添加一个原始
    stu["age"]=age
    stu["QQ"]=qq
    stus.append(stu)
    print("添加成功")

def search_student(name):
    for item in stus:
        if item["name"]==name.strip():#判断字典中包含有改学生的姓名
            print("%s 学生存在"%name)
            print_student(item)
            return item
        else:
            print("学生%s没有找到"%name)

def print_student(item):
    print("%s\t%s\t%s"%(item["name"],item["age"],item["qq"]))

def print_all_student():
    print("序号\t姓名\t年龄\tQQ号")
    for i,item in enumerate(stus,1):
        print("%s\t"%i,end="")
        print_student(item)
def del_studnet(name):
    student=search_student(name)
    stus.remove(student)

def main():
    print_menu()
    read_stus()
    while True:
        operate=input("请输入你想要的操作")
        if operate=="1":
            add_student()
            write_stus_to_file()
        if operate=="2":
            name=input("请输入要查找学生的姓名：")
            search_student(name)
        if operate=="3":
            pass
        if operate=="4":
            name=input("请输入要删除的学生姓名：")
            del_studnet(name)
            print("删除学生%s成功"%name)
            write_stus_to_file()
        if operate=="5":
            print_all_student()
        if operate=="0":
            break
file_name="stus.txt"#存放学生数据的文件
backup_file="backup-stus.txt"
#一个学生包含很多信息，一个学生一个字典，学生列表用列表存储
stus=[]#全局变量

main()

