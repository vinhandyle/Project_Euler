# Day 12: Passage Pathing
# Part 1: 4659
# Part 2: 148962

INPUT = 'input_12.txt'

    
    
def run():
    d = get_input()
    p = find_all_paths(d, 'start', 'end')
    print(len(p))

    p = find_all_paths2(d, 'start', 'end')
    print(len(p))



def find_all_paths2(d, start, end):
    paths = set()
    def explore(path, cave, sp):
        # Alternative run where current cave can be duplicated
        if cave not in ('start', 'end') and \
           cave == cave.lower() and sp is None:
            explore(path, cave, cave)

        # Regular run
        new_path = path + [cave]
        if cave == end:
            paths.add(tuple(new_path))
        else:
            for ncave in d[cave]:
                if ncave not in path:
                    explore(new_path, ncave, sp)
                elif ncave == ncave.upper() or \
                     (ncave == sp and path.count(ncave) < 2):
                    explore(new_path, ncave, sp)
    explore([], start, None)
    return paths



def find_all_paths(d, start, end):
    paths = []
    def explore(path, cave):
        new_path = path + [cave]
        if cave == end:
            paths.append(new_path)
        else:
            for ncave in d[cave]:
                if ncave not in path:
                    explore(new_path, ncave)
                elif ncave == ncave.upper():
                    explore(new_path, ncave)
    explore([], start)
    return paths



def get_input():
    d = dict()
    with open(INPUT) as f:
        for line in f:
            c1, c2 = line.rstrip().split('-')
            if c1 not in d:
                d[c1] = set()
            if c2 not in d:
                d[c2] = set()
            d[c1].add(c2)
            d[c2].add(c1)
    return d



if __name__ == '__main__':
    run()
