import pytest

from ding import ding


def test_tool_no_arguments():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input([])

def test_tool_insufficient_arguments_in():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['in'])

def test_tool_insufficient_arguments_at():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['at'])

def test_tool_in_wrong_suffix():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['in 1x'])

def test_tool_in_partly_wrong_suffix():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['in 1s 1x'])

def test_tool_at_invalid_separator():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['in 15 30'])

def test_tool_at_invalid_hour():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['in 25'])

def test_tool_at_invalid_minute():
    with pytest.raises(ding.InvalidArguments) as excinfo:
        x = ding.check_input(['at 22:71'])
