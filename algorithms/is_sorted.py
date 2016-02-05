from datastructures.stack import stack
from datastructures.binary_tree import binary_tree

def is_sorted(bt):
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

    >>> bt.right.left.set_left(5)
    >>> is_sorted(bt)
    False
    """
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

bt = binary_tree(6)
bt.set_left(2)
bt.left.set_left(1)
bt.left.set_right(4)
bt.left.right.set_left(3)
bt.left.right.set_right(5)
bt.set_right(8)
bt.right.set_left(7)
bt.right.set_right(9)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

