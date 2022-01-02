# Python recursion limit at 1000 so linked list processing must be iterative
# Linked list approach is slightly slower than list, wtf?

INPUT = '219748365'
TEST = '389125467'
A = 100
B = 10**7
DEBUG = False
DEBUG2 = True

class LL:
    def __init__(self, value: int, next: 'LL' = None):
        self.value = value
        self.next = next


class CupGame:
    def __init__(self, cups: str):
        self._rear = None
        self._min, self._max = 10**6 + 1, -1
        self._cups = self.build_ll([int(c) for c in cups])
        self._front = self._cups

    def build_ll(self, iterable) -> LL:
        '''Turns an iterable into a linked list'''
        if len(iterable) == 0:
            return None
        else:
            v = iterable[0]
            self._min = v if v < self._min else self._min
            self._max = v if v > self._max else self._max
            r = self.build_ll(iterable[1:])
            self._rear = r if r != None and r.next == None else self._rear
            return LL(v, r)

    def extend_ll(self, final: int) -> None:
        '''Extends the linked list to contain the given number of list nodes'''
        curr = self._max + 1
        while curr <= final:
            self._rear.next = LL(curr)
            self._rear = self._rear.next
            curr += 1

    def ll_to_list(self, ll: LL) -> list:
        '''Turns a linked list into a list'''
        if ll == None:
            return []
        else:
            return [ll.value] + self.ll_to_list(ll.next)

    def cups(self) -> LL:
        '''Returns a linked list of the cups'''
        return self._cups

    def picked_up(self) -> LL:
        '''Returns a linked list of the picked up cups'''
        return self._pfront

    def display_cups(self, ll: LL = []) -> str:
        '''Returns a string of the cup labels in order'''
        llstring = ''
        temp = self._front if ll == [] else ll
        while temp != None:
            llstring += str(temp.value)
            temp = temp.next
        return llstring

    def pick_cups(self) -> None:
        '''
        Changes the first cup's reference to the fifth cup and the fourth cup's
        reference to None. Stores the reference to the second cup in an attribute.
        '''
        self._pfront, self._cups.next = self._cups.next, None
        temp = self._pfront
        for i in range(2):
            temp = temp.next
        self._prear, self._cups.next = temp, temp.next
        self._prear.next = None

    def _get_target(self) -> int:
        '''
        Sets a target value as 1 less than the first cup's value. If one of the
        picked up cups has the target value, the target value is subtracted by 1.
        If the target value is less than the minimum cup value, it becomes the
        maximum cup value. Repeat this until a valid target value is found,
        which is then returned.
        '''
        picked_vals = self.ll_to_list(self._pfront)
        target = self._front.value - 1
        target = self._max if target < self._min else target
        while target in picked_vals:
            target -= 1
            target = self._max if target < self._min else target
        return target

    def _cup_with_value(self, value, ll: LL = []) -> LL:
        '''Returns the cup with the given value'''
        temp = self._front if ll == [] else ll
        while temp != None:
            if temp.value == value:
                return temp
            temp = temp.next

    def _get_rear(self) -> LL:
        '''Returns the last cup, whose reference is None'''
        if self._rear.next == None:
            return self._rear
        temp = self._rear
        while temp.next != None:
            temp = temp.next
        return temp
    
    def _rearrange(self) -> None:
        '''
        Changes the reference of the last cup to the 'first' cup and the first cup's
        reference to None.
        '''
        self._rear = self._get_rear()
        temp, self._front = self._front, self._front.next
        self._rear.next, temp.next = temp, None

    def place_cups(self) -> None:
        '''
        Finds the cup with the target value and changes its reference to the
        first cup
        '''
        target = self._get_target()
        print(f'Destination: {target}\n' if DEBUG else '', end = '')
        destination = self._cup_with_value(target)
        self._prear.next, destination.next = destination.next, self._pfront
        self._rearrange()
        self._cups = self._front
        


def run() -> None:
    print(get_first_ans())
    print(get_second_ans())



def get_first_ans() -> int:
    '''
    Returns the cups directly clockwise to the cup labelled 1 after 100 moves.
    '''
    game = CupGame(INPUT)

    move, moves = 0, A
    if DEBUG:
            print(move + 1, '->', game.display_cups(), '\n')
    while move < moves:
        move += 1
        game.pick_cups()
        if DEBUG:
            print(move + 1, '->', game.display_cups(), game.display_cups(game.picked_up()))
        game.place_cups()
        if DEBUG:
            print(move + 1, '->', game.display_cups(), '\n')
        print(f'{move}\n' if DEBUG2 and move % (moves // 10) == 0 else '', end = '')
        
    cups = game.display_cups()
    return cups[cups.index('1') + 1:] + cups[:cups.index('1')]



def get_second_ans() -> int:
    '''
    Returns the product of the two cups next in the reference chain from cup 1
    after 10 million moves.
    '''
    game = CupGame(TEST)
    game.extend_ll(15)

    move = 0
    if DEBUG:
            print(move + 1, '->', game.display_cups(), '\n')

    try:
        moves = B
        while move < moves:
            move += 1
            game.pick_cups()
            if DEBUG:
                print(move + 1, '->', game.display_cups(), game.display_cups(game.picked_up()))
            game.place_cups()
            if DEBUG:
                print(move + 1, '->', game.display_cups(), '\n')
            print(f'{move}\n' if DEBUG2 and move % (moves // 10) == 0 else '', end = '')

    except KeyboardInterrupt:
        print(move)
            
    cup1 = game._cup_with_value(1)
    cupX = cup1.next if cup1.next != None else game.cups()
    cupY = cupX.next if cupX.next != None else game.cups()
    return cupX.value * cupY.value



if __name__ == '__main__':
    run()
