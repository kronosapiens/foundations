from datastructures.graph import graph

def dfs(graph, root):
    """Runs depth-first search through a graph, starting at a given
    root. Neighboring nodes are processed in alphabetical order.

    Objectives:
        O(m + n) running time

    Args:
        graph: the given graph, with nodes encoded as strings.
        root: the node from which to start the search.

    Returns:
        A list of nodes in the order in which they were first visited.

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
    >>> dfs(g, 'A')
    ['A', 'B', 'D', 'C', 'E']
    """
    env = {
        'graph': graph,
        'explored': {node: 0 for node in graph.vertices.keys()},
        'start': {},
        'finish': {},
        'time': 0
    }
    search(root, env)
    return sorted(env['start'], key=env['start'].get) # Sort by arrival time

def previsit(node, env):
    env['start'][node] = env['time']
    env['time'] += 1

def postvisit(node, env):
    env['finish'][node] = env['time']
    env['time'] += 1

def search(node, env):
    previsit(node, env)
    env['explored'][node] = 1
    neighbors = env['graph'].vertices[node].keys()
    neighbors.sort()
    for neighbor in neighbors:
        if not env['explored'][neighbor]:
            search(neighbor, env)
    postvisit(node, env)


if __name__ == "__main__":
    import doctest
    doctest.testmod()