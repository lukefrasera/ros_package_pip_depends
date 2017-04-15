from __future__ import print_function
from tzlocal import get_localzone


def main():
    print('Execute example script with pip depends.')
    tz = get_localzone()
    print(tz)
    return 0
