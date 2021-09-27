from homework6.task1 import User


def test_new_class_inhereted_from_decorated_class():
    """
    Checking if a new class inhereting from class
    decorated by the instances_counter func
    behaves as expected: has a counter of objects,
    get_created_instances, and reset_instances_counter methods
    """
    class New(User):
        """An experimental class"""

    assert New.get_created_instances() == 0
    new, _ = New(), New()
    assert new.get_created_instances() == 2
    assert new.reset_instances_counter() == 2
    assert new.get_created_instances() == 0
