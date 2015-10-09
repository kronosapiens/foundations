class binheap(object):
    '''
    Implementation of a binary min/max heap.

    Objectives:
        O(logn) insert
        O(logn) extract

    Details:
        Functions assume indices starting at 1. Actual array access
        occurs inside the _compare and _swap functions, where indices are
        adjusted.

    >>> bh = binheap([4, 2, 9, 1]) # Should become [1, 2, 4, 9]
    >>> bh.extract()
    1
    >>> bh.extract()
    2
    >>> bh.insert(3)
    >>> bh.extract()
    3
    >>> bh.insert(5)
    >>> bh.extract()
    4
    '''
    def __init__(self, data, kind='min'):
        self._kind = kind
        self._heap = []
        self._construct_heap(data)

    def _compare(self, a, b):
        if self._kind == 'min':
            return self._heap[a-1] <= self._heap[b-1]
        else:
            return self._heap[a-1] >= self._heap[b-1]

    def _swap(self, a, b):
        temp = self._heap[a-1]
        self._heap[a-1] = self._heap[b-1]
        self._heap[b-1] = temp

    def insert(self, node):
        self._heap.append(node)
        self._bubble_up(len(self._heap))

    def extract(self):
        root = self._heap[0]
        leaf = self._heap.pop()
        self._heap[0] = leaf
        self._bubble_down(0)
        return root

    def _bubble_up(self, child):
        if child > 1:
            parent = child/2
            if self._compare(child, parent):
                self._swap(child, parent)
                self._bubble_up(parent)

    def _bubble_down(self, root):
        '''Wikipedia implementation, helper functions my own.
        '''
        size = len(self._heap)
        winner = root
        right = root*2
        left = root*2+1

        if left <= size and self._compare(left, winner):
            winner = left
        if right <= size and self._compare(right, winner):
            winner = right

        if winner != root:
            self._swap(winner, root)
            self._bubble_down(winner)

    def _construct_heap(self, data):
        for datum in data:
            self.insert(datum)


if __name__ == "__main__":
    import doctest
    doctest.testmod()