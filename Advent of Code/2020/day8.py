# Day 8: Handheld Halting
# Part 1: 1262
# Part 2: 1643

from pathlib import Path

INPUT = Path('input_8.txt')


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''
    Returns the value of the accumulator the instance before the program
    executes an instruction a second time.
    '''
    instructions = _get_boot_code()
    
    return _accumulate(instructions)[0]



def get_second_ans() -> int:
    '''
    Returns the value of the accumulator after the program terminates following
    the change of operation from "jmp" to "nop".
    '''
    instructions = _get_boot_code()
    og_traversed = _accumulate(instructions)[1]

    # Checks each jump operation executed in the
    # original set of instructions
    for index in og_traversed:
        line = instructions[index]
        operation, argument = line

        # Replaces the jump operation with no operation
        # and checks if it terminates
        # Reverts if there is an infinite loop
        if operation == 'jmp':
            instructions[index] = ('nop', argument)
            total, new_traversed = _accumulate(instructions)
            destinations = _get_destinations(instructions, new_traversed)

            # Program terminates if the last line was executed
            if len(instructions) - 1 in destinations:
                return total
            else:
                instructions[index] = (operation, argument)
                


def _accumulate(instructions: [(str, int)]) -> int:
    '''
    Executes the instructions and returns the value when the program terminates
    or begins and infinite loop.
    '''
    index = 0
    total = 0
    executed_lines = []
    
    while True:
        if index in executed_lines or \
           index == len(instructions):
            break

        operation, argument = instructions[index]
        executed_lines.append(index)

        if operation == 'acc':
            total += argument
            index += 1
        elif operation == 'jmp':
            index += argument
        elif operation == 'nop':
            index += 1

    return total, executed_lines


            
def _get_destinations(instruction: [(str, int)], traversed = []) -> [int]:
    '''
    Given a list of operations and their arguments, returns a list of integers
    representing the line on which the next operation would be executed following
    the execution of each line.
    '''
    num_list = []
    indexes = 0

    # Total or partial traversal of instruction
    if traversed == []:
        indexes = range(len(instruction))
    else:
        indexes = traversed

    for index in indexes:
        operation, argument = instruction[index]
        if operation == 'acc' or operation == 'nop':
            num_list.append(index + 1)
        elif operation == 'jmp':
            num_list.append(index + argument)
            
    return num_list



def _get_boot_code() -> [(str, int)]:
    '''
    Finds the text file specified by INPUT and returns its content as a list of
    tuples containing the operation name and its integer argument.
    '''
    file = open(INPUT, 'r')
    instruction_list = []

    for line in file:
        if line[4] == '+':
            instruction_list.append((line[:3], int(line[5:])))
        else:
            instruction_list.append((line[:3], int(line[4:])))
    

    file.close()
    return instruction_list



if __name__ == '__main__':
    run()
