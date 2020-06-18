#Author:Anliu
class File_Manage:  #定义类
    #a = "a"   #类变量:存在于类的内存中，不通过实例化即可使用。不能引用在类方法中。
    #hand = "in_handler"
    '''
    文本操作。
    '''
    #print(hand)

    def __init__(self,name):  #构造函数 在实例化时做一些类的初始化的工作
        self.name = name      #实例变量（静态属性），作用域实例本身
        self.__clock = "genkey"   #私有属性，在类的内部可以修改，外部调运时不能调运。
        #name = "name"

    def __run(self):   #私有方法，
        print("running")

    #__run()
    def open(self):           #类的方法，功能性的方法。（动态属性）
        print("%s file is opening...."%(self.name))
        print(self.__clock)
        self.__clock = "123"
        print(self.__clock)


    def close(self):
        print("file is close....")

    def read(self):
        print("file is close...")

    def write(self):
        print("file is write...")

    def __del__(self):
        print("结束了...")

#print(File_Manage)
#hanlder_name ="1234"
file1 = File_Manage("admin")  #实例化，file1类的对象
del file1
#print(file1)
#hand = "handle"    #实例变量:
#file1.open()
#file1.write()
#file1.read()
#file1.close()

#print(file1.name)
#file1.open()

#file1.open()
#file1.run()
#file1.clock = "123"
#print(file1.a)

#file2 = File_Manage("user")
#file3 = File_Manage("user1")
#file2.open()
#file3.open()

#file2.open()