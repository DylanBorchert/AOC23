#day 1 2021 test code
import sys
import os

def parse_data():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        data = f.read()
        f.close()
    return data

def task_1():
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    data = parse_data().split("\n")
    sum = 0
    #spit string in half 
    for i in data:
        first_half = i[:len(i)//2]
        second_half = i[len(i)//2:]
        
        for char in first_half:
            if char in second_half:
                sum += letters.index(char)+1
                break;
    print(sum)

    
def task_2():
    
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    data = parse_data().split("\n")
    
    sum = 0
    for i in range(0, len(data), 3):
        first = data[i]
        second = data[i+1]
        third = data[i+2]
        #print(first, second, third)
        for char in first:
            if char in second and char in third:
                sum += letters.index(char)+1
                break;
    print(sum)

task_1()
task_2()