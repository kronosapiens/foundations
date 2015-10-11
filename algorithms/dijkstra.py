from datastructures.graph import graph
from datastructures.binheap import binheap

def dijkstra(graph, s):
    '''
    Dijkstra's algorith implementation.

    Objectives:

    >>> g = graph(kind='undirected')
    >>> g.add_vertex('A')
    >>> g.add_vertex('B')
    >>> g.add_vertex('C')
    >>> g.add_vertex('D')
    >>> g.add_edge('A', 'B', w=1)
    >>> g.add_edge('A', 'C', w=3)
    >>> g.add_edge('B', 'C', w=1)
    >>> g.add_edge('B', 'D', w=3)
    >>> g.add_edge('C', 'D', w=1)
    >>> paths = dijkstra(g, 'A')
    >>> paths['dist']['D']
    3
    >>> paths['prev']['D']
    'C'
    >>> paths['dist']['C']
    2
    >>> paths['prev']['C']
    'B'
    >>> paths = dijkstra(g, 'C')
    >>> paths['dist']['A']
    2
    >>> paths['prev']['A']
    'B'
    '''
    V = set(graph.vertices.keys())
    S = set()
    dist = {}
    prev = {}

    initd = [(v, float('inf'), None) for v in V-{s}]
    initd.append((s, 0, None))
    heap = binheap(initd,fkey=lambda x: x[0], fval=lambda x: x[1], kind='min')

    while heap.size:
        u, udist, uprev = heap.extract()
        S.add(u)
        dist[u] = udist
        prev[u] = uprev
        edges = graph.vertices[u]
        for v in edges:
            vnode = heap.find(v)
            if vnode:
                v, vdist, vprev = vnode
                new_dist = udist + edges[v]
                if new_dist < vdist:
                    heap.update((v, new_dist, u))

    return {'dist': dist, 'prev': prev}


if __name__ == "__main__":
    import doctest
    doctest.testmod()