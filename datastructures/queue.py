class queue(object):
    '''Python queue implementation

    Objectives:
        O(1) push
        O(1) pop

    >>> q = queue(reset_limit=4)
    >>> q.push('a')
    >>> q.push('b')
    >>> q.push('c')
    >>> q.push('d')
    >>> q.push('e')
    >>> q.push('f')
    >>> q.size
    6
    >>> q.pop()
    'a'
    >>> q.pop()
    'b'
    >>> q.pop()
    'c'
    >>> q.size
    3
    >>> q.pop()
    'd'
    >>> q.pop()
    'e'
    >>> q.pop()
    'f'
    >>> q.size
    0
    '''
    def __init__(self, reset_limit=20):
        self._limit = reset_limit
        self._array = []
        self._head = 0

    def __repr__(self):
        return 'Queue: [{}]'.format(self._array)

    @property
    def size(self):
        return len(self._array) - self._head

    def pop(self):
        el = self._array[self._head]
        self._head += 1
        if self._head > self._limit:
            self._reset()
        return el

    def _reset(self):
        self._array = self._array[self._head:]
        self._head = 0

    def push(self, el):
        self._array.append(el)


if __name__ == "__main__":
    import doctest
    doctest.testmod()