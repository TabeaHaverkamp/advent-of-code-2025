
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




def solution2():
    def _chunkstring(string, length):
        return list(string[0+i:length+i] for i in range(0, len(string), length))


    input = parse_input('input.txt')
    invalid_sum = 0
    for i,j in input:
        for test in range(i, j+1):
            test = str(test)
            window_max_length =len(test)//2

            for w in range(1, window_max_length+1):
                chunks = _chunkstring(test, w)
                set_chunks = set(chunks)
                if ((len(chunks)>2 and len(set_chunks)==1) 
                    or (len(chunks)<=2 and chunks[0]==chunks[1])
                ):
                    invalid_sum+=int(test)
                    break
    print(invalid_sum)


                
solution2()