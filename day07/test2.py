#Author:Anliu
school = "xingyun"  #作用域在全局
def test1(name):
    print("before:",name)
    global school               #在函数中修改全局变量
    school = "shangluoxueyan"   #局部
    print(school)
    name = "ANLIU"  #  作用域在函数内部
    print("after:",name)

#test1("anliu")
#name = "anliu"
#print(school)

dict = {"name":"anliu","age":"18"}
def test2(vars):
    print("B:",vars)
    vars["name"] = "ANLIU"    #局部变量
    print("F:",vars)

test2(dict)
print(dict)
