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



def press_buttons_indicator(indicator, buttons):
    for b in buttons:
        indicator[b] = not indicator[b]
    return indicator

def press_buttons_joltage(joltage, buttons):
    for b in buttons:
        joltage[b] =  joltage[b]+1
    return joltage
    

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
        


import collections
@time_function
def solution2():
    i,all_buttons,j = parse_input('testinput.txt')
    button_presses = 0
    for _, buttons, joltages in zip(i,all_buttons,j):
        buttons = buttons[0]
        joltages_dict = {idx:i for idx, i in enumerate(joltages)}
        joltages_dict = {k: v for k, v in sorted(joltages_dict.items(), key=lambda item: -item[1])}
        buttons =  sorted(
            buttons,
            key=lambda sublist: tuple(value not in sublist for value in list(joltages_dict.keys()))
        )
        
        
        print(buttons, joltages_dict, joltages_dict.keys())
        counters ={}
        print("Testing !", buttons, joltages,joltages_dict)
        a = max(joltages)-1
        while joltages_dict != counters and a <= max(joltages)*len(joltages):
            a+= 1
            print('-- more comb!', a)
            for comb in itertools.combinations_with_replacement(buttons, a):
                #print(comb)
                # optimization: get the elements that are needed often first.
                counters = collections.Counter(itertools.chain.from_iterable(comb))
                if counters == joltages_dict:
                    print('.    solution!', a, comb, counters)
                    break # to break the while loop

        if counters != joltages_dict:          
            print('. no solution??')
                #print('  result', current_joltages)
            

        button_presses += a
    print(f"Solution 1: {button_presses}")
        

solution1()
solution2()