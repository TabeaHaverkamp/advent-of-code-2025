import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 


import itertools

import collections
from collections import deque

@time_function
def parse_input(file_path):
    with open(file_path, "r") as file:     
        data = [line for line in file]
        indicators =  [line[1:].split(']')[0] for line in data]
        indicators = [[True   if l =='#' else False for l in line] for line in indicators]
        buttons =  [[[list(map( int, i[1:-1].split(','))) for i in l.split(' {')[0].strip().split(' ')] for l in line.strip().split(']')[1:]] for line in data]
        joltage =  [list(map(int, line.strip().split('{')[-1].split('}')[0].split(',') )) for line in data]
        return indicators, buttons, joltage



def press_buttons_indicator(indicator, buttons):
    for b in buttons:
        indicator[b] = not indicator[b]
    return indicator



@time_function
def solution1():
    # instead of turning on to setting, i am turning setting to off. same amount of steps.
    i,all_buttons,j = parse_input('input.txt')
    button_presses = 0
    for indicator, buttons, _ in zip(i,all_buttons,j):
        buttons = buttons[0] # some reason double list
        a = 0
        while any(indicator):
            a+= 1
            for comb in itertools.combinations(buttons, a):
                ind = indicator.copy()
                for button in comb:
                    ind = press_buttons_indicator(ind, button)
                if not any(ind):
                    indicator = ind # to break the while loop
                    break # to break the for loop
            

        button_presses += a
    print(f"Solution 1: {button_presses}")
        


@time_function
def solution2():
    def press_buttons_joltage(joltage, buttons):
        joltage = list(joltage)
        for b in buttons:
            joltage[b] =  joltage[b]-1
        return tuple(joltage)
    
    def bfs(joltage, buttons):
        q =  deque()
        visited_joltages = set()
        q.append((joltage, []))
        print('start: ', joltage)
        while len(q) > 0:
            (current_joltages, buttons_pressed) = q.popleft()
            for b in buttons:
                new_joltages = press_buttons_joltage(current_joltages, b)
                #print('. ', current_joltages,  new_joltages)
                if all(j == 0 for j in new_joltages): 
                    print("found it!", len(buttons_pressed) + 1)
                    return len(buttons_pressed) +1
                if tuple(new_joltages) not in visited_joltages and min(new_joltages)>=0:
                    new_buttons_pressed = buttons_pressed + [b]
                    visited_joltages.add(tuple(new_joltages))
                    q.append((new_joltages, new_buttons_pressed))
        return -1

       
       

    _,all_buttons,all_joltages = parse_input('input.txt')
    button_presses = 0
    for buttons, joltages in zip(all_buttons,all_joltages):
        buttons = buttons[0]
        button_presses += bfs(joltages, buttons)
    print(f"Solution 2: {button_presses}")

            
              

solution1()
solution2()