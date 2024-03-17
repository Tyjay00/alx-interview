#!/usr/bin/python3

"""
Solution to the Lockboxes Task 
"""


def canUnlockAll(boxes):
    """
    Checks if the input list is valid and then iterates
    through the boxes to determine if all boxes can be unlocked.
    """
    if type(boxes) is not list:
        return False
    elif len(boxes) == 0:
        return False
    for k in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = k in boxes[idx] and k != idx
            if boxes_checked:
                break
        if not boxes_checked:
            return boxes_checked
    return True
