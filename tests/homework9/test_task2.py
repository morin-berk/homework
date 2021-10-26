import pytest

from homework9.task2 import SupressorClass, supressor_func


def test_supressor_class_positive():
    x = []
    with SupressorClass(ValueError):
        x.append(1)
    assert x == [1]


def test_supressor_class_negative():
    with pytest.raises(IndexError):
        with SupressorClass(ValueError):
            [][2]


def test_supressor_func_positive():
    x = []
    with supressor_func(ValueError):
        x.append(1)
    assert x == [1]


def test_supressor_func_negative():
    with pytest.raises(IndexError):
        with supressor_func(ValueError):
            [][2]


def test_supressor_class_index_error():
    with SupressorClass(IndexError):
        [0][2]


def test_supressor_func_index_error():
    with supressor_func(IndexError):
        [0][2]


def test_supressor_class_type_error():
    with SupressorClass(TypeError):
        'a' + 1


def test_supressor_func_type_error():
    with supressor_func(TypeError):
        'a' + 1


def test_supressor_class_zero_division_error():
    with SupressorClass(ZeroDivisionError):
        1 / 0


def test_supressor_func_zero_division_error():
    with supressor_func(ZeroDivisionError):
        1 / 0


def test_supressor_class_attribute_error():
    x = 10
    with SupressorClass(AttributeError):
        x.append(1)


def test_supressor_func_attribute_error():
    x = 10
    with supressor_func(AttributeError):
        x.append(1)
