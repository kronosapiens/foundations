'''Python dict implementation (hash table)

Objectives:
    O(1) lookup (average case)
    O(1) write (average case)

    O(n) lookup (worst case)
    O(n) write (worst case)

    No implicit memory allocation

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

class dict(object):
    def __init__(self, size=50):
        self.size = size
        self.data = [None for _ in xrange(size)] # Initialize to "fixed" width

    def set(self, key, value):
        subarray = self._get_subarray(key)
        for i in xrange(len(subarray)):
            k,v = subarray[i]
            if k == key:
                subarray[i] = (key, value)
                return
        subarray.append((key, value))

    def get(self, key):
        subarray = self._get_subarray(key)
        for k, v in subarray:
            if k == key:
                return v
        raise KeyError('Key \'{}\' not found!'.format(key))

    def _get_index(self, key):
        return hash(key) % self.size

    def _get_subarray(self, key):
        idx = self._get_index(key)
        if self.data[idx] is None:
            self.data[idx] = []
        return self.data[idx]


if __name__ == "__main__":
    import doctest
    doctest.testmod()