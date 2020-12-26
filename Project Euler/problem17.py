# Problem 17: Number letter counts
# Answer: 21124

THRESHOLD = 1000


def run() -> None:
    total = 0
    for i in range(1, THRESHOLD + 1):
        total +=  _letters_in_num(i)

    print(total)



def _letters_in_num(n: int) -> int:
    sum = 0
    
    if n == 1000:
        return len('onethousand')
    else:
        hundreds = int(n / 100)
        tens = int((n % 100) / 10)
        ones = int(n % 10)

        # Count hundres
        if hundreds > 0:
            sum += _letters_in_num(hundreds) + len('hundred')
            if tens + ones > 0:
                sum += len('and')

        # Count tens 
        if tens == 9:
            sum += len('ninety')
        elif tens == 8:
            sum += len('eighty')
        elif tens == 7:
            sum += len('seventy')
        elif tens == 6:
            sum += len('sixty')
        elif tens == 5:
            sum += len('fifty')
        elif tens == 4:
            sum += len('forty')
        elif tens == 3:
            sum += len('thirty')
        elif tens == 2:
            sum += len('twenty')
        elif tens == 1:
            if ones == 9:
                sum += len('nineteen')
            elif ones == 8:
                sum += len('eighteen')
            elif ones == 7:
                sum += len('seventeen')
            elif ones == 6:
                sum += len('sixteen')
            elif ones == 5:
                sum += len('fifteen')
            elif ones == 4:
                sum += len('fourteen')
            elif ones == 3:
                sum += len('thirteen')
            elif ones == 2:
                sum += len('twelve')
            elif ones == 1:
                sum += len('eleven')
            elif ones == 0:
                sum += len('ten')

        # Count ones
        if tens != 1:
            if ones == 9:
                sum += len('nine')
            elif ones == 8:
                sum += len('eight')
            elif ones == 7:
                sum += len('seven')
            elif ones == 6:
                sum += len('six')
            elif ones == 5:
                sum += len('five')
            elif ones == 4:
                sum += len('four')
            elif ones == 3:
                sum += len('three')
            elif ones == 2:
                sum += len('two')
            elif ones == 1:
                sum += len('one')

    return sum



if __name__ == '__main__':
    run()


