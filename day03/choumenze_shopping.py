#Author:Anliu
shopping_list = []
goods_list = [
    ('computer   ' ,5500),
    ('keyboard   ' ,350),
    ('mouse      ' ,52),
    ('MobilePhone' ,3000),
    ('PythonBook ' ,96)
]
budget = input("please input your budget:")
info = '''
---------------goods list:---------------
0.{0}
1.{1}
2.{2}
3.{3}
4.{4}
-----------------------------------------
'''.format(goods_list[0],goods_list[1],goods_list[2],goods_list[3],goods_list[4])
if budget.isdigit():  # isdigit() 方法检测字符串是否只由数字组成,是则返回True,否则返回False
   budget = int(budget)
   while True:
       print(info)
       select = input("Please select the goods you want to buy:")
       if select.isdigit():
           select = int(select)
           if select < len(goods_list) and select >= 0:
               product_choice = goods_list[select]
               if product_choice[1] < budget:
                   shopping_list.append(product_choice)
                   budget -= product_choice[1]
                   print("Add %s into your shopping_list,your balance is %s" % (product_choice, budget))
               else:
                   print("余额不足，无法购买！",budget)
                   print("---------shopping list-----------")
                   for s_index, s in enumerate(shopping_list):
                       print(s_index, s)
                   print("---------shopping list-----------")
                   print("你的余额为：",budget)
           else:
               print("没有这个商品")
       elif select == "q":
           print("---------shopping list-----------")
           for s_index, s in enumerate(shopping_list):
               print(s_index, s)
           print("---------shopping list-----------")
           print("你的余额为：",budget)
           exit()
       else:
         print("输入错误")