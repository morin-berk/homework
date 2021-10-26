import requests


def html_i_count(url: str) -> int or str:
    """
    Accepts an URL as input and count how many
    letters `i` are present in the HTML by this URL.
    """
    i_counter = 0
    try:
        response = requests.get(url)
    except requests.exceptions:
        raise ValueError("Unreachable {url}")
    if response.status_code == 200:
        for el in response.text:
            if el == 'i':
                i_counter += 1
    return i_counter
