import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 


import itertools, math, collections

def parse_input(file_path):
    with open(file_path, "r") as file:     
        return [tuple(map(int,line.split(","))) for line in file]
    

@time_function
def solution1():
    """
    O(N**2) notation, but hey it works still fast
    """
    tiles = parse_input('input.txt')
    max_area = 0

    for (t1,t2) in itertools.combinations(tiles, 2):
        x = abs(t2[0] - t1[0]) + 1
        y = abs(t1[1] - t2[1])+1
        area = abs(x)*abs(y)
        if area > max_area:
            max_area = area
    
    print(f"solution1 : {max_area}")



def visualise(tiles, green, red):
    #visualise
    max_x = max(tiles, key=lambda item: (item[0]))[0]+1
    max_y = max(tiles, key=lambda item: (item[1]))[1]+1
    matrix = [['.' for _ in range(max_x+1)] for _ in range(max_y+1)]
    for (x,y) in green:
        matrix[y][x] = 'X'
    for (x,y) in red:
        matrix[y][x] = '#'
    return matrix


directions = {'U': (-1, 0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
@time_function
def solution2():

    def fill_area(border):
        #fill the area with green tiles
        # 1. Map all X coordinates to their respective Y rows (O(N))
        # { y: [x1, x2, x3, ...] }
        y_to_x_map = collections.defaultdict(set)
        for x, y in border:
            y_to_x_map[y].add(x)
        # 2. Determine the overall vertical bounds
        all_y_coords = y_to_x_map.keys()
        min_y = min(all_y_coords)
        max_y = max(all_y_coords)
        interior_set = set()

        # 3. Iterate through every row (y) within the bounding box
        for y in range(min_y, max_y + 1):
            if y not in y_to_x_map:
                continue
               
            x_boundaries = sorted(list(y_to_x_map[y]))
            x_0 = x_boundaries[0]
            for x in x_boundaries[1:]:
                for i in range(x-x_0+1):
                    interior_set.add((x_0+i,y))
                x_0 = x

        return interior_set



    tiles = parse_input('input.txt')

    # get the red/green tiles for borders
    green_tiles = set()
    red_tiles = set(tiles)
    first_tile = tiles[0]
    tiles.append(tiles[0])
    for tile in tiles[1:]:      
        min_x = min(first_tile[0], tile[0])      
        min_y = min(first_tile[1], tile[1])     
        for i in range(abs(tile[0]- first_tile[0])):
            green_tiles.add((min_x +i, min_y))
        for i in range(abs(tile[1]- first_tile[1])):
            green_tiles.add((min_x, min_y+i))
        first_tile = tile
    print('borders done!')
    #green_tiles = fill_area(red_tiles | green_tiles)
    #print('filled!')


    max_area = 0
    max_area_tuples = []
    for (t1,t2) in itertools.combinations(red_tiles, 2):
        x = abs(t2[0] - t1[0]) + 1
        y = abs(t1[1] - t2[1])+1
        area = abs(x)*abs(y)
        if area > max_area:
            # at least in total 3 green tile around the red tiles      
            green_t1 = 0
            green_t2 = 0
            t1_d = []
            t2_d = []
            if t1[0] < t2[0]: 
                t1_d.append(directions['R'])
                t2_d.append(directions['L'])
            else:
                t1_d.append(directions['L'])
                t2_d.append(directions['R'])

            if t1[1] < t2[1]: 
                t1_d.append(directions['U'])
                t2_d.append(directions['D'])
            else:
                t1_d.append(directions['D'])
                t2_d.append(directions['U'])   


            for d in t1_d:
                if (t1[0]+ d[0], t1[1] + d[1]) in green_tiles:
                    green_t1 += 1
            for d in t2_d:
                if (t2[0]+ d[0], t2[1] + d[1]) in green_tiles:
                    green_t2 += 1
            if green_t1 + green_t2 >=3:
                print('possible:', t1,t2, area)
                # make a set of all indexes that are described by t1,t2.
                subset = set()
                subset.add(t1)
                subset.add(t2)
                min_x = min(t1[0],t2[0])
                max_x = max(t1[0],t2[0])
                min_y = min(t1[1],t2[1])
                max_y = max(t1[1],t2[1])
                for x in range(abs(t1[0]-t2[0])):
                    subset.add((min_x+x,min_y))
                    subset.add((min_x+x,max_y))
                for y in range(abs(t1[1]-t2[1])):
                    subset.add((min_x,min_y+y))
                    subset.add((max_x,min_y+y))
                
                subset = fill_area(subset)

                # check if that set is a real subset of red|green
                if subset <= red_tiles | green_tiles:
                        max_area = area
                        max_area_tuples = [t1, t2]
        
    print('---')
    print(max_area, max_area_tuples)



      


solution1()
solution2()