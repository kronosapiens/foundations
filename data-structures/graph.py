UNDIRECTED = 'undirected'
DIRECTED = 'directed'
OUT = 'out'
IN = 'in'

class graph(object):
    '''
    Python graph implementation (adjacency list)

    V = set of vertices
    E = set of edges
    n = number of vertices
    m = number of edges

    Objectives:
        Linear time for algorithms O(m + n)
        O(m + n) space

    Facts:
        m = 2Sum_{v \in V} deg(v)
        "density" -> m = Om(n^2)

    >>> ug = graph(kind='undirected')
    >>> ug.add_vertex('cat')
    >>> ug.add_vertex('dog')
    >>> ug.add_edge('cat', 'dog')
    >>> ug.vertices['dog']
    set(['cat'])
    >>> ug.vertices['cat']
    set(['dog'])
    >>> ug.remove_vertex('dog')
    >>> ug.vertices['cat']
    set([])

    >>> dg = graph(kind='directed')
    >>> dg.add_vertex('cat')
    >>> dg.add_vertex('dog')
    >>> dg.add_edge('cat', 'dog')
    >>> dg.vertices['cat']['out']
    set(['dog'])
    >>> dg.vertices['cat']['in']
    set([])
    >>> dg.vertices['dog']['out']
    set([])
    >>> dg.vertices['dog']['in']
    set(['cat'])
    >>> dg.remove_edge('cat', 'dog')
    >>> dg.vertices['cat']['out']
    set([])
    >>> dg.vertices['dog']['in']
    set([])

    '''
    def __init__(self, kind=UNDIRECTED):
        self.kind = kind
        self.vertices = {}

    def __repr__(self):
        return 'n = {}'.format(len(self.vertices))

    def add_vertex(self, v):
        if self.kind == UNDIRECTED:
            self.vertices[v] = set()
        else:
            self.vertices[v] = {OUT: set(), IN: set()}

    def add_edge(self, v1, v2):
        if self.kind == UNDIRECTED:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            self.vertices[v1][OUT].add(v2)
            self.vertices[v2][IN].add(v1)

    def remove_vertex(self, v):
        del self.vertices[v]
        for vertex in self.vertices:
            if self.kind == UNDIRECTED:
                self.vertices[vertex].remove(v)
            else:
                self.vertices[vertex][IN].remove(v)
                self.vertices[vertex][OUT].remove(v)

    def remove_edge(self, v1, v2):
        if self.kind == UNDIRECTED:
            self.vertices[v1].remove(v2)
            self.vertices[v2].remove(v1)
        else:
            self.vertices[v1][OUT].remove(v2)
            self.vertices[v2][IN].remove(v1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()