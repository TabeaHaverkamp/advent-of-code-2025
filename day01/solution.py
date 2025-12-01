
def parse_input(file_path):
    with open(file_path, "r") as file:
        data = [line.strip() for line in file]
    return [[l[0], int(l[1:])] for l in data]

orient_mapper = {'L': -1, 'R': 1}

def solution_1():
    input = parse_input('input.txt')
    cnt = 0
    status = 50
    for orient, number in input:
        status = (status + orient_mapper[orient] * number) %100
        if status == 0:
            cnt += 1
    print(f"Solution part 1: {cnt}")



def solution_2():
    input = parse_input('input.txt')
    cnt = 0
    status = 50
    for orient, number in input:

        #no matter what, if bigger than 100 it def turns.
        cnt += int(number/100)
        number = number %100
                
        if ((status + orient_mapper[orient] * number) <=0 
        or (status + orient_mapper[orient] * number) >=100
        ) and status != 0:

            cnt += 1

        status =  (status + orient_mapper[orient] * number) %100

    print(f"Solution part 2: {cnt}")




solution_1()
solution_2()