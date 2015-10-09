from datastructures.graph import graph
from datastructures.binheap import binheap

def djisktra(graph, s):
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
    S = set()

    dist = [(v, float('inf')) for v in V]
    dist.append((s,0))
    heap = binheap(dist, fkey=lambda x: x[0], fval=lambda x: x[1], kind='min')
    prev = {}

    while heap.size:
        u, dist = heap.extract()
        S = S.add(u)
        edges = graph.vertices[u]
        for e in edges:
            heap.update((e, dist+edges[e]))




if __name__ == "__main__":
    import doctest
    doctest.testmod()