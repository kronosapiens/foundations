from datastructures.graph import graph
from datastructures.queue import queue

def bfs(graph, root):
    """Runs breadth-first search through a graph, starting at a given root.

    Objectives:
        O(m + n) running time (linear)

    Args:
        graph: the given graph, with nodes encoded as strings.
        root: the node from which to start the search.

    Returns:
        A dictionary containing the parent-child relationships of the bfs tree.

    >>> g = graph(kind='undirected')
    >>> g.add_vertex('A')
    >>> g.add_vertex('B')
    >>> g.add_vertex('C')
    >>> g.add_vertex('D')
    >>> g.add_vertex('E')
    >>> g.add_edge('A', 'B')
    >>> g.add_edge('A', 'C')
    >>> g.add_edge('B', 'D')
    >>> g.add_edge('C', 'D')
    >>> g.add_edge('B', 'E')
    >>> g.add_edge('D', 'E')
    >>> prev, dist = bfs(g, 'A')
    >>> prev['A']
    >>> prev['D']
    'C'
    >>> prev['E']
    'B'
    >>> dist['C']
    1
    >>> dist['E']
    2
    """
    V = set(graph.vertices.keys()) - {root}
    explored = {node: 0 for node in V}
    q = queue()
    prev = {root: None}
    dist = {root: 0}
    explored[root] = 1
    q.push(root)
    while q.size:
        node = q.pop()
        for neighbor in graph.vertices[node]:
            if not explored[neighbor]:
                explored[neighbor] = 1
                prev[neighbor] = node
                dist[neighbor] = dist[node] + 1
                q.push(neighbor)
    return prev, dist

if __name__ == "__main__":
    import doctest
    doctest.testmod()