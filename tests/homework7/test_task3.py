import pytest

from homework7.task3 import tic_tac_toe_checker


@pytest.mark.parametrize('board, expected',
                         [([['o', '-', 'o'],
                            ['-', 'o', 'o'],
                            ['x', 'x', 'x']], 'x wins!'),
                          ([['o', '-', 'o'],
                            ['o', 'o', 'o'],
                            ['x', 'x', '-']], 'o wins!')])
def test_wins_horizontally(board, expected):
    """
    Cases when there are three x or o horizontally
    """
    assert tic_tac_toe_checker(board) == expected


@pytest.mark.parametrize('board, expected',
                         [([['o', '-', 'o'],
                            ['-', 'o', 'o'],
                            ['x', 'x', 'o']], 'o wins!'),
                          ([['o', 'x', 'o'],
                            ['o', 'x', 'o'],
                            ['x', 'x', '-']], 'x wins!')])
def test_wins_vertically(board, expected):
    """
    Cases when there are three x or o vertically
    """
    assert tic_tac_toe_checker(board) == expected


@pytest.mark.parametrize('board, expected',
                         [([['o', '-', 'x'],
                            ['-', 'o', 'o'],
                            ['x', 'x', 'o']], 'o wins!'),
                          ([['o', 'o', 'x'],
                            ['o', 'x', 'o'],
                            ['x', 'x', 'o']], 'x wins!')])
def test_wins_diagonally(board, expected):
    """
    Cases when there are three x or o diagonally
    """
    assert tic_tac_toe_checker(board) == expected


def test_wins_draw():
    """
    Case when there is a draw
    """
    assert tic_tac_toe_checker([['o', 'o', 'x'],
                                ['x', 'o', 'o'],
                                ['o', 'x', 'x']]) == 'draw!'


def test_unfinished():
    """
    Unfinished case
    """
    assert tic_tac_toe_checker([['-', '-', 'o'],
                                ['-', 'x', 'o'],
                                ['x', 'o', 'x']]) == 'unfinished!'
