#!/usr/bin/env python

import sys
import time
import datetime

EXIT_MSG = 'Invalid arguments. {}'

# A few parameters
N_BEEPS = 4
WAIT_BEEPS = 0.15

class InvalidArguments(Exception):
    pass

def check_input(args):
    # No arguments
    if len(args) < 2 or args[0] not in ['in', 'at']:
        raise InvalidArguments() 

    if args[0] == 'in':
        # Check suffix
        if not all(arg.endswith(('s', 'm', 'h')) for arg in args[1:]):
            raise InvalidArguments() 
        # Check prefix is positive integer
        if not all(arg[:-1].isdigit() for arg in args[1:]):
            raise InvalidArguments() 

    if args[0] == 'at':
        # There should be only one :-separated string
        if len(args) > 2:
            raise InvalidArguments() 

    return args

class TimeParser():
    time_map = {
        's': 1,
        'm': 60,
        'h': 60 * 60,
    }

    def __init__(self, time, relative):
        self.time = time or sys.exit(EXIT_MSG)
        self.relative = relative

    def get_seconds(self):
        return self._get_seconds_relative() if self.relative else self._get_seconds_absolute()

    def _get_seconds_relative(self):
        return sum([self.time_map[t[-1]] *  int(t[:-1]) for t in self.time])

    def _get_seconds_absolute(self):
        try:
            user_time = datetime.datetime.combine(datetime.date.today(), datetime.time(*map(int, self.time[0].split(':'))))
        except ValueError as e:
            raise InvalidArguments(e)
        now = datetime.datetime.now()
        if user_time < now:
            raise InvalidArguments('The time provided must be in the future')
        return (user_time - now).seconds 


def beep(seconds):
    time.sleep(seconds)
    for i in range(N_BEEPS):
        sys.stdout.write('\a')
        sys.stdout.flush()
        time.sleep(WAIT_BEEPS)


def parse_time(args):
    relative = True if args[0] == 'in' else False
    user_time = args[1:]
    parser = TimeParser(user_time, relative)
    return parser.get_seconds()


def main(args=sys.argv[1:]):
    try:
        seconds = parse_time(check_input(args))
    except InvalidArguments as e:
        sys.exit(EXIT_MSG.format(e))
    beep(seconds)

if __name__ == '__main__':
    main()
