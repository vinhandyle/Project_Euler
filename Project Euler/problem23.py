# Problem 23: Non-abundant sums
# Answer: 4179871

import euler

THRESHOLD = 28123


def run() -> None:
    sum = 1
    abundant_nums = []
    abundant_sums = []

    for i in range(12, THRESHOLD):
        if _is_abundant(i):
            abundant_nums.append(i)

    for i in range(len(abundant_nums)):
        for num in abundant_nums[i:]:
            abundant_sums.append(abundant_nums[i] + num)

    for i in range(2, THRESHOLD):
        if not i in abundant_sums:
            sum += i
        
    print(sum)


def _is_abundant(n: int) -> bool:
    factors = euler.list_unique_factors(n)
    factors.sort()
    factors = factors[:-1]

    sum = 0
    for factor in factors:
        sum += factor

    if sum > n:
        return True
    return False



if __name__ == '__main__':
    run()
