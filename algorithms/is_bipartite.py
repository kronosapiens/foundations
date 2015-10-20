from Queue import Queue

from datastructures.graph import graph

def is_bipartite(graph):
    """Runs breadth-first search through a graph to determine if a graph
        is bipartite. Uses 2-color test.

    Objectives:
        O(m + n) running time (linear)

    Args:
        graph: the given graph, with nodes encoded as strings.
        root: the node from which to start the search.

    Returns:
        True if a graph is bipartite, False otherwise.

    >>> g = graph(kind='undirected')
    >>> g.add_vertex('A')
    >>> g.add_vertex('B')
    >>> g.add_vertex('C')
    >>> g.add_vertex('D')
    >>> g.add_edge('A', 'B')
    >>> g.add_edge('A', 'C')
    >>> g.add_edge('B', 'D')
    >>> g.add_edge('C', 'D')
    >>> is_bipartite(g)
    True

    >>> g.add_vertex('E')
    >>> g.add_edge('B', 'E')
    >>> g.add_edge('D', 'E')
    >>> is_bipartite(g)
    False
    """
    V = set(graph.vertices.keys())
    explored = {node: 0 for node in V}
    q = Queue()
    color = {}
    curr_color = 0

    s = V.pop()
    explored[s] = 1
    color[s] = curr_color
    q.put(s)
    while not q.empty():
        node = q.get()
        curr_color = 0 if color[node] else 1
        for neighbor in graph.vertices[node]:
            if not explored[neighbor]:
                explored[neighbor] = 1
                color[neighbor] = curr_color
                q.put(neighbor)
            elif color[neighbor] == color[node]:
                return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()