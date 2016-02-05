"""Runs in-order iterative depth-first search through a binary tree,
    to check if the nodes are correctly ordered.

Objectives:
    O(m + n) running time

Args:
    bt: a binary tree, with nodes encoded as integers.

Returns:
    True if the elements of the tree are sorted, False otherwise.

Notes:
    My implemention performed some bookkeping and leaf-checking which
    the canonical implementation completely avoided. This was
    accomplished by separating the updating of the 'node' variable
    from the pushing of nodes onto the stack, allowing for None leaves
    to be treated as ordinary nodes. Also, the canonical version avoids
    visiting nodes twice, which it accomplishes by popping a node from
    the stack before considering its right child.

    While implementing this, I began with the assumption that I would need
    to maintain an explicit stack, and pop parents from the stack only once
    I had traversed both of their child subtrees. Looking at the canonical
    implementation, this assumption was incorrect. Upon reflection, I had
    been incorrectly remembering lessons from algorithms class, in which we
    used DFS to achieve topological sorting by recording the times in which
    nodes were popped and pushed from the stack.

    Key takeaways are that special None handling can be unecessary and that
    considering None as a first-class object (in this case, as a node)
    can result in more succint code. Also, that while there may seem
    to be a 1:1 relationship between the start/end of loops and
    popping/pushing from a stack or queue, these operations may be
    seperable, and in such cases such separation can allow for a wider
    variety of behaviors to be encoded in fewer lines. Finally, a class of
    algorithm can be implemented in different ways depending on
    the specifics of the problem.

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

