import pytest

from homework3.task3 import make_filter

sample_data = [
     {
         "name": "Bill",
         "last_name": "Gilbert",
         "occupation": "was here",
         "type": "person",
     },
     {
         "is_dead": True,
         "kind": "parrot",
         "type": "bird",
         "name": "polly"
     }
]


@pytest.mark.parametrize('test_input, expected',
                         [({'name': 'polly', 'type': 'bird'},
                           [sample_data[1]]),
                          ({'name': 'Bill'}, [sample_data[0]]),
                          ({'name': 'polly', 'type': 'person'}, []),
                          ({'name': 'Billy'}, [])])
def test_different_cases(test_input, expected):
    """Testing positive and negative cases"""
    assert make_filter(**test_input).apply(sample_data) == expected
