# Problem 27: Quadratic primes
# Answer:

import euler


def _consecutive_primes(f: 'lambda') -> int:
    '''
    Returns the number of consecutive primes generated from the given equation.
    '''
    n = 0
    while euler.is_prime_number(f(n)):
        n += 1
    return n

def run() -> None:
    max_primes = 0
    ans = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            if (p := _consecutive_primes(lambda n: n * n + a * n + b)) >= max_primes:
                max_primes = p
                ans = a * b
    print(ans)


if __name__ == '__main__':
    run()
