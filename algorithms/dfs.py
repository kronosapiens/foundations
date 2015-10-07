def DFS(graph, root):
    """Runs depth-first search through a graph, starting at a given root. Neighboring
    nodes are processed in alphabetical order.

    Args:
        graph: the given graph, with nodes encoded as strings.
        root: the node from which to start the search.

    Returns:
        A list of nodes in the order in which they were first visited.
    """
    env = {
        'graph': graph,
        'explored': {node: 0 for node in graph.nodes()},
        'start': {},
        'finish': {},
        'time': 0
    }
    search(root, env)
    return sorted(env['start'], key=env['start'].get)

def search(node, env):
    previsit(node, env)
    env['explored'][node] = 1
    neighbors = env['graph'][node].keys()
    neighbors.sort()
    for neighbor in neighbors:
        if not env['explored'][neighbor]:
            search(neighbor, env)
    postvisit(node, env)

def previsit(node, env):
    env['start'][node] = env['time']
    env['time'] += 1

def postvisit(node, env):
    env['finish'][node] = env['time']
    env['time'] += 1