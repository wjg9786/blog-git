import os
# 递归求目录
#从给定的目录去查找包含hell关键字py文件有那些
file_list=[]
#递归函数，该函数中所有文件路径全部采用绝对路径,parend_dir，文件所在父目录的绝对路径，file_name表示当前你要处理的文件或者目录
def find_hello(parent_dir,file_name):
    file_abspath=os.path.join(parent_dir,file_name)#当前正在处理的文件或者目录的绝对路径
    if os.path.isdir(file_abspath):#判断当前文件是一个目录，迭代这个目录下的文件
        for f in os.listdir(file_abspath):#进入目录，列出该目录下所有文件列表
            find_hello(file_abspath,f)#递归调用自己本身的函数，只有当是目录才会执行，不是就不会执行
    else:
        if dir.endswith(".py"):#如果传入的文件就是文件，判断文件名是否以.py结尾
            if read_and_find_hello(file_abspath):#读取该py结尾的文件，并且看看文件内容中是否包含有hello
                file_list.append(file_abspath)
#该函数主要功能，读取py结尾的文件，并且看看文件内容中是否包含有hello，如果有返回True，否则返回False
def read_and_find_hello(py_file):
    flag=False#定义一个是否包含有hello的标记变量，默认文件中不包含hello为False
    f=open(py_file)#打开文件
    while True:#由于是一行一行的读取文件，所以需要死循环
        line=f.readline()#读取其中一行
        if line=='':#文件读到最后一行，终止循环
            break
        elif "hello" in line:
            flag=True#该行内容中包含有hello则给变量flag赋值True
            break
    f.close()
    return flag
find_hello("/home","python")#传一个入口目录，文件名是python。
print(file_list)
