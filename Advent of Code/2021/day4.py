# Day 4: Giant Squid
# Part 1: 33348
# Part 2: 8112

INPUT = 'input_4.txt'

class Board:
    def __init__(self, rows: [str]):
        self._rows = list(list(int(n) for n in filter(''.__ne__, r.split(' '))) for r in rows)
        self._cols = list(list(r[i] for r in self._rows) for i in range(len(rows)))
        self._unmarked = list(n for r in self._rows for n in r)

    def mark(self, val: int):
        self._val = val
        for i in range(5):
            if val in self._rows[i]:
                self._unmarked.pop(self._unmarked.index(val))

                j = self._rows[i].index(val)
                self._rows[i][j] = -1
                self._cols[j][i] = -1
                break
        
    def win(self) -> bool:
        return any(arr.count(-1) == 5 for arr in self._rows + self._cols)

    def score(self) -> int:
        return sum(self._unmarked) * self._val

    def print(self):
        print(self._val)
        for r in self._rows:
            print(' '.join(f'{n}' for n in r))
        print()



def p1(draws: [int], boards: [Board]) -> int:
    '''Returns the final score of the first winning board'''
    for d in draws:
        for b in boards:
            b.mark(d)
            if b.win():
                return b.score()



def p2(draws: [int], boards: [Board]) -> int:
    '''Returns the final score of the last winning board'''
    w_boards = []
    for d in draws:
        _boards = list(b for b in boards)
        for b in _boards:
            b.mark(d)
            if b.win():
                w_boards.append(b.score())
                boards.pop(boards.index(b))
    return w_boards[-1]


    
def run():
    i = get_input()
    print(p1(*i))
    #print(p2(*i))
    


def get_input() -> ([int], [Board]):
    '''Parses the input file and returns a string array'''
    draws, boards = [], []
    with open(INPUT) as f:
        draws = list(int(n) for n in f.readline().rstrip().split(','))
        b = []

        for line in f:
            if line.rstrip() == '':
                if b != []:
                    boards.append(Board(b))
                    b = []
                continue
            b.append(line.rstrip())
        boards.append(Board(b))
            
    return draws, boards



if __name__ == '__main__':
    run()
