# Day 10: Syntax Scoring
# Part 1: 296535
# Part 2: 4245130838

INPUT = 'input_10.txt'


def get_corrupted(lines: [str]) -> int:
    '''Removes the corrupted lines from the list and returns their score'''
    illegal = {'(': 3, '[': 57, '{': 1197, '<': 25137}
    close = {')': '(', ']': '[', '}': '{', '>': '<'}
    score = 0
    l = list(lines)
    
    for line in l:
        stack = []
        for c in line:
            if c not in close:
                stack.append(c)
            else:
                if close[c] == stack[-1]:
                    stack.pop(-1)
                else:
                    score += illegal[close[c]]
                    lines.pop(lines.index(line))
                    break
    return score



def get_incomplete(lines: [str]) -> int:
    illegal = {')': 1, ']': 2, '}': 3, '>': 4}
    open = {'(': ')', '[': ']', '{': '}', '<': '>'}
    close = {v: k for k, v in open.items()}
    scores = []

    for line in lines:
        score = 0
        stack = []
        for c in line:
            if c in open:
                stack.append(c)
            elif close[c] == stack[-1]:
                stack.pop(-1)
        complete = [open[c] for c in stack[::-1]]
        for c in complete:
            score *= 5
            score += illegal[c]
        scores.append(score)
    return sorted(scores)[len(scores) // 2]



def run():
    i = get_input()
    print(get_corrupted(i))
    print(get_incomplete(i))



def get_input() -> [int]:
    '''Parses the input file and returns a string array'''
    arr = []
    with open(INPUT) as f:
        for line in f:
            arr.append(line.rstrip())
    return arr



if __name__ == '__main__':
    run()
