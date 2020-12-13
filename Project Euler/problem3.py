# Problem 3: Largest prime factor
# Answer: 6857

import euler

NUM = 600851475143

def run() -> None:
    largest = 0

    factors = euler.list_unique_factors(NUM)
    for i in range(len(factors)):
        if euler.is_prime_number(factors[i]) and factors[i] > largest:
            largest = factors[i]

    print(largest)


if __name__ == '__main__':
    run()
            

