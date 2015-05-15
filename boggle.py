import random
import math


cubes = [
    'aaafrs',
    'aaeeee',
    'aafirs',
    'adennn',
    'aeeeem',
    'aeegmu',
    'aegmnn',
    'afirsy',
    'bjkqxz',
    'ccenst',
    'ceiilt',
    'ceilpt',
    'ceipst',
    'ddhnot',
    'dhhlor',
    'dhlnor',
    'dhlnor',
    'eiiitt',
    'emottt',
    'ensssu',
    'fiprsy',
    'gorrvw',
    'iprrry',
    'nootuw',
    'ooottu'
]


def print_board(letters):
    board_size = int(math.sqrt(len(letters)))
    for i in xrange(len(letters)):
        print letters[i],
        if (i + 1) % board_size == 0:
            print


def get_user_words(letters):
    print "Type 'done' when finished or 'board' to reprint board."
    user_words = []
    while True:
        word = raw_input('Enter word: ')
        if word == 'done':
            break
        elif word == 'board':
            print_board(letters)
        else:
            user_words.append(word)
    return user_words


def check_if_word_in_board(word, board):
    if not word:
        return False

    first_letter = word[0]

    indices = [i for i, letter in enumerate(board) if letter == first_letter]

    return search_at_next_index(board, indices, word, [])



def find_word_starting_at_index(board, word, index, used_indices):
    if len(word) == 0:
        return True

    board_size = int(math.sqrt(len(board)))

    possible_next_indices = [i for i, letter in enumerate(board) if (letter == word[0] and adjacent(i, index, board_size) and i not in used_indices)]

    return search_at_next_index(board, possible_next_indices, word, used_indices)


def search_at_next_index(board, possible_next_indices, word, used_indices):
    if len(possible_next_indices) == 0:
        return False

    for next_index in possible_next_indices:
        word_found = find_word_starting_at_index(board, word[1:], next_index, used_indices + [next_index])
        if word_found:
            return True
    return False


def adjacent(pos1, pos2, board_size):
    return ((abs(pos1 - pos2) == 1 and pos1 / board_size == pos2 / board_size) or
            (abs(pos1 - pos2) == board_size - 1 and pos1 % board_size != pos2 / board_size)
            or abs(pos1 - pos2) == board_size or abs(pos1 - pos2) == board_size + 1)


def print_result(letters, user_words):
    print "Here are your results."
    score = 0
    for word in user_words:
        if check_if_word_in_board(word, letters):
            print word, len(word)
            score += len(word)
        else:
            print word, 'not on board'
    print "Score: ", score


def main():
    letters = [random.choice(cube) for cube in cubes]
    random.shuffle(letters)
    print_board(letters)
    user_words = get_user_words(letters)
    print_result(letters, user_words)


main()




