#!/usr/bin/python3
import sys


def line_in(line):
    """ function process each line
    returns status code and the file size
    """
    parts = line.split()
    s_code = int(parts[-2])
    f_size = int(parts[-1])
    return s_code, f_size


def print_stats(total_fs, s_code_count):
    """ Prints the statistics """
    print("File size: {}".format(total_fs))
    for code, count in sorted(s_code_count.items()):
        print("{}: {}".format(code, count))
    sys.stdout.flush()


def stats():
    """ Prints stats from stdin """
    total_fs = 0
    s_code_count = {}

    try:
        line_count = 0
        for line in sys.stdin:
            s_code, f_size = line_in(line.rstrip())
            if s_code is not None and f_size is not None:
                total_fs += f_size
                s_code_count[s_code] = s_code_count.get(s_code, 0) + 1

            line_count += 1

            if line_count == 10:
                print_stats(total_fs, s_code_count)
                line_count = 0
                total_fs = 0
                s_code_count = {}
    except KeyboardInterrupt:
        print_stats(total_fs, s_code_count)
        raise


if __name__ == '__main__':
    stats()
