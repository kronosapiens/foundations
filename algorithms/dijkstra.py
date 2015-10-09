from datastructures.graph import graph

def djisktra(graph, start):
    '''
    Dijkstra's algorith implementation.

    Objectives:

    >>> g = graph(kind='undirected')
    >>> [g.add_vertex(v) for v in ['A', 'B', 'C', 'D']]
    >>> g.add_edge('A', 'B', w=1)
    >>> g.add_edge('A', 'C', w=3)
    >>> g.add_edge('B', 'C', w=1)
    >>> g.add_edge('B', 'D', w=3)
    >>> g.add_edge('C', 'D', w=1)
    >>> paths = djikstra(g, 'A')
    >>> path['D']
    ['A', 'B', 'C', 'D']
    >>> paths = djikstra(g, 'C')
    >>> paths['A']
    ['C', 'B', 'A']
    '''
    V = set(graph.vertices.keys())
    S = {start}
    dist = {v: 0 for v in V}
    prev = {}




if __name__ == "__main__":
    import doctest
    doctest.testmod()