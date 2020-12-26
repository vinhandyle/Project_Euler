# Day 23: Crab Cups
# Part 1: 35827964
# Part 2:

INPUT = '219748365'
TEST = '389125467'
A = 100
B = 10000000
DEBUG = False


class CupGame:
    def __init__(self, cups: str):
        self._cups = [int(cup) for cup in cups]
        self._current_index = 0
        self._current_cup = self._cups[0]
        self._get_min_max()
        self._picked_up = None


    def cups(self) -> [int]:
        '''Returns a list of all cups, ordered clockwise'''
        return self._cups


    def picked_up_cups(self) -> [int]:
        '''Returns a list of the picked up cups, ordered clockwise'''
        return self._picked_up


    def _get_min_max(self) -> None:
        '''Identifies the smallest and largest cups'''
        smallest = self._current_cup
        largest = self._current_cup

        for cup in self._cups:
            if cup < smallest:
                smallest = cup

            if cup > largest:
                largest = cup

        self._smallest_cup = smallest
        self._largest_cup = largest


    def add_one_million(self) -> None:
        '''Adds to the list until there are a million cups'''
        while len(self._cups) < 1000000:
            self._cups.append(self._largest_cup + 1)
            self._largest_cup += 1


    def pick_up_cups(self) -> None:
        '''
        Moves the three cups directly clockwise to the current cup from the cups
        list to the 'picked up' list
        '''
        current = self._current_index
        picked_up = []
        # O(3)
        for i in range(3):
            if current + 1 >= len(self._cups):
                picked_up.append(self._cups.pop(0))
            else:
                picked_up.append(self._cups.pop(current + 1))
        self._picked_up = picked_up
        if DEBUG:
            print('A')


    def place_cups(self) -> None:
        '''
        Places the picked up cups directly clockwise to the cup that one less
        than the current cup. If the destination cup is one of the picked up
        cups, repeat the subtraction. If the destination cup is smaller than
        the smallest cup, wrap back around to the largest cup.
        '''
        destination = self._current_cup - 1

        if destination < self._smallest_cup:
            destination = self._largest_cup

        while destination in self._picked_up:
            destination -= 1
            if destination < self._smallest_cup:
                destination = self._largest_cup

        if DEBUG:
            print('B')

        # O(1) to O(n)
        target_i = self._cups.index(destination)
        self._cups = self._cups[:target_i + 1] + \
                             self._picked_up + \
                             self._cups[target_i + 1:]
        self._picked_up = None

        if DEBUG:
            print('C')

        self._reconfigure()

        if DEBUG:
            print('D')

        self._current_index += 1
        if self._current_index >= len(self._cups):
            self._current_index = 0
        self._current_cup = self._cups[self._current_index]


    def _reconfigure(self) -> None:
        '''Repositions the cups so that the current cup is at the current index'''
        # O(1) to O(n)
        index = self._cups.index(self._current_cup)
        self._cups = self._cups[index - self._current_index: index] + \
                     self._cups[index:] + \
                     self._cups[:index - self._current_index]


    def get_answer(self) -> str:
        '''Returns the cups starting from the one after the cup labelled 1'''
        ans = ''
        index = 0
        for i in range(len(self._cups)):
            if self._cups[i] == 1:
                index = i

        cup_list = self._cups[index + 1:] + self._cups[:index]
        for cup in cup_list:
            ans += str(cup)
        return ans


    def get_answer2(self) -> int:
        '''
        Finds the two cups directly after the cup labelled 1 and returns the
        product of their labels.
        '''
        index = 0
        for i in range(len(self._cups)):
            if self._cups[i] == 1:
                index = i

        indexes = [index + 1, index + 2]
        for i in range(len(indexes)):
            if indexes[i] >= len(self._cups):
                indexes[i] -= len(self._cups)

        return self._cups[indexes[0]] * self._cups[indexes[1]]

    
def run() -> None:
    print(get_first_ans())
    #print(get_second_ans())



def get_first_ans() -> str:
    '''
    Returns the cups directly clockwise to the cup labelled 1 after 100 moves.
    '''
    game = CupGame(INPUT)

    move = 0
    try:
        while move < B:
            #print(game.cups())
            game.pick_up_cups()
            #print(game.picked_up_cups())
            game.place_cups()
            move += 1

    except KeyboardInterrupt:
        print(move)

    return game.get_answer()



def get_second_ans() -> int:
    '''
    Returns the product of the two cups immediately clockwise to the cup
    labelled 1 after 10 million moves.
    '''
    game = CupGame(TEST)
    game.add_one_million()

    move = 0
    try:
        while move < B:
            game.pick_up_cups()
            game.place_cups()
            move += 1

    except KeyboardInterrupt:
        print(move)

    return game.get_answer2()
    


if __name__ == '__main__':
    run()
