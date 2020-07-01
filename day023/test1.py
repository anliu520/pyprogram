#Author:Anliu
class BaseColor(object):
    color =  "color"
    @classmethod
    def value(self):
        #print(self.name)
        return self.color

class Red(BaseColor):
    color = "red"

class Green(BaseColor):
    color = "green"

#print(BaseColor.color)
b = BaseColor()
print(b.value())
print(Green.value())
#print(Green.value())
#print(Red.value())

