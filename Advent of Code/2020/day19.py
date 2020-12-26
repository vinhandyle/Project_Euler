# Day 19: Monster Messages
# Part 1: 149
# Part 2: 332

from pathlib import Path

INPUT = Path('input_19.txt')
DEBUG1 = False
DEBUG2 = False


class Data:
    def __init__(self, rules: {int: str or [int]}, messages = [str]):
        self._rules = rules
        self._messages = messages
        self._counter = 0


    def count_valid(self) -> int:
        '''Returns the number of messages which satisfy rule 0'''
        valid = 0
        for message in self._messages:
            self._counter = 0
            if self._satisfies_rule(message, 0, 0)[0]:
                valid += 1
                if DEBUG2:
                    print(message)
                
            if DEBUG1:
                print()
                
        return valid


    def change_rules(self) -> None:
        '''Changes rules 8 and 11'''
        self._rules[8] = [[42], [42, 8]]
        self._rules[11] = [[42, 31], [42, 11, 31]]


    def _satisfies_rule(self, message: str, rule_num: int, index: int) -> (bool, int):
        '''
        Returns True if the message satisfies the given rule.
        Returns False otherwise.
        In addition, returns the difference between inital and end indexes.
        '''
        curr_rule = self._rules[rule_num]

        # The index should return to its initial state when
        # going on to the next rule set.
        for rule_set in curr_rule:
            _index = index
            requirements = len(rule_set)
            passed = 0
            
            for rule in rule_set:
                index_delta = 0
                if DEBUG1:
                    print(f'{message} {rule_set}, rule: {rule}, index: {index}, _index: {_index}, delta: {index_delta},', end = ' ')

                # When reaching the bottom layer,
                # check if the character at the given index in
                # the message matches the character in the rule.
                if type(rule) == str:
                    try:
                        is_valid = message[_index] == rule

                    except IndexError:
                        self._counter += 1 # Count how many times message overflowed
                        
                        if DEBUG2:
                            print(len(message), index, rule, message)

                        return True, 0
                        
                    if DEBUG1:
                        print(f'{is_valid}')
                        
                    return is_valid, 0

                if DEBUG1:
                    print()
                
                valid, index_delta = self._satisfies_rule(message, rule, _index)

                # The index should increment by the distance
                # traversed in the previous rule if the entire
                # trip was successful.
                if valid:
                    passed += 1
                    _index += index_delta + 1

                else:
                    break

                if DEBUG1:
                    print(f'{message} {rule_set}, rule: {rule}, index: {index}, _index: {_index}, delta: {index_delta}')

            # If this branch was successful, return the difference in
            # start and end indexes.
            if passed == requirements:
                if rule_num == 0:
                    # If passed all but with some unmatched or too many
                    # overflows, fail it anyways.
                    if len(message) > _index or \
                       self._counter * 1.5 >= len(message):
                        return False, 0
                    else:
                        return True, 0
                else:
                    return True, _index - index - 1

        # Index does not matter for failure since we backtrack all the way
        #print(f'rule:{rule_num}, set:{rule_set}, i:{_index}, m:{message}')
        return False, 0



def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''Returns the number of messages which satisfy all rule 0'''
    rules, messages = _get_rules_and_messages()
    data = Data(rules, messages)
    return data.count_valid()



def get_second_ans() -> int:
    '''Returns the number of messages which satisfy all rule 0'''
    rules, messages = _get_rules_and_messages()
    data = Data(rules, messages)
    data.change_rules()
    return data.count_valid()



def _get_rules_and_messages() -> ({int: str or [int]}, [str]):
    '''
    Finds the text file specified by INPUT and returns its content as a tuple
    containing a dictionary for the rules and list of strings for the messages.
    '''
    file = open(INPUT, 'r')
    rules = dict()
    messages = []
    mode = 'rules'

    for line in file:
        if mode == 'rules':
            rule_num = 0
            rule_list = []
            rule_sequence = []
            chunk = ''

            # Switch modes when the blank line is reached
            if line[0] == '\n':
                mode = 'messages'
                continue

            # Get rule number (first number)
            index = 0
            for char in line.replace('\n', ''):
                if char == ':':
                    rule_num = int(chunk)
                    chunk = ''
                    break
                else:
                    chunk += char
                index += 1

            # Get sub-rules
            for char in line[index + 2:].replace('"', ''):
                if char == ' ':
                    try:
                        rule_sequence.append(int(chunk))
                        chunk = ''

                    except ValueError:
                        pass
                    
                elif char == '|':
                    rule_list.append(rule_sequence)
                    rule_sequence = []
                    
                elif char == '\n':
                    if len(chunk) > 0:
                        try:
                            rule_sequence.append(int(chunk))

                        except ValueError:
                            rule_sequence.append(chunk)

                        finally:
                            rule_list.append(rule_sequence)
                        
                else:
                    chunk += char 
            
            rules[int(rule_num)] = rule_list
        else:
            messages.append(line[:-1])
    
    file.close()
    return rules, messages



if __name__ == '__main__':
    run()
