import sys


def my_precious_logger(text: str):
    """
    The func receives a string and write it to stderr
    if line starts with "error"
    and to the stdout otherwise
    """
    if text.startswith('error'):
        return sys.stderr.write(text + '\n')
    return sys.stdout.write(text + '\n')
