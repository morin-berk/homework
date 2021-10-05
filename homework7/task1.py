from typing import Any, Iterable

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


def find_occurrences(tree: dict, element: Any) -> int:
    """Recursive func walks through any(dict, set, tuple, list)
    and counts number of element occurrences with
    nonlocal counter."""
    counter = 0

    def find_occurrences_recursive(tree: Any) -> Any:
        nonlocal counter
        if isinstance(tree, dict):
            for key, value in tree.items():
                if key == element:
                    counter += 1
                find_occurrences_recursive(value)
        elif isinstance(tree, Iterable) and not isinstance(tree, str):
            for k in tree:
                find_occurrences_recursive(k)
        if tree == element:
            counter += 1

    find_occurrences_recursive(tree)
    return counter


if __name__ == '__main__':
    print(find_occurrences(example_tree, "RED"))  # 6
