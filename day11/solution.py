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
    

@time_function
def solution1(current_node = 'you', end_node = 'out'):
    paths = parse_input('input.txt')

    def dfs(current_node, end_node, paths,current_path, possible_paths):
        current_path.append(current_node)
        if current_node == end_node:
            possible_paths.append(current_path.copy())
        for p in paths.get(current_node, []):
            if p not in current_path:
                dfs(p, end_node, paths, current_path,possible_paths)
        current_path.pop()

    possible_paths = []

    dfs(current_node, end_node, paths, [], possible_paths)
    print(f"Solution 1: {len(possible_paths)}")
        



@time_function
def solution2():
    paths = parse_input('input.txt')

    def dfs(current_node, end_node, paths, visited_set, include1 = None, include2 = None):
        if current_node in visited_set: return 0
        if  current_node == end_node: 
            if (include1 is  None or include1 in visited_set) and (include2 is None or include2 in visited_set):
                return 1
            else:
                return 0

        count = 0 
        visited_set.add(current_node)

        for p in paths.get(current_node, []):
            count += dfs(p, end_node, paths, visited_set,include1, include2)
        visited_set.remove(current_node)

        return count

    def combine (p1, p2, p3, final_paths):

        # Combine the segments (Concatenation)
        for path1 in p1:
            for path2 in p2:
                # Check for illegal cycle (nodes in path2 cannot be in path1, except R1)
                # path1 set includes all nodes EXCEPT the last one (R1)
                path1_set_no_end = set(path1[:-1]) 
                overlap = path1_set_no_end.intersection(set(path2[1:]))
                if overlap: continue

                # We need the full set of nodes from the start of the chain (path1 + path2 without duplicates)
                # full_base_set = set(path1[:-1]) | set(path2[1:-1])
                full_base_set = path1_set_no_end.union(set(path2[1:-1]))
                for path3 in p3:
                    
                    # Check against nodes in path3 (excluding R2)
                    overlap_full = full_base_set.intersection(set(path3[1:]))
                    if overlap_full: continue
                    
                    final_paths.append(path1 + path2[1:] + path3[1:])
        

    possible_paths_fft_dac = 0
    possible_paths_dac_fft = 0
    possible_paths_fft_out = 0
    possible_paths_svr_dac = 0
    possible_paths_dac_out = 0
    possible_paths_svr_fft = 0
    final_paths = []

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

    





solution1()
solution2()


#dac -> out without fft
# 12215