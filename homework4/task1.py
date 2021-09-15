def read_magic_number(path: str) -> bool:
    """
    The func opens a file and checks
    whether the first line data is int,
    if yes, whether it belongs to [1, 3)
    """
    try:
        with open(path, 'r', encoding='utf8') as file:
            first_line = file.readline()
            if not int(first_line):
                raise ValueError('The first line is not int')
            if 1 <= int(first_line) < 3:
                return True
            return False
    except FileNotFoundError:
        print('Cannot find the file')
