#!/usr/bin/python3
""" Log parsing """
import sys

allowed_scode = {200, 301, 400, 401, 403, 404, 405, 500}


def line_in(line):
    """ function process each line
    returns status code and the file size
    """
    parts = line.split()
    if len(parts) < 7:
        return None, None
    try:
        s_code = int(parts[-2])
        f_size = int(parts[-1])
        return s_code, f_size
    except (ValueError, IndexError):
        return None, None


def print_stats(total_fs, s_code_count):
    """ Prints the statistics """
    print("File size: {}".format(total_fs))
    for code, count in sorted(s_code_count.items()):
        print("{}: {}".format(code, count))


try:
    """ Prints stats from stdin """
    total_fs = 0
    s_code_count = {}

    line_count = 0
    for line in sys.stdin:
        s_code, f_size = line_in(line.rstrip())
        if s_code is not None and f_size is not None:
            total_fs += f_size
            if s_code in allowed_scode:
                s_code_count[s_code] = s_code_count.get(s_code, 0) + 1

        line_count += 1

        if line_count == 10:
            print_stats(total_fs, s_code_count)
            line_count = 0
except KeyboardInterrupt:
    print_stats(total_fs, s_code_count)
    raise

print_stats(total_fs, s_code_count)
