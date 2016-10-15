import boggle
import pytest

@pytest.mark.parametrize('pos1, pos2, board_size', [
    (0, 1, 5),
    (1, 0, 5),
])
def test_horizontal_adjacent_1(pos1, pos2, board_size):
    # when
    result = boggle.horizontal_adjacent(pos1, pos2, board_size)

    # then
    assert result


def test_horizontal_adjacent_2():
    # given
    position1 = 0
    position2 = 1
    board_size = 5

    # when
    result = boggle.horizontal_adjacent(position1, position2, board_size)

    # then
    assert result


def test_horizontal_adjacent_tuples():
    # given
    params = [(0, 1, 5), (2, 3, 5), (4, 3, 5)]

    # when
    for p in params:
        result = boggle.horizontal_adjacent(*p)

        # then
        assert result


def test_horizontal_adjacent_list_comprehension():
    # given
    params = [(0, 1, 5), (2, 3, 5), (4, 3, 5)]

    # when
    results = [boggle.horizontal_adjacent(*p) for p in params]

    # then
    assert sum(results) == len(params)
