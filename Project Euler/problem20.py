# Problem 20: Factorial digit sum
# Answer: 648

import math


def run() -> None:
    sum = 0
    num = math.factorial(100)

    digits = list(str(num))

    for digit in digits:
        sum += int(digit)

    print(sum)



if __name__ == '__main__':
    run()


