import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 


import itertools, math

def transpose(m): 
     return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
def parse_input(file_path):
    with open(file_path, "r") as file:     
        data = [line.replace("\n", "") for line in file]
        agg_idx = [i for i, ltr in enumerate(data[-1]) if ltr != ' ']
        agg = data[-1].split()
    return data[:-1], agg, agg_idx


@time_function
def solution1():
    data, agg, _ = parse_input('input.txt')
    data= transpose([[int(i.strip()) for i in line.split() ]for line  in data[:-1]])
    cnt = 0
    for d, a in zip(data, agg):
        if a == '*':
            cnt += math.prod(d)
        elif a == '+':
            cnt += sum(d)
    print(f"solution1: {cnt}")




@time_function
def solution2():
    data,agg, agg_idx = parse_input('input.txt')
    m =  [[0 for _ in range(len(agg))] for _ in range(len(data))]
    cnt = 0
    for r_idx, row in enumerate(data):
        prev = 0
        for c_idx, a_idx in enumerate(agg_idx[1:]):
            m[r_idx][c_idx] = (row[prev:a_idx])
            prev = a_idx
        m[r_idx][c_idx+1] = (row[a_idx:])
    

    for col, a  in zip(transpose(m), agg):
        #col = col[::-1]
        number_len = len(col[0])
        numbers = []
        for i in range(number_len-1, -1, -1):
            new_number =''
            for number in col:
                if number[i] !=' ':
                    new_number += number[i]
            if len(new_number)>0:
                numbers.append(int(new_number))
        if a == '*':
            cnt += math.prod(numbers)
        elif a == '+':
            cnt += sum(numbers)
    print(f"solution 2: {cnt}")
        
    

solution1()
solution2()