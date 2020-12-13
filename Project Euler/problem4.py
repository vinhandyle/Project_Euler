# Problem 4: Largest palindrome product
# Answer: 906609


def run() -> None:
    largest = 0

    for i in range(100, 999):
        for j in range(i, 999):
            k = i * j
            if _is_palindrome(str(k)) and k > largest:
                largest = k

    print(largest)


def _is_palindrome(s: str) -> bool:
    '''
    Returns True if the given string is a palindrome. Returns False, otherwise.
    '''
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False

    return True


if __name__ == '__main__':
    run()
