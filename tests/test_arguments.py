import pytest
import datetime

from ding import ding

# Valid arguments

def test_time_a_second_in_the_past():
    a_second_ago = datetime.datetime.now() - datetime.timedelta(seconds=1)
    time_str = str(a_second_ago.time()).split('.')[0]
    assert ding.check_input(['at', time_str])

def test_time_a_minute_in_the_future():
    a_second_ago = datetime.datetime.now() + datetime.timedelta(minutes=1)
    time_str = str(a_second_ago.time()).split('.')[0]
    assert ding.check_input(['at', time_str])

def test_time_in_1s():
    assert ding.check_input(['in', '1s'])

def test_time_in_1m():
    assert ding.check_input(['in', '1m'])

def test_time_in_1m():
    assert ding.check_input(['in', '1h'])

def test_time_in_1h_1m_1s():
    assert ding.check_input(['in', '1h', '1m', '1s'])

# Invalid arguments
def test_no_arguments():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input([])

def test_insufficient_arguments_in():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['in'])

def test_insufficient_arguments_at():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['at'])

def test_in_wrong_suffix():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['in', '1x'])

def test_in_partly_wrong_suffix():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['in', '1s', '1x'])

def test_at_invalid_separator():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['in', '15', '30'])

def test_at_invalid_hour():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['at', '25'])

def test_at_invalid_minute():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['at', '22:71'])

def test_at_characters_in_string():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['at', '22a:71'])

def test_notimer_not_at_end():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['--no-timer', 'in', '1s'])
