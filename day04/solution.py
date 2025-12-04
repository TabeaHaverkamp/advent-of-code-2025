import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 


import itertools, math


def parse_input(file_path):
    with open(file_path, "r") as file:     
        data = [[
                    i for i in line.strip()
                ]for line in file]
    return data

directions = {"L": (0, -1), "R": (0,1), "U": (-1,0), "D": (1,0),
              "LU": (-1,-1) , "RU": (-1, 1), "LD": (1,-1), "RD":(1,1)
              }

paper = "@"
empty = "."


def check_neighbours(r,c, input):
    papers_in_neighbourhood = 0
    _directions = directions.copy()
    if r == 0:
        _directions.pop("U", None)
        _directions.pop("LU", None)
        _directions.pop("RU", None)
    if c == 0:
        _directions.pop("L", None)
        _directions.pop("LU", None)
        _directions.pop("LD", None)
    if r == len(input[0])-1:
        _directions.pop("D", None)
        _directions.pop("LD", None)
        _directions.pop("RD", None)
    if c == len(input)-1:
        _directions.pop("R", None)
        _directions.pop("RD", None)
        _directions.pop("RU", None)  
    for d in _directions.values():
        if input[r+d[0]][c+d[1]] in (paper):
            papers_in_neighbourhood +=1
    return papers_in_neighbourhood

@time_function
def solution1():
    access = 0
    input = parse_input("input.txt")
    for r_idx,row in enumerate(input):
        for c_idx, item in enumerate(row):
            if item == paper:
                if check_neighbours(r_idx, c_idx, input) < 4:
                    access += 1
    print(f"solution 1: {access}")


import time
@time_function
def solution2():
    access = 0
    input = parse_input("input.txt")
    while True:
        papers= []
        for r_idx,row in enumerate(input):
            for c_idx, item in enumerate(row):
                if item == paper:
                    if check_neighbours(r_idx, c_idx, input) < 4:
                        access += 1
                        papers.append((r_idx, c_idx))
        if len(papers) == 0:
            break
        for (r,c) in papers:
            input[r][c]=empty
            
    print(f"solution 2: {access}")
        

solution1()
solution2()