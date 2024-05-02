#!/usr/bin/python3
from collections import deque


def canUnlockAll(boxes):
    n = len(boxes)
    visited = set()
    visited.add(0)
    keys_queue = deque(boxes[0])

    while keys_queue:
        key = keys_queue.popleft()
        if key < n and key not in visited:
            visited.add(key)
            keys_queue.extend(boxes[key])

    return len(visited) == n
