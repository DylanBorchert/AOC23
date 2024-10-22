#day 1 2021 test code
import sys
import os

def parse_data():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        data = f.read()
        f.close()
    return [[list(map(int, y.split("-"))) for y in x.split(",")] for x in data.split()]


def task_1():
    data = parse_data()
    count = 0
    for i in data:
        if(i[0][0] <= i[1][0] and i[0][1] >= i[1][1]) or (i[0][0] >= i[1][0] and i[0][1] <= i[1][1]):
            count += 1
    print(count)


    
def task_2():
    data = parse_data()
    
    count = 0
    for i in data:
        if i[0][0] <= i[1][1] and i[0][1] >= i[1][0]:
            count += 1
                
    print(count)
    

task_1()
task_2()