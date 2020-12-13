# Problem 1: Multiples of 3 and 5
# Answer: 233168

THRESHHOLD = 1000

def run() -> None:
    total = 0

    for i in range(THRESHHOLD):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    print(total)


if __name__ == '__main__':
    run()
