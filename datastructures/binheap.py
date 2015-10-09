class binheap(object):
    '''
    Implementation of a binary min/max heap.

    Objectives:
        O(logn) insert
        O(logn) extract

    Details and Abstractions:
        - Functions assume indices starting at 1. Actual array access
        occurs inside the _compare and _swap functions, where indices are
        adjusted.
        - Heap manipulation uses indices (integers) to represent nodes.
        Actual node contents are handled in _compare and _swap.

    >>> bh = binheap([4, 2, 9, 1])
    >>> bh.extract()
    1
    >>> bh.extract()
    2
    >>> bh.insert(3)
    >>> bh.extract()
    3
    >>> bh.insert(10)
    >>> bh.extract()
    4
    >>> bh.update(9, 0)
    >>> bh.extract()
    0
    '''
    def __init__(self, data, fkey=None, fval=None, kind='min'):
        self._kind = kind
        self.fval = fval if (fval is not None) else lambda x: x
        self.fkey = fkey if (fkey is not None) else lambda x: x
        self._heap = []
        self._location = {}
        self._construct_heap(data)

    @property
    def size(self):
        return len(self._heap)

    def _compare(self, a, b):
        '''True result means a is preferred to b given comparison operator.
        '''
        f, heap = self.fval, self._heap
        if self._kind == 'min':
            return f(heap[a-1]) <= f(heap[b-1])
        else:
            return f(heap[a-1]) >= f(heap[b-1])

    def _find(self, key):
        return self._location[key]+1 # From 0-index to 1-index

    def _replace(self, idx, new):
        self._heap[idx-1] = new

    def insert(self, node):
        self._heap.append(node)
        self._location[self.fkey(node)] = self.size
        self._bubble_up(self.size)

    def peek(self):
        return self._heap[0]

    def extract(self):
        root = self.peek()
        leaf = self._heap.pop()
        self._heap[0] = leaf
        self._bubble_down(0)
        del self._location[self.fkey(root)]
        return root

    def update(self, new):
        node = self._find(self.fkey(new))
        self._replace(node, new)
        parent = node/2
        if self._compare(node, parent):
            self._bubble_up(node)
        else:
            self._bubble_down(node)

    def _swap(self, a, b):
        f, heap, location = self.fkey, self._heap, self._location
        a_val = heap[a-1]
        b_val = heap[b-1]
        heap[a-1] = b_val
        heap[b-1] = a_val
        location[f(a_val)] = b-1
        location[f(b_val)] = a-1

    def _bubble_up(self, child):
        if child > 1:
            parent = child/2
            if self._compare(child, parent):
                self._swap(child, parent)
                self._bubble_up(parent)

    def _bubble_down(self, root):
        '''Wikipedia implementation, helper functions my own.
        '''
        winner = root
        right = root*2
        left = root*2+1

        if left <= self.size and self._compare(left, winner):
            winner = left
        if right <= self.size and self._compare(right, winner):
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