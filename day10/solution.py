import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 


import itertools, math, collections

@time_function
def parse_input(file_path):
    with open(file_path, "r") as file:     
        data = [line for line in file]
        indicators =  [line[1:].split(']')[0] for line in data]
        indicators = [[True   if l =='#' else False for l in line] for line in indicators]
        buttons =  [[[list(map( int, i[1:-1].split(','))) for i in l.split(' {')[0].strip().split(' ')] for l in line.strip().split(']')[1:]] for line in data]
        joltage =  [list(map(int, line.strip().split('{')[-1].split('}')[0].split(',') )) for line in data]
        return indicators, buttons, joltage



def press_buttons(indicator, buttons):
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
        while a < 10 and  any(indicator):
            a+= 1
            lights_on = [i for i, e in enumerate(indicator) if e == True]
            for comb in itertools.combinations(buttons, a):
                ind = indicator.copy()
                for button in comb:
                    ind = press_buttons(ind, button)
                if not any(ind):
                    indicator = ind # to break the while loop
                    break # to break the for loop
            

        button_presses += a
    print(f"Solution 1: {button_presses}")
        


solution1()