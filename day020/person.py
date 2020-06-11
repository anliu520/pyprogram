#Author:Anliu
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s ,%s eating"%(self.name,self.age))

    def sleep(self):
        print("sleeping..")


m = person("zhangkai",18)
m.eat()