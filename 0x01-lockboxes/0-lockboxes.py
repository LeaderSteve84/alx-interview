#!/usr/bin/python3
"""module whose function Return True if all
boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened.
    Args:
        boxes (any): a list of lists.
        Return: True if all boxes can be opened, else return False.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    queue = [0]  # Start with the first box (index 0)
    visited[0] = True  # Mark the first box as visited

    while queue:
        current_box = queue.pop(0)  # Dequee the first box from the queue

        for key in boxes[current_box]:  # Check all keys in the current box
            # Ensure key is a valid box index and not visited
            if 0 <= key < n and not visited[key]:
                # Add the box corresponding to the key to the key to the queue
                queue.append(key)
                visited[key] = True  # Mark the box visited

    # check if all boxex have been visited
    return all(visited)
