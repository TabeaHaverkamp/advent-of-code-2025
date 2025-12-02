import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 
import itertools
def parse_input(file_path):
    with open(file_path, "r") as file:
        
        data = [[
                    list(map(int, elem.split('-'))) 
                    for elem in line.strip().split(',')
                ]for line in file]
    return data[0]

@time_function
def solution1():
    input = parse_input('input.txt')
    invalid_sum = 0
    for i,j in input:
        for test in range(i, j+1):

            test_str = str(test)
            if len(test_str)%2 == 0:
                a = test_str[0:len(test_str)//2]
                b = test_str[len(test_str)//2:]
                if a==b:
                    invalid_sum += test
    print(f"solution 1: {invalid_sum}")



@time_function
def solution2():
    def _chunkstring(string, length):
        return {string[0+i:length+i] for i in range(0, len(string), length)}


    input = parse_input('input.txt')
    invalid_sum = 0
    for i,j in input:
        for test in range(i, j+1):
            test_str = str(test)        
            for w in range(1, len(test_str)//2+1): # batches can max be half as long as the string
                if len(test_str)%w ==0: # the batches need to be even sized.
                    if len(_chunkstring(test_str, w))==1 :
                        invalid_sum+=test
                        break
    print(f"solution 2: {invalid_sum}")



@time_function
def solution2_fast():
    """
    Incredibly fast, wouldnt have been possible without gemini.
    """
    def _generatechunks(start, end, length,repeat):
        numbers = range(10**(length - 1), 10**length) 
        return  [int(str(n)*repeat) for n in numbers if start <= int(str(n)*repeat)  and int(str(n)*repeat) <= end]
    input = parse_input('input.txt')
    invalid_sum = 0

    for i,j in input:
        max_len = len(str(j))
        solutions = set()
        for block_len in range(1,(max_len//2)+1):
            for repeat in itertools.count(start=2):
                total_len = block_len * repeat
                if total_len > max_len:
                    break
                solutions.update(_generatechunks(i,j, block_len, repeat))
        invalid_sum += sum(solutions)
    print(f"solution 2: {invalid_sum}")


solution1()             
solution2()
solution2_fast()