import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 


import itertools, math

def parse_input(file_path):
    with open(file_path, "r") as file:     
        return [tuple(map(int,line.split(","))) for line in file]
    

@time_function
def solution1():
    tiles = parse_input('input.txt')
    max_area = 0

    for (t1,t2) in itertools.combinations(tiles, 2):
        x = abs(t2[0] - t1[0]) + 1
        y = abs(t1[1] - t2[1])+1
        area = abs(x)*abs(y)
        if area > max_area:
            max_area = area
    
    print(f"solution1 : {max_area}")

solution1()



# 2282848362 too low