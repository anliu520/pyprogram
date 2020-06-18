#Author:Anliu
class People(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eating(self):
        print("%s is eating..."%self.name)

    def sleep(self):
        print("%s is sleepping..."%self.name)

class MakeFirends(object):
    def __init__(self,realheat):
        self.realheat = realheat

    def make(self):
        print("%s %s is make firend ..."%(self.name,self.realheat))

class Man(People,MakeFirends):
    def __init__(self,name,age,type):
        #People.__init__(self,name,age)
        super(Man,self).__init__(name,age)
        self.type = type

    def chou(self):
        print("%s is chouuing....%s"%(self.name,self.type))

class Woman(MakeFirends,People):
    def __init__(self,name,age,realheat):
        #super(Woman,self).__init__(name,age)
        #super(MakeFirends,self).__init__(realheat)
        MakeFirends.__init__(self,realheat)
        People.__init__(self,name,age)
        #MakeFirends.__init__(self,realheat)

    def shpping(self):
        print("%s is shopping ..."%self.name)

r1 = People("runrun","18")
r1.eating()
r1.sleep()
m1 = Man("tianhao","20","haomao")
m1.sleep()
m1.chou()
#m1.make()

w1 = Woman("tongtong","21","money")
#w1.shpping()
w1.make()
