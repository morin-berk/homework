import sys


def my_precious_logger(text: str):
    """
    The func receives a string and write it to stderr
    if line starts with "error"
    and to the stdout otherwise
    """
    if list(text.split())[0] == 'error':
        return sys.stderr.write(text + '\n')
    return sys.stdout.write(text + '\n')
