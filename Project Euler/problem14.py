# Problem 14: Longest Collatz sequence
# Answer: 837799

THRESHOLD = 1000000


def run() -> None:
    print(_brute_force())


def _brute_force() -> int:
    '''
    Generates a Collatz sequence using every number under the threshold.
    Process is sped up by storing the length of previously generated chains.
    '''
    longest = (0, 0) # start, length
    known_chains = dict()

    for i in range(1, THRESHOLD + 1):
        chain = _collatz(i, known_chains)
        if chain > longest[1]:
            longest = i, chain

    return longest[0]



def _collatz(n: int, known_chains: {int: int}) -> int:
    if n == 1:
        return 1
    
    if n % 2 == 0:
        next = int(n / 2)
    else:
        next = 3 * n + 1

    if next in known_chains:
        return known_chains[next]
    else:
        known_chains[next] = _collatz(next, known_chains) + 1
        return known_chains[next]
    
        


if __name__ == '__main__':
    run()


