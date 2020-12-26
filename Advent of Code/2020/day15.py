# Day 15: Rambunctious Recitation
# Part 1: 211
# Part 2: 2159626

INPUT = {1: 5, 0: 4, 15: 3, 2: 2, 10: 1, 13: 0}
INPUT2 = {1: 0, 0: 1, 15: 2, 2: 3, 10: 4, 13: 5}

TEST = {0: 2, 3: 1, 6: 0}
TEST2 = {0: 0, 3: 1, 6: 2}

DEBUG = False


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''Returns the 2020th number spoken in the Elf game'''
    starting_nums = _copy_dict(INPUT2)
    return _find_nth_number_faster(starting_nums, 2020)


def get_second_ans() -> int:
    '''Returns the 30 millionth number spoken in the Elf game'''
    starting_nums = _copy_dict(INPUT2)
    return _find_nth_number_faster(starting_nums, 30000000) 



def _find_nth_number_faster(nums: {int: int}, n: int) -> int:
    '''Returns the nth number spoken in the Elf game, but faster'''
    recent = _get_most_recent(nums, age = False)
    index = len(nums)

    while index < n:
        try:
            # Gets the most recent num and the index of its previous iteration
            recent_num, prev_index = recent

            # Finds the difference indexes between the two iterations
            if not recent_num in nums:
                nums[recent_num] = prev_index
                diff = 0
            else:
                diff = prev_index - nums[recent_num]

            if DEBUG:
                print((index, diff), (nums[recent_num], recent_num))
                
            # Saves the new most recent number
            recent = (diff, index)
            nums[recent_num] = prev_index
            index += 1

        except KeyboardInterrupt:
            print(index)
            raise Exception

    recent_num = recent[0]
    return recent_num



def _find_nth_number(nums: {int: int}, n: int) -> int:
    '''Returns the nth number spoken in the Elf game'''
    recent = _get_most_recent(nums)
    index = len(nums) + 1

    while index <= n:
        try:
            # Get the most recent num and the age of its previous iteration
            recent_num, age = recent
            _age_nums(nums)

            if DEBUG:
                if age == 0:
                    print(index, recent, '*')
                else:
                    print(index, recent)

            # If the difference in age has not been recorded before
            if not age in nums:
                nums[age] = 0

            # Save the new most recent number
            recent = (age, nums[age])
            nums[age] = 0                
            index += 1

        except KeyboardInterrupt:
            print(index)
            raise Exception

    recent_num = _get_most_recent(nums)[0]
    return recent_num



def _get_most_recent(nums: (int, int), age = True) -> int:
    '''Returns the number in the dictionary with the lowest age'''
    if age:
        smallest = (-1, -1)

        for num in nums:
            if smallest[1] == -1:
                smallest = (num, nums[num])
            elif nums[num] < smallest[1]:
                smallest = (num, nums[num])

        return smallest

    else:
        largest = (0, 0)

        for num in nums:
            if nums[num] > largest[1]:
                largest = (num, nums[num])

        return largest



def _age_nums(nums: {int: int}) -> None:
    '''Increments the age of each number in the dictionary by 1'''
    for num in nums:
        nums[num] += 1



def _copy_dict(d: {int: int}) -> {int: int}:
    '''Returns a copy of the given dictionary'''
    new_d = dict()

    for key in d:
        new_d[key] = d[key]

    return new_d


if __name__ == '__main__':
    run()
