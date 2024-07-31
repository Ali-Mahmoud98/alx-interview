#!/usr/bin/python3
"""0-lockboxes module"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened given a list of boxes,
    where each box contains a list of keys.

    Each box in the `boxes` list contains a list of keys that can
    be used to open other boxes. The function starts with the first
    box (index 0) and tries to open as many boxes as possible using
    the keys found in the currently accessible boxes. It keeps track
    of all the boxes that can be opened using a set of keys.

    The function returns True if all boxes can be opened (i.e., all
    boxes can be accessed starting from the first box); otherwise,
    it returns False.

    Parameters:
    boxes (List[List[int]]): A list of lists where each inner list
    represents a box and contains integers indicating the indices
    of other boxes that can be opened with the keys in the current box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    total_boxes = len(boxes)
    setofkeys = [0]
    counter = 0
    index = 0

    while index < len(setofkeys):
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in setofkeys:
                setofkeys.append(key)
                counter += 1
        index += 1

    return counter == total_boxes - 1
