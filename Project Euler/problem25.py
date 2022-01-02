# Problem 25: 1000-digit Fibonacci number
# Answer: 4782

def run() -> None:
    last_two_nums = [1, 1]
    index = 3
    while True:
        next_num = sum(last_two_nums)
        last_two_nums.pop(0)
        last_two_nums.append(next_num)
        if len(str(next_num)) >= 1000:
            break
        index += 1
    print(index)



if __name__ == '__main__':
    run()
