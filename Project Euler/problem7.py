# Problem 7: 10001st prime
# Answer: 104743

import euler


TARGET = 10001

def run() -> None:
    primes = 2
    index = 3
    while primes < TARGET:
        index += 2
        if euler.is_prime_number(index):
            primes += 1
    print(index)



if __name__ == '__main__':
    run()
