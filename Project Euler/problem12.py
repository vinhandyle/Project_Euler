# Problem 12: Highly divisible triangular number
# Answer: 76576500
# Bad time complexity

import euler

THRESHOLD = 5000

def run() -> None:
    sum = 0
    index = 1

    while True:
        sum += index
        factors = euler.list_unique_factors(sum)
        if len(factors) > THRESHOLD:
            break
        index += 1
        
    print(sum)



if __name__ == '__main__':
    run()


