import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 


import itertools, math


def parse_input(file_path):
    with open(file_path, "r") as file:     
        data = [[
                    int(i) for i in line.strip()
                ]for line in file]
    return data

@time_function
def solution1():
    s = 0
    input = parse_input('input.txt')
    for battery in input:
        first = max(battery[:-1])
        battery = battery[battery.index(first)+1:]
        second = max(battery)
        s += int(first*10 + second)
    print(f"Solution 1: {s}")



@time_function
def solution2():
    s = 0
    input = parse_input('input.txt')
    for battery in input:
        found_batteries = []
        for i in range (11,-1,-1):
            if i > 0:
                search_space = battery[:-i]
            else: search_space = battery
            b = max(search_space)
            battery = battery[battery.index(b)+1:]
            found_batteries.append(b)
        s+= int(''.join(map( str,found_batteries)))


    print(f"solution 2: {s}")


solution1()
solution2()