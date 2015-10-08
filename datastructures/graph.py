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
    {'cat': 1}
    >>> ug.vertices['cat']
    {'dog': 1}
    >>> ug.remove_vertex('dog')
    >>> ug.vertices['cat']
    {}

    >>> dg = graph(kind='directed')
    >>> dg.add_vertex('cat')
    >>> dg.add_vertex('dog')
    >>> dg.add_edge('cat', 'dog', 3)
    >>> dg.vertices['cat']['out']
    {'dog': 3}
    >>> dg.vertices['cat']['in']
    {}
    >>> dg.vertices['dog']['out']
    {}
    >>> dg.vertices['dog']['in']
    {'cat': 3}
    >>> dg.remove_edge('cat', 'dog')
    >>> dg.vertices['cat']['out']
    {}
    >>> dg.vertices['dog']['in']
    {}

    '''
    def __init__(self, kind=UNDIRECTED):
        self.kind = kind
        self.vertices = {}

    def __repr__(self):
        return 'n = {}'.format(len(self.vertices))

    def add_vertex(self, v):
        if self.kind == UNDIRECTED:
            self.vertices[v] = {}
        else:
            self.vertices[v] = {OUT: {}, IN: {}}

    def add_edge(self, v1, v2, weight=1):
        if self.kind == UNDIRECTED:
            self.vertices[v1][v2] = weight
            self.vertices[v2][v1] = weight
        else:
            self.vertices[v1][OUT][v2] = weight
            self.vertices[v2][IN][v1] = weight

    def remove_vertex(self, v):
        del self.vertices[v]
        for vertex in self.vertices:
            if self.kind == UNDIRECTED:
                del self.vertices[vertex][v]
            else:
                del self.vertices[vertex][IN][v]
                del self.vertices[vertex][OUT][v]

    def remove_edge(self, v1, v2):
        if self.kind == UNDIRECTED:
            del self.vertices[v1][v2]
            del self.vertices[v2][v1]
        else:
            del self.vertices[v1][OUT][v2]
            del self.vertices[v2][IN][v1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()