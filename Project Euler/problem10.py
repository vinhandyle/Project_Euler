# Problem 10: Summation of primes
# Answer: 142913828922

import euler

THRESHOLD = 2000000


def run() -> None:
    sum = 2
    for i in range(3, THRESHOLD, 2):
        if euler.is_prime_number(i):
            sum += i
    print(i)



if __name__ == '__main__':
    run()
