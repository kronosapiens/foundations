import linkedlist

class dict(object):
    '''Python dict implementation (hash table)

    Objectives:
        O(1) lookup (average case)
        O(1) write (average case)

        O(n) lookup (worst case)
        O(n) write (worst case)

        No implicit memory allocation

    Implementation rules:
        - Nodes cannot have None content, EXCEPT for first node at idx=i.

    >>> mydict = dict()
    >>> mydict.set('cat', 'meow')
    >>> mydict.get('cat')
    'meow'

    >>> mydict.set('cat', 'purr')
    >>> mydict.get('cat')
    'purr'

    >>> mydict.get('dog')
    Traceback (most recent call last):
    KeyError: "Key 'dog' not found!"

    >>> mydict.set('dog', 'woof')
    >>> mydict.get('dog')
    'woof'

    >>> mydict.size == len(mydict.data)
    True
    '''
    def __init__(self, size=50):
        self.size = size
        self.data = [None for _ in xrange(size)] # Initialize to "fixed" width

    def set(self, key, value):
        raise NotImplemented() # See implementations below

    def get(self, key):
        raise NotImplemented() # See implementations below

    def _get_index(self, key):
        return hash(key) % self.size


    ##############################
    ### LINKED LIST IMPLEMENTATION
    ##############################

    # [node|->](key, value)

    def set(self, key, value):
        node = self._get_sublist(key)

        # If first node at idx=i
        if not node.has_content:
            node.content = (key, value)
            return

        # If existing nodes at idx=i
        last = None
        while node is not None:
            if self._check_key(node, key):
                node.content = (key, value)
                return
            last = node
            node = node.next
        last.next = linkedlist.node((key, value))

    def get(self, key):
        node = self._get_sublist(key)
        while node is not None:
            if self._check_key(node, key):
                return self._get_value(node)
            else:
                node = node.next
        raise KeyError('Key \'{}\' not found!'.format(key))

    def _get_sublist(self, key):
        idx = self._get_index(key)
        if self.data[idx] is None:
            self.data[idx] = linkedlist.node()
        return self.data[idx]

    def _check_key(self, node, key):
        if node.has_content:
            k, v = node.content
            return k == key

    def _get_value(self, node):
        k, v = node.content
        return v


    ########################
    ### ARRAY IMPLEMENTATION
    ########################
    # def set(self, key, value):
    #     subarray = self._get_subarray(key)
    #     for i in xrange(len(subarray)):
    #         k,v = subarray[i]
    #         if k == key:
    #             subarray[i] = (key, value)
    #             return

    #     subarray.append((key, value))

    # def get(self, key):
    #     subarray = self._get_subarray(key)
    #     for k, v in subarray:
    #         if k == key:
    #             return v
    #     raise KeyError('Key \'{}\' not found!'.format(key))

    # def _get_subarray(self, key):
    #     idx = self._get_index(key)
    #     if self.data[idx] is None:
    #         self.data[idx] = []
    #     return self.data[idx]


if __name__ == "__main__":
    import doctest
    doctest.testmod()