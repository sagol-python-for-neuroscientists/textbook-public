"""
__author__ = Hagai Har-Gil
HW1 Question 1 Solution
"""
def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    if len(word) < 6:
        return False

    # Deal with pairs starting in an even letter
    num_pairs = 0
    even = word[::2]
    odd = word[1::2]
    for first, second in zip(even, odd):
        if first == second:
            num_pairs += 1
            if num_pairs == 3:
                return True
        else:
            num_pairs = 0

    # If we reached here we need to deal with the case of a pair of letters starting in an odd letter
    num_pairs = 0
    new_even = even[1:]
    for first, second in zip(new_even, odd):
        if first == second:
            num_pairs += 1
            if num_pairs == 3:
                return True
        else:
            num_pairs = 0

    return False


if __name__ == '__main__':
    print("Question 1 solution:")
    string1 = 'llkkbmm'
    string2 = '434343'
    print("String one: ", trifeca(string1))



