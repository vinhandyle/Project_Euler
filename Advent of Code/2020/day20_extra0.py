def reverse_string(s: str) -> str:
    '''Given a string, returns a new string which is the former backwards'''
    new_s = ''
    for i in range(len(s) - 1, -1, -1):
        new_s += s[i]
    return new_s



def can_match(s1: str, s2: str) -> bool:
    '''
    Returns True if the strings are the same or mirrored versions of each other.
    '''
    return s1 == s2 or reverse_string(s1) == s2



def reverse_list(l: list) -> list:
    '''Reverses the elements of a list'''
    new_list = []
    for i in range(len(l) - 1, -1, -1):
        new_list.append(l[i])
    return new_list
