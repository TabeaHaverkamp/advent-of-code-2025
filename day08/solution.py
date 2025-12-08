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

#@time_function
def get_distances (coordinates):
    distances = dict()
    for c in range(len(coordinates)):
        for c2 in range(len(coordinates)):
            if c != c2:
                #distances are not directed, so no need to compute all again
                if not distances.get((c2,c)):
                    distances[(c,c2)] = distance(coordinates[c],coordinates[c2])
    return distances

def recursive_dfs(connection_dict, current_key, current_group,visited_set ):
    visited_set.add(current_key)
    current_group.append(current_key)
    for value in connection_dict.get(current_key, set()):
        if value in connection_dict.keys() and value not in visited_set:
            if value not in visited_set:
                recursive_dfs(connection_dict, value, current_group,visited_set)

def union(node_a, node_b, parent, size):
    def get_root(node):
        if parent[node] == node:
            return node
        parent[node] = get_root(parent[node])
        return parent[node]
    root_a = get_root(node_a)
    root_b = get_root(node_b)
    
    if root_a != root_b:
        # Optimization: Merge the smaller tree into the larger tree
        if size[root_a] < size[root_b]:
            parent[root_a] = root_b
            size[root_b] += size[root_a]
        else:
            parent[root_b] = root_a
            size[root_a] += size[root_b]
        return True # The sets were merged
    return False # The sets were already connected


@time_function
def solution1():
    input_type = 'input'
    if input_type == 'testinput':
        connection_cnt = 10
    else:
        connection_cnt = 1000
    coordinates = parse_input(f'{input_type}.txt')
    distances = get_distances(coordinates)

    # get all minimum connections, so we can build nets later on
    connections = dict()
    for _ in range(connection_cnt):
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
    



@time_function
def solution2():
    coordinates = parse_input('input.txt')

    # get distances to each node
    distances = get_distances(coordinates)
   
    first_group_size = 0
    connections = dict()
    last_added_coord = tuple()
    while  first_group_size < len(coordinates) :
        # get all minimum connections, so we can build nets later on
        min_dist = min(distances.values())
        result = [k for k, v in distances.items() if v == min_dist] 

        for (x,y)  in result:
            if x in connections.keys():
                connections[x].add(y)
            else: connections[x] = {y}
            
            if y in connections.keys():
                connections[y].add(x)
            else:
                connections[y] = {x}

            distances.pop((x,y))
            last_added_coord = (coordinates[x],coordinates[y])

        all_groups = []
        visited = set()
        for node in connections.keys():
            if node not in visited:
                current_group = []
                recursive_dfs(connections, node, current_group, visited)
                all_groups.append(current_group)
        first_group_size = len(all_groups[0])

    print(f"Solution 2: {last_added_coord[0][0]* last_added_coord[1][0]}")



@time_function
def solution1_fast():
    """
    The fast approach uses DSU instead of DFS.
    """
    input_type = 'input'
    if input_type == 'testinput':
        connection_cnt = 10
    else:
        connection_cnt = 1000
    coordinates = parse_input(f'{input_type}.txt')

    # get distances to each node
    distances = get_distances(coordinates)
    
    parent = {i: i for i in range(len(coordinates))}
    size = {i: 1 for i in range(len(coordinates))}

    group_count = len(coordinates)
    sorted_connections = sorted(distances.items(), key=lambda item: item[1]) # sort asc by distance.

    for _ in range(connection_cnt):
        ((x,y),_) = sorted_connections.pop(0)
        if union(x, y,parent, size):
            group_count -= 1 # Only decrease count if a merge (union) happened

    sorted_size = sorted(size.items(), key=lambda item: item[1]) # sort asc by distance.
    biggest_groups = [i[1] for i in sorted_size[-3:]]
    print(f"Solution 1, fast: {math.prod(biggest_groups)} ")
    


@time_function
def solution2_fast():
    """
    The fast approach uses DSU instead of DFS and has the minimum calculation outside of the loop.
    """
    coordinates = parse_input('input.txt')

    # get distances to each node
    distances = get_distances(coordinates)
    
    parent = {i: i for i in range(len(coordinates))}
    size = {i: 1 for i in range(len(coordinates))}

    group_count = len(coordinates)
    last_added_coord = tuple()
    sorted_connections = sorted(distances.items(), key=lambda item: item[1]) # sort asc by distance.

    while  group_count > 1 :
        ((x,y),_) = sorted_connections.pop(0)
        if union(x, y,parent, size):
            group_count -= 1 # Only decrease count if a merge (union) happened
        last_added_coord = (coordinates[x],coordinates[y])

    print(f"Solution 2, fast: {last_added_coord[0][0]* last_added_coord[1][0]}")


    




solution1()
solution2()
solution1_fast()
solution2_fast()