#day 1 2021 test code
import sys
import os
import re

def parse_data():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        #read line by line
        data = f.read()
        f.close()
        crane = [y.split(" ") for y in [x.replace("]", "").replace("[","") for x in [str(x[3:]) for x in [x.split("\n") for x in data.split("\n\n")][0]]]]
        data = data.split("\n\n")[1].split("\n")
        lines = []
        for line in data:
            if "move" in line:
                regex = re.search("move (\d+) from (\d+) to (\d+)", line)
                lines.append((int(regex.group(1)), int(regex.group(2)), int(regex.group(3))))
    return crane, lines

def task_1():
    crane, lines = parse_data()
    
    for line in lines:
        i = line[0]
        while i > 0:
            itm = crane[line[1]-1].pop()
            crane[line[2]-1].append(itm)
            i -= 1
            
    print("".join(line[-1] for line in crane))
    
    
def task_2():
    crane, lines = parse_data()
    
    for line in lines:
        itm = crane[line[1]-1][-line[0]:]
        del crane[line[1]-1][-line[0]:]
        crane[line[2]-1].extend(itm)     

    print("".join(line[-1] for line in crane))

task_1()
task_2()