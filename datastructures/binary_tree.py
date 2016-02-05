class binary_tree(object):
    '''
    Python binary tree implementation.

    >>> mytree = binary_tree('cat')
    >>> mytree.left = binary_tree('ape')
    >>> mytree.set_right('dog')
    >>> mytree.right.set_right('gorilla')
    >>> mytree.right.set_left('chimpanzee')
    >>> mytree.right.value
    'dog'
    >>> mytree.right.left.value
    'chimpanzee'
    >>> mytree.left.value
    'ape'
    '''
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return 'node({})'.format(self.value)

    def set_left(self, value):
        if isinstance(value, binary_tree):
            self.left = value
        else:
            self.left = binary_tree(value)

    def set_right(self, value):
        if isinstance(value, binary_tree):
            self.right = value
        else:
            self.right = binary_tree(value)


if __name__ == "__main__":
    import doctest
    doctest.testmod()