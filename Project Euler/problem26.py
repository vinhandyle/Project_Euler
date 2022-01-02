# Problem 26: Reciprocal cycles
# Answer:

import euler


def run() -> None:
    primes = [i for i in range(2, 1001) if euler.is_prime_number(i)]
    d_list = [i for i in range(1, 1001) if 1000 % i != 0]

    for p in primes:
        print(p, 1 / p)


    
if __name__ == '__main__':
    run()
