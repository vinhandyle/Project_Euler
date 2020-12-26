# Problem 16: Power digit sum
# Answer: 1366

THRESHOLD = 1000


def run() -> None:
    num = 1
    total = 0
    
    for i in range(THRESHOLD):
        num *= 2

    digits = list(str(num))
    for digit in digits:
        total += int(digit)

    print(total)



if __name__ == '__main__':
    run()


