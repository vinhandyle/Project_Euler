# Problem 21: Amicable numbers
# Answer: 31626

import euler

THRESHOLD = 10000


def run() -> None:
    amicable = []
    
    for i in range(2, THRESHOLD):
        if not i in amicable:
            partner = _amicable(i)
            if partner > 0 and partner != i:
                amicable.append(i)
                amicable.append(partner)

    total = 0
    for num in amicable:
        total += num

    print(total)



def _amicable(n: int) -> int:
    factors = euler.list_unique_factors(n)
    factors.remove(n)
    
    sum = 0
    for factor in factors:
        sum += factor

    factors = euler.list_unique_factors(sum)
    if sum > 1:
        factors.remove(sum)
    
    _sum = 0
    for factor in factors:
        _sum += factor

    if _sum == n:
        return sum
    return 0



if __name__ == '__main__':
    run()


