from unittest import mock

from homework4.task2 import html_i_count


@mock.patch('homework4.task2.requests.get')
def test_html_i_count(mock_request):
    """Testing whether the func counts "i" if status_code == 200"""
    mock_request.return_value = mock.Mock(**{'status_code': 200,
                                             'text': 'This is our html'})
    assert html_i_count('smt') == 2
