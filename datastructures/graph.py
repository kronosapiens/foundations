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
    >>> ug.add_vertex('ape')
    >>> ug.add_edge('cat', 'dog')
    >>> ug.add_edge('cat', 'ape')
    >>> ug.vertices['cat']
    {'dog': 1, 'ape': 1}
    >>> ug.vertices['dog']
    {'cat': 1}
    >>> ug.remove_vertex('dog')
    >>> ug.vertices['cat']
    {'ape': 1}
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

    def add_edge(self, v1, v2, w=1):
        if self.kind == UNDIRECTED:
            self.vertices[v1][v2] = w
            self.vertices[v2][v1] = w
        else:
            self.vertices[v1][OUT][v2] = w
            self.vertices[v2][IN][v1] = w

    def remove_vertex(self, v):
        self.vertices.pop(v, None)
        for vertex in self.vertices:
            if self.kind == UNDIRECTED:
                self.vertices[vertex].pop(v, None)
            else:
                self.vertices[vertex][IN].pop(v, None)
                self.vertices[vertex][OUT].pop(v, None)

    def remove_edge(self, v1, v2):
        if self.kind == UNDIRECTED:
            self.vertices[v1].pop(v2, None)
            self.vertices[v2].pop(v1, None)
        else:
            self.vertices[v1][OUT].pop(v2, None)
            self.vertices[v2][IN].pop(v1, None)

    def find_sinks(self):
        pass

    def find_sources(self):
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()