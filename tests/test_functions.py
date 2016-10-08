from datetime import datetime, timedelta
import argparse

import pytest
from ding import ding

def test_time_parser_relative_1s():
    parser = ding.TimeParser(['1s'], relative=True)
    assert parser.get_seconds() == 1

def test_time_parser_relative_1m():
    parser = ding.TimeParser(['1m'], relative=True)
    assert parser.get_seconds() == 60

def test_time_parser_relative_1h():
    parser = ding.TimeParser(['1h'], relative=True)
    assert parser.get_seconds() == 60 * 60

def test_time_parser_relative_1h_30m():
    parser = ding.TimeParser(['1h', '30m'], relative=True)
    assert parser.get_seconds() == 60 * 60 + 30 * 60

def test_time_parser_relative_1h_30m():
    parser = ding.TimeParser(['1h', '30m'], relative=True)
    assert parser.get_seconds() == 60 * 60 + 30 * 60

def test_time_parser_relative_1h_30m_10s():
    parser = ding.TimeParser(['1h', '30m', '10s'], relative=True)
    assert parser.get_seconds() == 60 * 60 + 30 * 60 + 10

def test_time_parser_absolute_10s():
    new_time = str((datetime.now() + timedelta(seconds=10)).time()).split('.')[0]
    parser = ding.TimeParser(new_time, relative=False)
    assert abs(parser.get_seconds() - 10) < 2

def test_time_parser_absolute_1h():
    new_hour = str((datetime.now() + timedelta(hours=1)).hour)
    parser = ding.TimeParser(new_hour, relative=False)
    assert 0 < parser.get_seconds() < 60 * 60

def test_time_parser_absolute_5m():
    new_time = ':'.join(str((datetime.now() + timedelta(minutes=5)).time()).split(':')[:2])
    parser = ding.TimeParser(new_time, relative=False)
    assert 60 * 4 <= parser.get_seconds() < 60 * 6

def test_relative_time_regex_very_wrong_regex():
    with pytest.raises(argparse.ArgumentTypeError)as excinfo:
        ding.relative_time('this is very wrong')

def test_relative_time_regex_1s():
     assert ding.relative_time('1s')

def test_relative_time_regex_h_m_s():
     assert ding.relative_time('12h 12m 34s')

def test_relative_time_regex_extra_space():
     assert ding.relative_time('12h           12m')

def test_absolute_time_hh_mm_ss():
    assert ding.absolute_time('12:12:12')

def test_absolute_time_hh():
    assert ding.absolute_time('12')

def test_absolute_time_hh_mm_ss_invalid_hour():
    with pytest.raises(argparse.ArgumentTypeError)as excinfo:
        assert ding.absolute_time('32:12:12')

def test_beep_with_custom_command(capfd):
    ding.beep(1, 'echo "test"')
    out, err = capfd.readouterr()
    assert out == 'test\n' * ding.N_BEEPS
