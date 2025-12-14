import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 



def parse_input(file_path):
    with open(file_path, "r") as file:     
        data = [d.split('\n') for d in ''.join([l for l in file]).split('\n\n')]
        presents = [[list(map(int, d.split(':')[0].split('x'))), list(map(int,d.split(': ')[1].split(' ')))]  for d in data[-1]]
        shapes = {int(d[0].split(':')[0]): d[1:] for d in data[:-1]}
        shapes_space_cnt ={k: sum([1
                            for _, row in enumerate(v)         
                            for _, char in enumerate(row)     
                            if char == '#'] )                      
                        for k, v in shapes.items()}     
                        
        return presents,shapes_space_cnt

@time_function
def solution1():
    presents,shapes_space_cnt = parse_input('input.txt')

    fitted_count = 0
    """
    For some reason, it was enough to check if it would THEORETICALLY fit.
    This did not work for the test input, but was enough for the real input.
    """
    for shape, present_list in presents:
        free_spots = shape[1] * shape[0]
        present_spot_cnt = 0
        for p_idx, p_cnt in enumerate(present_list):
            present_spot_cnt += p_cnt * shapes_space_cnt[p_idx]
        if present_spot_cnt <= free_spots: fitted_count +=1

    print(f'Solution1: {fitted_count}')


solution1()