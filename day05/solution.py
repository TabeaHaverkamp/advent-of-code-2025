import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 


import itertools, math


def parse_input(file_path):
    with open(file_path, "r") as file:     
        data = [line.strip() for line in file]
        ranges = [tuple(map(int,r.split("-"))) for r in data[:data.index("")]]
    return ranges, [int(i) for i in data[data.index("")+1:]]

@time_function
def solution1():
    ranges_input, ingredients = parse_input("input.txt")

    fresh_cnt = 0
    for i in ingredients:
        for a,b in ranges_input:
            if i in range(a,b+1): 
                fresh_cnt+=1
                break
    print(f"solution 1: {fresh_cnt}")



import math
@time_function
def solution2():
    ranges_input, _ = parse_input("input.txt")
    ranges_input.sort()
    current_max = ranges_input[0][1]
    current_start = ranges_input[0][0]
    small_ranges = []
    cnter = 0
    for a,b in ranges_input[1:]:
        if current_max +1 < a:
            small_ranges.append((current_start, current_max))
            cnter += current_max - current_start +1
            current_start = a 
            current_max = b
        else: 
            current_max = max(b, current_max)

    cnter += current_max - current_start +1
   
    print(f"solution 2: {cnter}")
solution1()
solution2()