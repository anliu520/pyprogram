#Author:Anliu
import time
time_formart = '%Y-%m-%d %X'
time_current = time.strftime(time_formart)
def logger(host,ip):
    print("%sthis is a test form %s,%s" %(time_current,host,ip))

def test():
    logger(host="DNS","192.168.42.111")

test()