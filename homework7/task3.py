from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """Checks if the are some winners in a tic_tac_toe game."""
    all_sym_in_board = [i for j in board for i in j]
    vertical_line = list(zip(board[0], board[1], board[2]))
    diagonal_line_left = list(k for k in all_sym_in_board[::4])
    diagonal_line_right = list(k for k in all_sym_in_board[2:7:2])

    def find_three_equal_values(boards: List) -> List:
        """Checks if all three values in an array are equal.
        Returns a list with indexes of suited arrays."""
        return list(filter(lambda x: len(set(boards[x])) == 1
                    and set(boards[x]) != '-', range(3)))

    def check_x_or_o(boards: List) -> bool:
        if boards[0] != '-':
            return boards[0] == 'x'

    horizontal = find_three_equal_values(board)
    vertical = find_three_equal_values(vertical_line)

    if horizontal:
        return "x wins!" if board[horizontal[0]][0] == 'x' else "o wins!"
    elif vertical:
        return "x wins!" if vertical_line[vertical[0]][0] == 'x' else "o wins!"
    elif len(set(diagonal_line_left)) == 1:
        return "x wins!" if check_x_or_o(diagonal_line_left) else "o wins!"
    elif len(set(diagonal_line_right)) == 1:
        return "x wins!" if check_x_or_o(diagonal_line_right) else "o wins!"
    elif '-' not in all_sym_in_board:
        return 'draw!'
    return 'unfinished!'
