#day 1 2021 test code
import sys
import os

def parse_data():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
        data = f.read()
        f.close()
    return data

def main():
    task_1()
    task_2()

#12156
def task_1():
    dict = {
        "A": 1, #rock
        "B": 2, #paper
        "C": 3, #scissors
        "X": 1, #rock
        "Y": 2, #paper
        "Z": 3  #scissors
    }
    
    loss = ['AZ', 'BX', 'CY']
    win = ['AY', 'BZ', 'CX']
    tie = ['AX', 'BY', 'CZ']
    
    data = [x.replace(" ", "") for x in parse_data().split("\n")]
    
    score = 0
    for i in data:
        if i in tie:
            score += 3 + dict[i[1]]
        if i in win:
            score += 6 + dict[i[1]]
        if i in loss:
            score += dict[i[1]]

    print(score)

#10835
def task_2():
    dict = {
        "A": 1, #rock
        "B": 2, #paper
        "C": 3, #scissors
        "X": 1, #rock
        "Y": 2, #paper
        "Z": 3  #scissors
    }
    
    loss = ['AZ', 'BX', 'CY']
    win = ['AY', 'BZ', 'CX']
    tie = ['AX', 'BY', 'CZ']
    
    data = [x.replace(" ", "") for x in parse_data().split("\n")]
    
    score = 0
    for i in data:
        if dict[i[1]] == 1: #lose
            score += dict[loss[dict[i[0]] - 1][1]]
        if dict[i[1]] == 2: #draw
            score += 3 + dict[tie[dict[i[0]] - 1][1]]
        if dict[i[1]] == 3: #win
            score += 6 + dict[win[dict[i[0]] - 1][1]]
    print(score)
    
    
main()



