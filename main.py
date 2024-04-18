from collections import defaultdict



def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph



def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        new_frontier = set()
        for node in frontier:
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in result:
                    new_frontier.add(neighbor)
                    result.add(neighbor)
        frontier = new_frontier
    return result




def connected(graph):
    nodes = set(graph.keys())
    if len(nodes) == 0:
        return False

    visited = set()
    stack = [next(iter(nodes))]

    while stack:
        node = stack.pop()
        visited.add(node)
        neighbors = graph[node]
        for neighbor in neighbors:
            if neighbor not in visited:
                stack.append(neighbor)

    return len(visited) == len(nodes)




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    visited = set()
    components = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            components += 1
            dfs(node)
    
    return components

