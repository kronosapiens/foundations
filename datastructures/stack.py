import linkedlist

class stack(object):
    '''
    Python stack implementation.

    Objectives:
        O(1) push
        O(1) pop
        O(n) size (no implicit memory allocation)

    >>> mystack = stack()
    >>> mystack.push('cat')
    >>> mystack.push('dog')
    >>> mystack.pop()
    'dog'
    >>> mystack.push('ape')
    >>> mystack.peek()
    'ape'
    >>> mystack.pop()
    'ape'
    >>> mystack.pop()
    'cat'
    >>> mystack.pop()
    '''
    def __init__(self):
        self.head = None

    def push(self, element):
        self.head = linkedlist.node(element, self.head)

    def pop(self):
        if self.head is not None:
            element = self.head.content
            self.head = self.head.next
            return element

    def peek(self):
        if self.head is not None:
            return self.head.content

    @property
    def is_empty(self):
        return self.head is None



if __name__ == "__main__":
    import doctest
    doctest.testmod()