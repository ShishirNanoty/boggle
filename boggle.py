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
    board = [letters[i] + '\n' if (i + 1) % board_size == 0 else letters[i] for i in xrange(len(letters))]
    print ' ' + ' '.join(board)

    # for i in xrange(len(letters)):
    #
    #
    #     print letters[i],
    #     if (i + 1) % board_size == 0:
    #         print


def main():
    letters = [random.choice(cube) for cube in cubes]
    random.shuffle(letters)
    print_board(letters)

main()


