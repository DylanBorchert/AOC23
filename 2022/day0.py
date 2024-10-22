#day 1 2021 test code
import sys
import os

def parse_data():
    with open(os.path.join(sys.path[0], "test.txt"), "r") as f:
        data = f.read()
        f.close()
    return data

def task_1():
    print(parse_data())
    
def task_2():
    print(parse_data())

task_1()
task_2()