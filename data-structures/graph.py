class graph(object):
    '''
    Python undirected graph implementation (adjacency list)

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

    >>> g = graph()
    >>> g.add_vertex('cat')
    >>> g.add_vertex('dog')
    >>> g.add_edge('cat', 'dog')
    >>> g.vertices['dog']
    set(['cat'])
    >>> g.vertices['cat']
    set(['dog'])
    >>> g.remove_vertex('dog')
    >>> g.vertices['cat']
    set([])
    '''
    def __init__(self):
        self.vertices = {}

    def __repr__(self):
        return 'n = {}'.format(len(self.vertices))

    def add_vertex(self, v):
        self.vertices[v] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
        self.vertices[v2].add(v1)

    def remove_vertex(self, v):
        del self.vertices[v]
        for vertex in self.vertices:
            self.vertices[vertex].remove(v)

    def remove_edge(self, v1, v2):
        self.vertices[v1].remove(v2)
        self.vertices[v2].remove(v1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()