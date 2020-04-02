#Author:Anliu
import time
time_format = "%Y-%m-%d %X"
time_current = time.strftime(time_format)
def logger():
    """this is a test logger..."""

    print("%s this is a test logger" %time_current)

def test1():
    """ test1"""

    logger()
    print("test1")

def test2():
    """test2"""

    logger()
    print("test2")

def test3():
    """test3"""

    logger()
    print("test3")

test1()
test2()
test3()