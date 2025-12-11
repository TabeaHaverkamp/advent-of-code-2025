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
    k = (current_node, frozenset(visited_set))
    if  k in memo: return memo[k]
    if current_node in visited_set: 
        memo[k] = 0
        return 0
    if  current_node == end_node: 
        if (include1 is  None or include1 in visited_set) and (include2 is None or include2 in visited_set):
            memo[k] = 1
            return 1
        else:
            memo[k] = 0
            return 0
    count = 0 
    visited_set.add(current_node)

    for p in paths.get(current_node, []):
        count += dfs(p, end_node, paths, visited_set,include1, include2)
    visited_set.remove(current_node)
    
    memo[k] = count
    return count


@time_function
def solution1(current_node = 'you', end_node = 'out'):
    paths = parse_input('input.txt')

    print(f"Solution 1: {dfs(current_node, end_node, paths, set())}")
        



@time_function
def solution2():
    
    paths = parse_input('input.txt')
       
    memo = {}
    print('testing..')
    test = dfs('svr', 'out', paths,set(), include1='dac', include2='fft')
    print('test solution 2:', test)
    return
    # get SVR -> DAC -> FFT -> OUT

    print('dac -> fft without svr')
    p = paths.copy()
    p.pop('svr')
    s = set()
    fac_fft = dfs('dac', 'fft', p, s)


    if fac_fft > 0:
        print('fft -> out without dac')
        p = paths.copy()
        p.pop('dac')
        s = set()
        fft_out = dfs('fft', 'out', p, s)

        print('svr -> dac without fft')
        p = paths.copy()
        p.pop('fft')
        s = set()
        svr_dac = dfs('svr', 'dac', p,[],s)

        #combine(possible_paths_svr_dac, possible_paths_dac_fft, possible_paths_fft_out, final_paths)


    print('fft -> dac without svr ')
    p = paths.copy()
    p.pop('svr')
    s = set()
    fft_dac = dfs('fft', 'dac', p, s)
    print(fft_dac)

    print('dac -> out without fft')
    p = paths.copy()
    p.pop('fft')
    s = set()
    dac_out = dfs('dac', 'out', p,s)
    print(dac_out)
    

    print('svr -> fft without dac')
    p = paths.copy()
    p.pop('dac')
    s= set()
    svr_fft = dfs('svr', 'fft', p,s)
    print(svr_fft)


    #combine(possible_paths_svr_fft, possible_paths_fft_dac, possible_paths_dac_out, final_paths)
        




    print(possible_paths_svr_dac)
    print(possible_paths_dac_fft)
    print(possible_paths_fft_out)
    print('---')
    print(possible_paths_svr_fft)
    print(possible_paths_fft_dac)
    print(possible_paths_dac_out)


    # find the intersections for the paths without double


    print('--')
    for a in final_paths: print(a)

    




memo = {}
solution1()
print(memo)
memo = {}
solution2()


#dac -> out without fft
# 12215