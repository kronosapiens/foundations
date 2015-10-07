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
'''


class node(object):
    def __init__(self, content):
        self.content = content
        self.next = None

    def __repr__(self):
        return 'Content: ({}), next = {}'.format(
            self.content, self.next is not None)

    def find(self, key):
        if self.content == key:
            return self
        elif self.next is not None:
            return self.next.find(key)


if __name__ == "__main__":
    import doctest
    doctest.testmod()