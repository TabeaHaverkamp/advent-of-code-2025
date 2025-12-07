import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 

from collections import deque


def parse_input(file_path):
    with open(file_path, "r") as file:     
        data = [line.strip() for line in file]
        splitters = []
        for row,(line) in enumerate(data):
            line = line.strip()
            for column,item in enumerate(line):
                if item == '^':
                    splitters.append((row,column))

    return data, splitters, (0,data[0].index('S'))

@time_function
def solution1():
    data, splitters, start = parse_input('input.txt')
    rays = set()
    rays.add(start[1])
    split_cnt = 0
    for row in range(1,len(data[0])):
        if splitters[0][0] == row: # if  are splitters in this row
            while len(splitters) > 0 and splitters[0][0]== row:
                spl = splitters.pop(0)[1]                
                if spl in rays:
                    if spl == 0:
                        rays.add(spl+1)
                    elif spl == len(data[0]):
                        rays.add(spl-1)
                    else: 
                        rays.add(spl+1)
                        rays.add(spl-1)
                    split_cnt+=1
                    rays.remove(spl)
    print(f"solution 1: {split_cnt}")
                


@time_function
def solution2():
    data, splitters, start = parse_input('input.txt')
    rays = set()
    rays.add(start[1])
    ray_counts = {start[1]:1}

    for row in range(1,len(data[0])):
        if splitters[0][0] == row: # if  are splitters in this row
            while len(splitters) > 0 and splitters[0][0]== row:
                spl = splitters.pop(0)[1]                
                if spl in rays:
                    incoming_cnt = ray_counts[spl]
                    ray_counts[spl]=0
                    if spl == 0:
                        ray_counts[spl+1] = ray_counts.get(spl+1,0) + incoming_cnt
                        rays.add(spl+1)
                    elif spl == len(data[0]):
                        rays.add(spl-1)
                        ray_counts[spl-1] = ray_counts.get(spl-1,0) + incoming_cnt

                    else: 
                        ray_counts[spl+1] = ray_counts.get(spl+1,0) + incoming_cnt
                        ray_counts[spl-1] = ray_counts.get(spl-1,0) + incoming_cnt
                        rays.add(spl+1)
                        rays.add(spl-1)
                    rays.remove(spl)
                    
    
    print(f"solution 2: {sum(ray_counts.values())}")

solution1()
solution2()



# 3106 too low