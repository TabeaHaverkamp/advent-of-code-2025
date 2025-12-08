import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 


import itertools, math

def parse_input(file_path):
    with open(file_path, "r") as file:     
        return [tuple(map(int,line.split(","))) for line in file]

def distance(point1, point2):
    return math.sqrt(pow(point1[0]-point2[0], 2)
                    + pow(point1[1]-point2[1], 2)
                    + pow(point1[2]-point2[2], 2))

@time_function
def solution1():

    input_type = 'input'
    if input_type == 'testinput':
        connection_cnt = 10
    else:
        connection_cnt = 1000
    coordinates = parse_input(f'{input_type}.txt')
    distances = dict()
    for c in range(len(coordinates)):
        for c2 in range(len(coordinates)):
            if c != c2:
                #distances are not directed, so no need to compute all again
                if not distances.get((c2,c)):
                    distances[(c,c2)] = distance(coordinates[c],coordinates[c2])


    # get all minimum connections, so we can build nets later on
    connections = dict()
    for i in range(connection_cnt):
        min_dist = min(distances.values())
        result = [k for k, v in distances.items() if v == min_dist] 
        for i in result:
            (x,y)  = i
            if x in connections.keys():
                connections[x].add(y)
            else: connections[x] = {y}
            
            if y in connections.keys():
                connections[y].add(x)
            else:
                connections[y] = {x}

            distances.pop(i)

    
    def recursive_dfs(connection_dict, current_key, current_group,visited_set ):
        visited_set.add(current_key)
        current_group.append(current_key)
        for value in connection_dict.get(current_key, set()):
            if value in connection_dict.keys() and value not in visited_set:
                if value not in visited_set:
                    recursive_dfs(connection_dict, value, current_group,visited_set)
    
    all_groups = []
    visited = set()
    for node in connections.keys():
        if node not in visited:
            current_group = []
            recursive_dfs(connections, node, current_group, visited)
            all_groups.append(current_group)
    group_size = [len(group) for group in all_groups]
    group_size.sort()
    print(f"Solution 1: {math.prod(group_size[-3:])}")
    




solution1()
