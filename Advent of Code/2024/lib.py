def read_input(path):
    arr = []
    with open(path) as f:
        for line in f:
            arr.append(line.rstrip())
    return arr



def log(path, data):
    with open(path, 'w') as f:
        f.write(data)



def print_matrix(m):
    return '\n'.join(''.join(str(i) for i in line) for line in m)