#day 1 2021 test code
import sys
import os

class Folder:
    def __init__(self, name: str, parent, size=None):
        self.name = name
        self.sub_folders = []
        self.parent = parent
        self.size = size if size else 0

    def add_folder(self, folder):
        self.sub_folders.append(folder)

    def add_size(self, size: int):
        self.size += size
        if self.parent:
            self.parent.add_size(size)
    
    def __str__(self):
        return f"{self.name} {self.size}"
    
def parse_data():
    with open(os.path.join(sys.path[0], "test.txt"), "r") as f:
        data = f.read()
        f.close()
    return data


def task_1():
    data = parse_data().split("\n")
    data = [x for x in data if x != '$ ls']
        
    working_dir = Folder('root', None)
    root = working_dir
    
    for i in range(1, len(data)):
        input = data[i].split(" ")
        if input[1] == 'cd':
            if input[2] == '..':
                if working_dir.parent:
                    working_dir = working_dir.parent
            else:
                for folder in working_dir.sub_folders:
                    if folder.name == input[2]:
                        working_dir = folder
                        break
        elif(input[0] == 'dir'):
            working_dir.add_folder(Folder(input[1], working_dir))
        elif input[0].isnumeric():
            working_dir.add_size(int(input[0]))

def get_sums(workingDir):
    if workingDir.sub_folders:
        for i in workingDir.sub_folders:
            if workingDir.size <= 10_000:
                
        
def task_2():
    pass

task_1()
task_2()