class SimplifiedEnum(type):
    """Removes duplications in variables declarations."""
    def __new__(cls, name: str, bases: tuple, dct: dict):
        for value in dct[f'_{name}__keys']:
            setattr(cls, value, value)
        return super().__new__(cls, name, bases, dct)
