from typing import Union


class KeyValueStorage:
    """This is a wrapper for key-value storage, which has its keys
    and values accessible as collection items and as attributes"""
    def __init__(self, file_path: str):
        self.storage = {}
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip().split('=')
                self.storage[line[0]] = line[1]
        for key, value in self.storage.items():
            if value.isdigit():
                self.storage[key] = int(value)
            if key.isdigit():
                raise ValueError("Int cannot be an attribute")

    def __getitem__(self, item: str) -> Union[str, int]:
        return self.storage[item]

    def __getattr__(self, item: str) -> Union[str, int]:
        if item in self.storage:
            return self.storage[item]
        raise AttributeError("No such attribute: " + item)
