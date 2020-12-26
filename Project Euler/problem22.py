# Problem 22: Names scores
# Answer: 871198282

from pathlib import Path

INPUT = Path('problem22.txt')

def run() -> None:
    names = _get_names()
    names.sort()
    sum = 0

    for index in range(len(names)):
        sum += (index + 1) * _name_score(names[index])

    print(sum)



def _name_score(s: str) -> int:
    name_scores = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
                   'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
                   'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
                   'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

    s = s[1:-1]
    score = 0

    for char in s:
        score += name_scores[char]

    return score



def _get_names() -> [str]:
    file = open(INPUT, 'r')
    
    data = file.readline()
    names = data.split(',')

    file.close()
    return names



if __name__ == '__main__':
    run()


