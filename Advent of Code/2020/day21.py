# Day 21: Allergen Assessment
# Part 1: 2203
# Part 2: fqfm,kxjttzg,ldm,mnzbc,zjmdst,ndvrq,fkjmz,kjkrm

from pathlib import Path

INPUT = Path('input_21.txt')


class Food:
    def __init__(self, ingredients, allergens):
        self._ingredients = ingredients
        self._allergens = allergens


    def ingredients(self) -> [str]:
        '''Returns a list of the food's ingredients'''
        return self._ingredients


    def allergens(self) -> [str]:
        '''Returns a list of food's listed allergens'''
        return self._allergens


        
def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''
    Returns the number of times ingredients that contain no allergens appear in
    the list.
    '''
    food_list = _get_food_list()
    known_allergens = dict()

    # Get all unique allergens
    for food in food_list:
        for allergen in food.allergens():
            if not allergen in known_allergens:
                known_allergens[allergen] = ''

    # One-by-one identify allergen containing foods
    incomplete = True
    while incomplete:
        _perform_full_search(food_list, known_allergens)
        incomplete = not _is_complete(known_allergens)

    # Count leftover food
    total = 0
    for food in food_list:
        total += len(food.ingredients())

    return total


        
def get_second_ans() -> str:
    '''Returns the canonical dangerous ingredient list'''
    food_list = _get_food_list()
    known_allergens = dict()

    # Get all unique allergens
    for food in food_list:
        for allergen in food.allergens():
            if not allergen in known_allergens:
                known_allergens[allergen] = ''

    # One-by-one identify allergen containing foods
    incomplete = True
    while incomplete:
        _perform_full_search(food_list, known_allergens)
        incomplete = not _is_complete(known_allergens)

    # Alphabetically sorts allergens
    allergens = []
    for allergen in known_allergens:
        allergens.append(allergen)
    allergens.sort()

    # Attaches the corresponding ingredient to the string
    danger = ''
    for allergen in allergens:
        danger += known_allergens[allergen] + ','

    return danger[:-1]


def _is_complete(d: {str: str}) -> bool:
    '''
    Returns True if each field in the dictionary is not an empty string.
    Returns False otherwise.
    '''
    completed = 0
    for allergen in d:
        if d[allergen] != '':
            completed += 1
    return completed == len(d)



def _perform_full_search(food_list: [Food], a_dict: {str: str}) -> None:
    '''
    For each incomplete allergen, builds a list of foods which definitely
    contain the allergen.
    Finds the one ingredient that each food in the list have in common (if
    there is more than one, proceeds to the next allergen).
    This ingredient is put into the dictionary under the allergen and removed
    from all food in the main list.
    Iterates through the entire dictionary of allergens.
    '''
    for allergen in a_dict:
        if a_dict[allergen] == '':
            a_list = _build_a_list(food_list, allergen)
            common = None
            reference = a_list[0]

            for ingredient in reference.ingredients():
                passed = 1
                for food in a_list[1:]:
                    for _ingredient in food.ingredients():
                        if ingredient == _ingredient:
                            passed += 1

                if passed == len(a_list) > 1:
                    if common == None:
                        common = ingredient
                    else:
                        common = None
                        break

            if common != None:
                a_dict[allergen] = common
                _remove_from_all_food(food_list, common)


        _handle_last_allergen(food_list, a_dict)



def _handle_last_allergen(food_list: [Food], a_dict: {str: str}) -> None:
    '''
    Handles the case where the last allergen appears in only one food, preventing
    the recursion from finding and removing it.
    '''
    allergen = None
    empty = 0
    for a in a_dict:
        if a_dict[a] == '':
            allergen = a
            empty += 1

    if empty > 1 or allergen == None:
        return

    a_list = _build_a_list(food_list, allergen)

    if len(a_list) > 1:
        return
        
    food = a_list[0]

    if len(food.ingredients()) == 1:
        common = food.ingredients()[0]
        a_dict[allergen] = common
        _remove_from_all_food(food_list, common)
    else:
        a_dict[allergen] = ' '


                    
def _build_a_list(food_list: [Food], allergen: str) -> [Food]:
    '''Returns a list of food that definitely contain the given allergen'''
    a_list = []
    for food in food_list:
        if allergen in food.allergens():
            a_list.append(food)
    return a_list



def _remove_from_all_food(food_list: [Food], ingredient: str) -> None:
    '''Removes a given ingredient from every food in the list'''
    for food in food_list:
        if ingredient in food.ingredients():
            food.ingredients().remove(ingredient)
            


def _get_food_list() -> [([str], [str])]:
    '''
    Finds the text file specified by INPUT and returns its content as a list of
    tuples containing a list of ingredients and a list of allergens.
    '''
    file = open(INPUT, 'r')
    food_list = []

    for line in file:
        ingredients = []
        allergens = []
        word = ''
        phase_1 = True

        index = 0
        while True:
            char = line[index]
            if phase_1:
                if char == '(':
                    phase_1 = False
                    index += len('contains') + 1
                elif char == ' ':
                    ingredients.append(word)
                    word = ''
                else:
                    word += char
            else:
                if char == ')':
                    allergens.append(word)
                    break
                elif char == ' ':
                    allergens.append(word)
                    word = ''
                elif char != ',':
                    word += char
            index += 1
        food_list.append(Food(ingredients, allergens))
        
    file.close()
    return food_list


if __name__ == '__main__':
    run()
