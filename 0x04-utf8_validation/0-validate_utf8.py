#!/usr/bin/python3
"""
validUTF8
"""


def validUTF8(data):
    """Number of bytes in the current UTF-8 character"""
    num_bytes = 0

    # Masks to check the most significant bits of a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate over each integer in the data list
    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & num:
                num_bytes += 1
                mask = mask >> 1

            # 1 byte character
            if num_bytes == 0:
                continue

            # If num_bytes is more than 4 or 1, it's invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the next byte starts with '10'
            if not (num & mask1 and not (num & mask2)):
                return False

        num_bytes -= 1

    # If we finish and num_bytes is not 0, then it's invalid
    return num_bytes == 0
