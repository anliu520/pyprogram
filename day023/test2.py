#Author:Anliu
#Author:Anliu
class file():
    platform = "linux"
    def __init__(self,name,inode):
        self.name = name
        self.inode = inode
        self.__foo = None   #（2）初始化一个私有方法

    def open_file(self):
        print("name:%s ;inode:%s file is opening..."%(self.name,self.inode))

    @property
    #def delete_file(self,math):  #(2)直接传递参数将报错:TypeError: delete_file() missing 1 required positional argument: 'math'
    def delete_file(self):
        print("name:%s :inode:%s file is delete...%s  %s"%(self.name,self.inode,self.platform,self.__foo))

    @delete_file.setter          #（2）定义修改方法
    def delete_file(self,math):
       self.__foo = math        #(2)将参数传递给私有方法


f1 =  file("f1","01001")
#f1.delete_file()  #(1)添加属性方法后，本身就不是类的方法，并直接调运
                   #TypeError: 'NoneType' object is not callable
f1.delete_file="aaa"
f1.delete_file


#(2)如何通过属性方法传参？只能通过，重新定义修改方法
#f1.delete_file = "vim"  #(2)传参
#f1.delete_file