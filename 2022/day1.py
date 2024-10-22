#day 1 2021 test code
import sys
import os

def get_data():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        data = f.read()
    return [[int(x) for x in x.split("\n")] for x in data.split("\n\n")]

def task_1():
    print(max([sum(x) for x in get_data()]))

def task_2():
    print(sum(sorted([sum(x) for x in get_data()], reverse=True)[:3]))

task_1()
task_2()
