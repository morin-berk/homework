from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """
    Takes directory path, a file extension and an optional tokenizer.
    Counts lines in all files with that extension if there are no tokenizer.
    If a the tokenizer is not none, it counts tokens.
    """
    count = 0
    for file in Path(dir_path).glob("*." + file_extension):
        if not tokenizer:
            with open(file, 'r') as f:
                count += sum(1 for _ in f)
        else:
            with open(file, 'r') as f:
                count += sum(1 for _ in tokenizer(f.read()))
    return count
