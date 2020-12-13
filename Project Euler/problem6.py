# Problem 6: Sum square difference
# Answer: 25164150

UPPER_BOUND = 100

def run() -> None:
    sum_square = 0
    sum = 0
    for n in range(1, UPPER_BOUND + 1):
        sum_square += n * n
        sum += n

    difference = abs(sum_square - sum * sum)
    print(difference)



if __name__ == '__main__':
    run()
