#day 1 2021 test code
import sys
import os

def parse_data():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        data = f.read()
        f.close()
    return data

def task_1():
    get_unique(parse_data(), 4)
    
def task_2():
    get_unique(parse_data(), 14)
        
def get_unique(data, distinct):
    for i in range(0, len(data)):
        packet = data[i:i+distinct]
        if len(set(packet)) == distinct:
            print(i+distinct)
            break

task_1()
task_2()