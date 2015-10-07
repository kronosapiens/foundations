class node(object):
    '''Python linked list implementation

    Objectives:
        O(n) lookup
        Variable size
        No implicit memory allocation

    >>> ll = node('cat')
    >>> ll.content
    'cat'
    >>> ll.next
    >>> ll.next = node('dog')
    >>> ll.next.content
    'dog'
    >>> ll
    Content: (cat), next = True
    >>> ll.find('dog')
    Content: (dog), next = False
    >>> ll.find('monkey')
    >>> ll.next.next = node('monkey')
    >>> ll.find('monkey')
    Content: (monkey), next = False
    >>> ll.remove_next()
    >>> ll.next.content
    'monkey'
    '''
    def __init__(self, content):
        self.content = content
        self.next = None

    def __repr__(self):
        return 'Content: ({}), next = {}'.format(self.content, self.has_next)

    @property
    def has_next(self):
        return self.next is not None

    def find(self, key):
        if self.content == key:
            return self
        elif self.has_next:
            return self.next.find(key)

    def remove_next(self):
        if self.has_next and self.next.has_next:
            self.next = self.next.next


if __name__ == "__main__":
    import doctest
    doctest.testmod()