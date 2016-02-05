"""Runs in-order iterative depth-first search through a binary tree,
    to check if the nodes are correctly ordered.

Objectives:
    O(m + n) running time

Args:
    bt: a binary tree, with nodes encoded as integers.

Returns:
    True if the elements of the tree are sorted, False otherwise.

>>> bt = binary_tree(6)
>>> bt.set_left(2)
>>> bt.left.set_left(1)
>>> bt.left.set_right(4)
>>> bt.left.right.set_left(3)
>>> bt.left.right.set_right(5)
>>> bt.set_right(8)
>>> bt.right.set_left(7)
>>> bt.right.set_right(9)
>>> is_sorted(bt)
True

>>> bt.right.set_left(5)
>>> is_sorted(bt)
False
"""

from datastructures.stack import stack
from datastructures.binary_tree import binary_tree

# My Implementation
def my_is_sorted(bt):
    s = stack()
    explored = set()
    curr_max = 0

    s.push(bt)
    while not s.is_empty:
        curr_node = s.peek()
        explored.add(curr_node)

        # Explore left subtree
        if curr_node.left is not None and curr_node.left not in explored:
            s.push(curr_node.left)
            continue

        # Compare to max
        if curr_node.right not in explored:
            if curr_node.value < curr_max:
                return False
            else:
                curr_max = curr_node.value

        # Explore right subtree
        if curr_node.right is not None and curr_node.right not in explored:
            s.push(curr_node.right)
            continue

        # All children explored
        s.pop()

    return True

### Canonical Implementation
def canonical_is_sorted(node):
    s = stack()
    curr_max = 0

    while not s.is_empty or node is not None:
        if node is not None:
            s.push(node)
            node = node.left
        else:
            node = s.pop()

            if node.value < curr_max:
                return False
            else:
                curr_max = node.value

            node = node.right
    return True

is_sorted = my_is_sorted
# is_sorted = canonical_is_sorted

if __name__ == "__main__":
    import doctest
    doctest.testmod()

