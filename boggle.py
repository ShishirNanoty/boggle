# Backward compat for 2.x print statements
from __future__ import print_function
import random
import math

# Backward compat for 2.x input
try:
    input = raw_input
except NameError:
    pass

cubes = [
    'aaafrs', 'aaeeee', 'aafirs', 'adennn', 'aeeeem',
    'aeegmu', 'aegmnn', 'afirsy', 'bjkqxz', 'ccenst',
    'ceiilt', 'ceilpt', 'ceipst', 'ddhnot', 'dhhlor',
    'dhlnor', 'dhlnor', 'eiiitt', 'emottt', 'ensssu',
    'fiprsy', 'gorrvw', 'iprrry', 'nootuw', 'ooottu'
]

# Simple Set of colors for ascii printing.
class bcolors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Build the dictionary up front so we can use in multiple places
with open('dictionary.txt') as f:
    english_dict = [line.strip() for line in f.readlines()]

def print_board(letters):
    board_size = int(math.sqrt(len(letters)))
    line = ""
    for i in range(len(letters)):
        line += letters[i]
        if (i + 1) % board_size == 0:
            print (line)
            line = ""
        else:
            line += " "

def get_words_from_user(board):
    print ("Type 'done!' when finished or 'board!' to reprint board.")
    user_words = []
    while True:
        word = input('Enter word: ')
        if word == 'done!':
            break
        elif word == 'board!':
            print_board(board)
        elif not find_word(board,word):
            print( bcolors.BOLD, word, bcolors.ENDC, bcolors.RED, 'Not found on board', bcolors.ENDC)
        elif word not in english_dict:
            print( bcolors.BOLD, word, bcolors.ENDC, bcolors.RED, 'Not found in dictionary', bcolors.ENDC)
        else:
            user_words.append(word)
    return set(user_words)


def find_word(board, word, used_indices=None):
    if len(word) == 0:
        return True

    used_indices = used_indices or []
    possible_next_indices = get_possible_next_indices(board, used_indices, word)

    for next_index in possible_next_indices:
        word_found = find_word(board, word[1:], used_indices + [next_index])
        if word_found:
            return True
    return False


def get_possible_next_indices(board, used_indices, word):
    return [i for i, letter in enumerate(board) if letter == word[0] and index_is_valid(i, used_indices, board)]


def index_is_valid(index, used_indices, board):
    return not used_indices or (adjacent(index, used_indices[-1], board) and index not in used_indices)


def adjacent(pos1, pos2, board):
    board_size = int(math.sqrt(len(board)))
    return (horizontal_adjacent(pos1, pos2, board_size) or
            vertical_adjacent(pos1, pos2, board_size) or
            diagonal_adjacent(pos1, pos2, board_size))


def horizontal_adjacent(pos1, pos2, board_size):
    return abs(pos1 - pos2) == 1 and pos1 / board_size == pos2 / board_size


def vertical_adjacent(pos1, pos2, board_size):
    return abs(pos1 - pos2) == board_size


def diagonal_adjacent(pos1, pos2, board_size):
    return (abs(pos1 - pos2) == board_size - 1 and pos1 / board_size != pos2 / board_size
          or abs(pos1 - pos2) == board_size + 1)


def print_result(board, user_words):
    print ("Here are your results:")
    score = 0

    for word in user_words:
        if not word:
            continue

        elif not find_word(board, word):
            print (word, 'not on board')

        elif word not in english_dict:
            print (word, 'not in dictionary')

        else:
            print (word, len(word))
            score += len(word)

    print ("Score: ", score)


def main():
    board = [random.choice(cube) for cube in cubes]
    random.shuffle(board)
    print_board(board)
    user_words = get_words_from_user(board)
    print_result(board, user_words)


if __name__ == "__main__":
    main()
