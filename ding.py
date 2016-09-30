#!/usr/bin/env python

import sys
import time
import datetime

EXIT_MSG = 'Invalid arguments'

# A few parameters
N_BEEPS = 4
WAIT_BEEPS = 0.15

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
        user_time = datetime.datetime.combine(datetime.date.today(), datetime.time(*map(int, self.time[0].split(':'))))
        now = datetime.datetime.now()
        return (user_time - now).seconds if user_time > now else sys.exit('The time provided must be in the future')


def beep(seconds):
    time.sleep(seconds)
    for i in range(N_BEEPS):
        sys.stdout.write('\a')
        sys.stdout.flush()
        time.sleep(WAIT_BEEPS)


def parse_time(args):
    try:
        relative = True if args[0] == 'in' else False if args[0] == 'at' else sys.exit(EXIT_MSG)
    except IndexError:
        sys.exit(EXIT_MSG)
    user_time = args[1:]
    parser = TimeParser(user_time, relative)
    return parser.get_seconds()


def main():
    seconds = parse_time(sys.argv[1:])
    beep(seconds)

if __name__ == '__main__':
    main()
