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

    if len(indices) == 0:
        return False


    for index in indices:
        word_found = find_word_starting_at_index(board, word, index)
        if word_found:
            return True
    return False


def find_word_starting_at_index(board, word, index):
    word_found = True
    indices_used = [index]
    board_size = int(math.sqrt(len(board)))
    for i in xrange(1, word):
        possible_next_indices = [i for i, letter in enumerate(board) if letter == word[i] and adjacent(i, indices_used[-1], board_size)]
        next_index = get_index_of_next_letter(indices_used[-1], word[i], board, indices_used)
        if next_index == -1:
            word_found = False
            break
        else:
            word_found = True
            indices_used.append(next_index)
    return word_found


def adjacent(pos1, pos2, board_size):
    return ((abs(pos1 - pos2) == 1 and pos1 % board_size == pos2 % board_size)  # if but one apart, must be on same line
            or abs(pos1 - pos2) == 4 or abs(pos1 - pos2) == 5 or abs(pos1 - pos2) == 6)


def check_top_row(board, board_size, current_index, indices_used, letter, next_index):
    # first square
    if current_index % board_size == 0:
        if check_relative_tile(current_index, board, letter, indices_used, 1):
            next_index = current_index + 1
        elif check_relative_tile(current_index, board, letter, indices_used, 5):
            next_index = current_index + 5
        elif check_relative_tile(current_index, board, letter, indices_used, 6):
            next_index = current_index + 6

    # last square
    elif current_index % board_size == board_size - 1:
        if check_relative_tile(current_index, board, letter, indices_used, -1):
            next_index = current_index - 1
        elif check_relative_tile(current_index, board, letter, indices_used, 4):
            next_index = current_index + 4
        elif check_relative_tile(current_index, board, letter, indices_used, 5):
            next_index = current_index + 5

    # other squares
    else:
        if check_relative_tile(current_index, board, letter, indices_used, -1):
            next_index = current_index - 1
        elif check_relative_tile(current_index, board, letter, indices_used, 1):
            next_index = current_index + 1
        elif check_relative_tile(current_index, board, letter, indices_used, 4):
            next_index = current_index + 4
        elif check_relative_tile(current_index, board, letter, indices_used, 5):
            next_index = current_index + 5
        elif check_relative_tile(current_index, board, letter, indices_used, 6):
            next_index = current_index + 6

    return next_index


def check_bottom_row(board, board_size, current_index, indices_used, letter, next_index):
    # first square
    if current_index % board_size == 0:
        if check_relative_tile(current_index, board, letter, indices_used, 1):
            next_index = current_index + 1
        if check_relative_tile(current_index, board, letter, indices_used, -5):
            next_index = current_index - 5
        if check_relative_tile(current_index, board, letter, indices_used, -4):
            next_index = current_index - 4


    # last square
    if current_index % board_size == board_size - 1:
        if check_relative_tile(current_index, board, letter, indices_used, -1):
            next_index = current_index - 1
        if check_relative_tile(current_index, board, letter, indices_used, -5):
            next_index = current_index - 5
        if check_relative_tile(current_index, board, letter, indices_used, -6):
            next_index = current_index - 6

    # other square
    else:
        if check_relative_tile(current_index, board, letter, indices_used, -1):
            next_index = current_index - 1
        if check_relative_tile(current_index, board, letter, indices_used, 1):
            next_index = current_index + 1
        if check_relative_tile(current_index, board, letter, indices_used, -4):
            next_index = current_index - 4
        if check_relative_tile(current_index, board, letter, indices_used, -5):
            next_index = current_index - 5
        if check_relative_tile(current_index, board, letter, indices_used, -6):
            next_index = current_index - 6

    return next_index


def check_other_rows(board, board_size, current_index, indices_used, letter, next_index):
    # first square
    if current_index % board_size == 0:
        if check_relative_tile(current_index, board, letter, indices_used, 1):
            next_index = current_index + 1
        if check_relative_tile(current_index, board, letter, indices_used, -4):
            next_index = current_index - 4
        if check_relative_tile(current_index, board, letter, indices_used, -5):
            next_index = current_index - 5
        if check_relative_tile(current_index, board, letter, indices_used, 5):
            next_index = current_index + 5
        if check_relative_tile(current_index, board, letter, indices_used, 6):
            next_index = current_index + 6

    # last square
    if current_index % board_size == board_size - 1:
        if check_relative_tile(current_index, board, letter, indices_used, -1):
            next_index = current_index - 1
        if check_relative_tile(current_index, board, letter, indices_used, -5):
            next_index = current_index - 5
        if check_relative_tile(current_index, board, letter, indices_used, -6):
            next_index = current_index - 6
        if check_relative_tile(current_index, board, letter, indices_used, 4):
            next_index = current_index + 4
        if check_relative_tile(current_index, board, letter, indices_used, 5):
            next_index = current_index + 5

    # other square
    else:
        if check_relative_tile(current_index, board, letter, indices_used, -1):
            next_index = current_index - 1
        if check_relative_tile(current_index, board, letter, indices_used, 1):
            next_index = current_index + 1
        if check_relative_tile(current_index, board, letter, indices_used, -4):
            next_index = current_index - 4
        if check_relative_tile(current_index, board, letter, indices_used, -5):
            next_index = current_index - 5
        if check_relative_tile(current_index, board, letter, indices_used, -6):
            next_index = current_index - 6
        if check_relative_tile(current_index, board, letter, indices_used, 4):
            next_index = current_index + 4
        if check_relative_tile(current_index, board, letter, indices_used, 5):
            next_index = current_index + 5
        if check_relative_tile(current_index, board, letter, indices_used, 6):
            next_index = current_index + 6

    return next_index


def get_index_of_next_letter(current_index, letter, board, indices_used):
    board_size = int(math.sqrt(len(board)))
    
    next_index = -1
    
    # top row
    if current_index < board_size:
        next_index = check_top_row(board, board_size, current_index, indices_used, letter, next_index)

    # bottom row
    elif current_index / board_size == board_size - 1:
        next_index = check_bottom_row(board, board_size, current_index, indices_used, letter, next_index)

    # other rows
    else:
        next_index = check_other_rows(board, board_size, current_index, indices_used, letter, next_index)
            
    return next_index



def check_relative_tile(index, board, letter, used_indices, relative_location):
    return board[index + relative_location] == letter and index + relative_location not in used_indices


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




