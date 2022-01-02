# Problem 24: Lexicographic permutations
# Answer: 2783915460

from math import factorial as f

def run() -> None:
    p_index = 999999
    d_index = 0
    nums = [i for i in range(10)]
    ans = ''
    while d_index < 10:
        perms = f(9 - d_index)
        remainder = p_index % perms
        ans += str(nums.pop(p_index // perms))
        p_index = remainder
        d_index += 1
    print(ans)



if __name__ == '__main__':
    run()
