from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """
    Checks if the are some winners in a tic_tac_toe game
    """
    vertical_line = list(zip(board[0], board[1], board[2]))
    diagonal_line_left = [board[0][0], board[1][1], board[2][2]]
    diagonal_line_right = [board[0][2], board[1][1], board[2][0]]
    all_sym_in_board = [i for j in board for i in j]

    def check_three_in_line(boards: List) -> List:
        """Checks if all three values in an array are equal
        Returns a list with indexes of suited arrays"""
        return list(filter(lambda x: len(set(boards[x])) == 1, range(3)))

    def check_x_or_o_array(boards: List) -> bool:
        for elem in check_three_in_line(boards):
            if boards[elem][0] != '-':
                return boards[elem][0] == 'x'

    def check_x_or_o(boards: List) -> bool:
        if boards[0] != '-':
            return boards[0] == 'x'

    # check if x or o wins horizontally
    if any(check_three_in_line(board)) == 1:
        return "x wins!" if check_x_or_o_array(board) else "o wins!"
    # check if x or o wins vertically
    elif any(check_three_in_line(vertical_line)):
        return "x wins!" if check_x_or_o_array(vertical_line) else "o wins!"
    # check if x or o wins in diagonal left
    elif len(set(diagonal_line_left)) == 1:
        return "x wins!" if check_x_or_o(diagonal_line_left) else "o wins!"
    # check if x or o wins in diagonal right
    elif len(set(diagonal_line_right)) == 1:
        return "x wins!" if check_x_or_o(diagonal_line_right) else "o wins!"
    # check if there is a draw
    elif '-' not in all_sym_in_board:
        return 'draw!'
    return 'unfinished!'
