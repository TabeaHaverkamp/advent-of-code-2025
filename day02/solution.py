
def parse_input(file_path):
    with open(file_path, "r") as file:
        
        data = [[
                    list(map(int, elem.split('-'))) 
                    for elem in line.strip().split(',')
                ]for line in file]
    return data[0]

def solution1():
    input = parse_input('input.txt')
    invalid_sum = 0
    for i,j in input:
        for test in range(i, j+1):
            test = str(test)
            if len(test)%2 == 0:
                a =  test[0:len(test)//2]
                b = test[len(test)//2:]
                if a==b:
                    invalid_sum += int(a+b)
    return invalid_sum




solution1()