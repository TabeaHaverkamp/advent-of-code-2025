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

def check_neighbours(r,c, paper_set):
    papers_in_neighbourhood = 0
    for d in directions.values():
        if (r+d[0],c+d[1]) in paper_set:
            papers_in_neighbourhood +=1
    return papers_in_neighbourhood


@time_function
def solution1():
    access = 0
    input = parse_input("input.txt")
    papers = set()
    for r_idx,row in enumerate(input):
        for c_idx, item in enumerate(row):
            if item == paper:
                papers.add((r_idx, c_idx))
    
    for r, c in papers:
        if check_neighbours(r, c, paper_set=papers) < 4:
            access += 1
    print(f"solution 1: {access}")



import time
@time_function
def solution2():
    access = 0
    input = parse_input("input.txt")
    paper_list = set()
    for r_idx,row in enumerate(input):
            for c_idx, item in enumerate(row):
                if item == paper:
                    paper_list.add((r_idx, c_idx))

    while True:
        papers_to_remove = []
        for (r_idx, c_idx) in paper_list:
            if check_neighbours(r_idx, c_idx, paper_list) < 4:
                access += 1
                papers_to_remove.append ((r_idx,c_idx))
        if not papers_to_remove:
            break
        for coord in papers_to_remove:
            paper_list.remove(coord)
            
    print(f"solution 2: {access}")
        

solution1()
solution2()