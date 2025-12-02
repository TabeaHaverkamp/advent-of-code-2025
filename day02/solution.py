import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if project_root not in sys.path: sys.path.append(project_root)
from utils.utils import time_function 
import itertools, math
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
    This is ridicioulus. How do people think this way!?
    """
    input = parse_input('input.txt')
    invalid_sum = 0

    for start_val, end_val in input:
        max_len = len(str(end_val))
        solutions = set()
        for block_len in range(1,(max_len//2)+1):
            for repeat in itertools.count(start=2):
                total_len = block_len * repeat
                if total_len > max_len:
                    break

                #  Calculate the Multiplier (The structure of the repeating number)
                # This is faster, instead of doing str(block)*repeat
                multiplier_str = '1'
                for _ in range(1, repeat):
                    multiplier_str += '0' * (block_len - 1) + '1'
                multiplier = int(multiplier_str)

                min_base = 10**(block_len - 1)
                max_base = 10**block_len- 1

                start_p = max(min_base,  math.ceil(start_val / multiplier))
                end_p = min(max_base, math.floor(end_val / multiplier))
                # Generate and store the invalid IDs
                # This loop now iterates only over the handful of test values 
                # that *might* produce a match.
                if start_p <= end_p:
                    for block in range(start_p, end_p + 1):
                        ID_int = block * multiplier
                        # Since the start_p and end_p bounds are highly accurate,
                        # the final check is mostly just confirming the bounds were tight.
                        if ID_int >= start_val and ID_int <= end_val:
                            solutions.add(ID_int)
        invalid_sum += sum(solutions)
    print(f"solution 2: {invalid_sum}")


solution1()             
solution2()
solution2_fast()