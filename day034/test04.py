#Author:Anliu
from greenlet import greenlet
import time
def test01():
    time.sleep(1)
    print("haha")
    gr2.switch()
    time.sleep(1)
    print("hehe")
    gr2.switch()

def test02():
    time.sleep(1)
    print("xixi")
    gr1.switch()
    print("xixi")
    print("wowo")

if __name__ == '__main__':
    gr1 = greenlet(test01)
    gr2 = greenlet(test02)
    gr1.switch()
