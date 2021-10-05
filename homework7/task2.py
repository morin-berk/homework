def backspace_compare(first: str, second: str) -> bool:
    """Given two strings, the func returns if they are equal
    when both are typed into empty text editors."""

    def clear_string(string: str) -> str:
        string = [sym.replace(string[k], '').replace(string[k - 1], '')
                  if sym == "#" else sym for k, sym in enumerate(string)]
        return ''.join(string)

    return clear_string(first) == clear_string(second)
