#Author:Anliu
import time

#"生产者："
def consumer(name):
    print("%s 开始消费了"%name)
    while True:
        massage = yield
        print("消息:[%s],被[%s]接收了"%(massage,name))

c = consumer("runrun")
#print(c.__next__())

#"消费者："
def produce(name):
    #初始化生成器
    c1 = consumer("leilei")   #consumer 没有运行
    c2 = consumer("quanquan")  #consumer 没有运行
    c3 = consumer("tongtong")   #consumer 没有运行
    #调运
    c1.__next__()
    c2.__next__()
    c3.__next__()
    print("%s：开始生产消息了..."%name)
    for i in range(10):
        time.sleep(1)
        #mesg = "明天放假不上课"
        #print("明天放假不上课")
        #print(i)
        #c1.send(mesg)
        #c2.send(mesg)
        #c3.send(mesg)
        c1.send(i)
        c2.send(i)
        c3.send(i)

#produce("anliu")



