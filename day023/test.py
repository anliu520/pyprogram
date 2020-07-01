#Author:Anliu
class People(object):
    def __init__(self,name):
        self.name = name


    def eating(self):
        pass

    def sleep(self):
        pass

    def talk(self):
        print(self.name)
        pass

    @staticmethod
    def run():
        print(self.name)
        pass

r1 = People("tongtong")
r1.talk()
r1.run()



