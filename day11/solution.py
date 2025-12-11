import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 



def parse_input(file_path):
    with open(file_path, "r") as file:     
        data = [line.strip() for line in file]
        parse = dict()
        for line in data:
            k, v = line.split(': ')
            parse[k] = v.split(' ')
        return parse
    



def dfs(current_node, end_node, paths, visited_set, include1 = None, include2 = None):

    #if we already had this combination, no need to re-calculate!
    if (current_node, end_node) in memo: 
        return memo[(current_node, end_node)]

    if  current_node == end_node: 
        visited_set.add(current_node)
        memo[(current_node, end_node)] = 1
        return 1
    count = 0
    if current_node not in visited_set:
        visited_set.add(current_node)

        for neighbor in paths.get(current_node, []):
            count += dfs(neighbor, end_node, paths, visited_set)
        
    memo[(current_node, end_node)] = count
    return count


@time_function
def solution1(current_node = 'you', end_node = 'out'):
    paths = parse_input('input.txt')
    print(f"Solution 1: {dfs(current_node, end_node, paths, set())}")
        



@time_function
def solution2():
    
    paths = parse_input('input.txt')
    # put the problem into sub-problems.

    # SVR -> DAC -> FFT -> OUT
    svr_dac = dfs('svr', 'dac', paths, set())
    # print('svr_dac:', svr_dac)

    dac_fft = dfs('dac', 'fft', paths, set())
    # print('dac_fft:', dac_fft)

    fft_out = dfs('fft', 'out', paths, set())
    # print('fft_out:', fft_out)


    #SVR -> FFT -> DAC -> OUT
    svr_fft = dfs('svr', 'fft', paths, set())
    # print('svr_fft:', svr_fft)

    fft_dac = dfs('fft', 'dac', paths, set())
    # print('fft_dac:', fft_dac)

    dac_out = dfs('dac', 'out', paths, set())
    # print('dac_out:', dac_out)
    print(f"Solution 2: {svr_dac*dac_fft*fft_out + svr_fft*fft_dac*dac_out}")

    
memo = {}
solution1()

#new global memo
memo = {}
solution2()
