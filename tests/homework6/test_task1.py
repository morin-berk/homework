from homework6.task1 import User, instances_counter


def test_new_class_inhereted_from_decorated_class():
    """
    Testing a new class inhereting from class
    decorated by the instances_counter func.
    """
    class New(User):
        """An experimental class"""

    assert New.get_created_instances() == 0
    new, _ = New(), New()
    assert new.get_created_instances() == 2
    assert new.reset_instances_counter() == 2
    assert new.get_created_instances() == 0


def test_class_with_init():
    """
    Testing if a class decorated by the instances_counter func
    with __init__() behaves as expected.
    """
    @instances_counter
    class New:
        def __init__(self, some_arg: str, other_arg: int):
            self.some_arg = some_arg
            self.other_arg = other_arg

    assert New.get_created_instances() == 0
    new, _ = New('something', 1), New('new', 1)
    assert new.get_created_instances() == 2
    assert new.reset_instances_counter() == 2
    assert new.get_created_instances() == 0


def test_class_with_methods():
    """
    Testing if a class decorated by the instances_counter func
    with __init__() and some_method() behaves as expected.
    """
    @instances_counter
    class New:
        def __init__(self, other_arg: int):
            self.other_arg = other_arg

        def some_method(self, arg: int) -> int:
            return arg + self.other_arg

    new, _ = New(1), New(2)
    assert new.get_created_instances() == 2
    assert new.reset_instances_counter() == 2
    assert new.some_method(10) == 11
