import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 


import itertools, math

def transpose(m): 
     return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
def parse_input(file_path):
    with open(file_path, "r") as file:     
        data = [line.strip() for line in file]
        agg = data[-1].split()
        data = transpose([[int(i.strip()) for i in line.split() ]for line  in data[:-1]])
    return data, agg 


@time_function
def solution1():
    data, agg = parse_input('input.txt')
    cnt = 0
    for d, a in zip(data, agg):
        if a == '*':
            cnt += math.prod(d)
        elif a == '+':
            cnt += sum(d)
    print(f"solution1: {cnt}")


def parse_input2(file_path):
    with open(file_path, "r") as file:     
        data = [line for line in file]
        agg = data[-1].split()
        data   = data[:-1]
        data = [[line[i:i+len(agg)].replace("\n", "") for i in range(0, len(line), len(agg))] for line in data]
    return data, agg 

@time_function
def solution2():
    data, agg = parse_input2('testinput.txt')
    for l in data: print(l)

    print('---')

    for l in transpose(data): print(l)
    
    print('---')
    agg = agg[::-1]
    for l in transpose(data):
        cnt = 0
        # check if the first thing is only empty
        only_empty = True
        for number in l:
            number = number[::-1]
            if number != ' ':
                only_empty = False
            
        if only_empty:
            l = [item[:-1] for item in l]
        l = l[::-1]
        print("line: ", l)
        numbers = []
        # go through every line. build the numbers by adding the columns on top of each other
        for c in range(len(l[0])):
            current_number = 0
            number_cnt = 0
            for number in l:
                number = number[::-1]
                if number[c] != ' ':
                    current_number += (10**number_cnt) * int(number[c])
                    #print(".  ", number[c], current_number)
                    number_cnt+=1
            numbers.append(current_number)
        print(numbers)
        if agg[c] == '*':
            numbers.remove(0)
            cnt += math.prod(numbers)
            print('mul!', math.prod(numbers))
        elif agg[c] == '+':
            cnt += sum(numbers)
            print("sum, ", sum(numbers))
    print(f"solution2: {cnt}")


solution2()