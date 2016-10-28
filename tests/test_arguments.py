import pytest
import datetime
import argparse

from ding import ding

# Valid arguments

def test_time_a_second_in_the_past():
    a_second_ago = datetime.datetime.now() - datetime.timedelta(seconds=1)
    time_str = str(a_second_ago.time()).split('.')[0]
    assert ding.get_args(['at', time_str])

def test_time_a_minute_in_the_future():
    a_second_ago = datetime.datetime.now() + datetime.timedelta(minutes=1)
    time_str = str(a_second_ago.time()).split('.')[0]
    assert ding.get_args(['at', time_str])

def test_time_in_1s():
    assert ding.get_args(['in', '1s'])

def test_time_in_1m():
    assert ding.get_args(['in', '1m'])

def test_time_in_1m():
    assert ding.get_args(['in', '1h'])

def test_time_in_1h_1m_1s():
    assert ding.get_args(['in', '1h', '1m', '1s'])

# Invalid arguments
def test_no_arguments():
    with pytest.raises(SystemExit) as excinfo:
        assert ding.get_args([])

def test_insufficient_arguments_in():
    with pytest.raises(SystemExit) as excinfo:
        assert ding.get_args(['in'])

def test_insufficient_arguments_at():
    with pytest.raises(SystemExit) as excinfo:
        assert ding.get_args(['at'])

def test_insufficient_arguments_at():
    with pytest.raises(SystemExit) as excinfo:
        assert ding.get_args(['every'])

def test_in_wrong_suffix():
    with pytest.raises(SystemExit) as excinfo:
        assert ding.get_args(['in', '1x'])

def test_in_partly_wrong_suffix():
    with pytest.raises(SystemExit) as excinfo:
        assert ding.get_args(['in', '1s', '1x'])

def test_at_invalid_separator():
    with pytest.raises(SystemExit) as excinfo:
        assert ding.get_args(['in', '15', '30'])

def test_at_invalid_hour():
    with pytest.raises(SystemExit) as excinfo:
        assert ding.get_args(['at', '25'])

def test_at_invalid_minute():
    with pytest.raises(SystemExit) as excinfo:
        assert ding.get_args(['at', '22:71'])

def test_at_characters_in_string():
    with pytest.raises(SystemExit) as excinfo:
        assert ding.get_args(['at', '22a:71'])

def test_notimer_not_at_end():
    with pytest.raises(SystemExit) as excinfo:
        assert ding.get_args(['--no-timer', 'in', '1s'])

# Test optional args
def test_argument_no_timer():
    assert ding.get_args(['in', '1s', '--no-timer'])
    assert ding.get_args(['in', '1s', '-n'])

def test_argument_alternative_command():
    assert ding.get_args(['in', '1s', '--command', 'beep'])
    assert ding.get_args(['in', '1s', '-c', 'beep'])

def test_argument_inexistent():
    with pytest.raises(SystemExit) as excinfo:
        assert ding.get_args(['in', '1s', '--inexistent-argument'])
