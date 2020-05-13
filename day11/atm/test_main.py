#Author:Anliu
import os,sys
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_path)
#print(base_path)
#print(sys.path)
import time_test

#persent_path = os.path.dirname(os.path.abspath(__file__))
#sys.path.append(persent_path)
#print(sys.path)
#print(os.path.abspath(__file__))
#print(sys.path)
time_test.time()




def test():
    print("This is a test from test_main....")
