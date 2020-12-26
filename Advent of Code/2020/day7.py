# Day 7: Handy Haversacks
# Part 1: 112
# Part 2: 6260

from pathlib import Path


INPUT = Path('input_7.txt')
OUR_BAG = 'shinygoldbag'


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''Returns the number of bags which contain our bag (regardless of depth)'''
    rules = _get_rules()
    valid_bags = [OUR_BAG]

    _find_container_bags(valid_bags, rules)

    return len(valid_bags) - 1
        


def get_second_ans() -> int:
    '''Returns the number of bags our bag contains'''
    rules = _get_rules()

    return _get_contained_bags(OUR_BAG, rules) -1



def _get_contained_bags(container_bag: str, rules: 'nested dict') -> int:
    '''Returns the number of bags contained by the given bag'''
    bags = 0
    
    for contained_bag in rules[container_bag]:
        num_bags = contained_bag[next(iter(contained_bag))]
        if num_bags == 0:
            return 1

        sub_contained_bags = _get_contained_bags(
            next(iter(contained_bag)), rules)

        bags += num_bags * sub_contained_bags
    
    return bags + 1



def _find_container_bags(valid_bags: [str], rules: 'nested dict') -> None:
    '''
    Given a set of rules, updates the list of valid bags to also contain every
    bag which contains any of the valid bags.
    '''
    # Pseduo-recursive since container bags added to
    # the end also get checked for their container bags
    for valid_bag in valid_bags:
        for container_bag in rules:
            for contained_bag in rules[container_bag]:
                # Checks if valid_bag is a key in contained_bag and
                # if valid_bags already contains container_bags
                if valid_bag in contained_bag and \
                   not container_bag in valid_bags:
                    valid_bags.append(container_bag)



def _get_rules() -> {str: [{str: int}]}:
    '''
    Finds the text file specified by INPUT and returns its content as a nested
    dictonary.
    Outer dict: keys = container bag, fields = inner dicts
    Inner dict: keys = contained bag, field = # of contained bags in container
    '''
    file = open(INPUT, 'r')
    rules = dict()

    for line in file:
        _line = line.split()
        key = ''
        field = []
        num = 0
        bag_type = ''
        mode = 'key'
        
        for index in range(len(_line)):
            string = _line[index]
            if string == 'contain':
                mode = 'field'
                # Remove plural
                if key[-1] == 's':
                    key = key[:-1]
                
            elif mode == 'key':
                key += string
                
            elif mode == 'field':
                # Checks if the string is an integer
                # Then adds each bag type to the field list
                try:
                    num = int(string)

                except ValueError:
                    if string[-1] == ',' or string[-1] == '.':
                        # Remove plural
                        if string[-2] == 's':
                            bag_type += string[:-2]
                        else:
                            bag_type += string[:-1]
                            
                        field.append({bag_type: num})
                        bag_type = ''
                    else:
                        bag_type += string
                        
        rules[key] = field
        
    file.close()
    return rules



if __name__ == '__main__':
    run()
