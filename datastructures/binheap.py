class binheap(object):
    '''
    Implementation of a binary min/max heap.

    Objectives:
        O(logn) insert
        O(logn) extract
        O(1) direct update

    Details and Abstractions:
        - Functions assume indices starting at 1. Helper functions _to_arr()
        and _to_tree() convert indices from 1 to 0 and vice versa.

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

    def _to_tree(self, idx):
        '''Convert from concrete array (0) index to abstract tree (1) index
        '''
        return idx+1

    def _to_arr(self, idx):
        '''Convert from abstract tree (1) index to concrete array (0) index
        '''
        return idx-1

    def _get_loc(self, key):
        '''Get abstract location of node in tree. Encapsulate location access.
        '''
        loc = self._location.get(key, None)
        if loc is not None:
            return self._to_tree(loc)

    def _compare(self, a, b):
        '''True result means a is preferred to b given comparison operator.
        '''
        f, heap = self.fval, self._heap
        a, b = self._to_arr(a), self._to_arr(b)
        if self._kind == 'min':
            return f(heap[a]) <= f(heap[b])
        else:
            return f(heap[a]) >= f(heap[b])

    def _swap(self, a, b):
        f, heap, location = self.fkey, self._heap, self._location
        a, b = self._to_arr(a), self._to_arr(b)
        a_val = heap[a]
        b_val = heap[b]
        heap[a] = b_val
        heap[b] = a_val
        location[f(a_val)] = b
        location[f(b_val)] = a

    def _replace(self, idx, new):
        '''Replace node at abstract location=idx with new node.
        '''
        self._heap[self._to_arr(idx)] = new

    def find(self, key):
        '''Return node, regardless of location in tree. Uses real location.
        '''
        loc = self._get_loc(key)
        if loc:
            return self._heap[self._to_arr(loc)]

    def update(self, new):
        node = self._get_loc(self.fkey(new))
        if node:
            self._replace(node, new)
            parent = node/2
            if self._compare(node, parent):
                self._bubble_up(node)
            else:
                self._bubble_down(node)

    def insert(self, node):
        self._heap.append(node)
        self._location[self.fkey(node)] = self.size
        self._bubble_up(self.size)

    def peek(self):
        return self._heap[self._to_arr(1)]

    def extract(self):
        root = self.peek()
        leaf = self._heap.pop()
        if self.size:
            self._heap[self._to_arr(1)] = leaf
            del self._location[self.fkey(root)]
            self._location[self.fkey(leaf)] = self._to_arr(1)
            self._bubble_down(1)
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