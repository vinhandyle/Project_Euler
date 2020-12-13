# Problem 2: Even Fibonacci numbers
# Answer: 4613732

import euler

THRESHHOLD = 4000000

def run() -> None:
    num = 0
    index = 1
    total = 0

    while True:
        num = euler.fibonacci_num(index)
        
        if num < THRESHHOLD :
            if num % 2 == 0:
                total += num
            index += 1
        else:
            break

    print(total)


if __name__ == '__main__':
    run()
