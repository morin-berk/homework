from homework4.task3 import my_precious_logger


def test_my_precious_logger_stdout(capsys):
    """
    Testing that str, not starting from 'error',
    goes through stdout
    """
    my_precious_logger('there is no error')
    captured = capsys.readouterr()
    assert captured.out == "there is no error\n"


def test_my_precious_logger_stderr(capsys):
    """
    Testing that str, starting from 'error',
    goes through stderr
    """
    my_precious_logger('error not found')
    captured = capsys.readouterr()
    assert captured.err == "error not found\n"
