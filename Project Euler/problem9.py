# Problem 9: Special Pythagorean triplet
# Answer: 31875000

import math

TARGET = 1000


def run() -> None:
    # The largest value a can take is 1 less
    # than a third of the total
    for a in range(1, math.floor(TARGET / 3)):
        # The largest value b can take is 1 less than half of
        # 1 less than the total
        for b in range(a + 1, math.floor((TARGET - 1) / 2)):
            c = math.sqrt(a * a + b * b)
            if c == math.floor(c):
                if a + b + c == 1000:
                    print(int(a * b * c))

            

if __name__ == '__main__':
    run()
