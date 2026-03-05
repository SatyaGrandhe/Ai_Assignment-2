def depth_limited(graph, node, target, limit):

    if node == target:
        return True

    if limit == 0:
        return False

    for neighbor in graph.get(node, []):
        if depth_limited(graph, neighbor, target, limit - 1):
            return True

    return False


def iterative_deepening(graph, start, goal, max_depth):

    for level in range(max_depth + 1):

        if depth_limited(graph, start, goal, level):
            return True

    return False


graph_data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

result = iterative_deepening(graph_data, 'A', 'F', 5)

print("IDDFS Result:", result)def depth_limited(graph, node, target, limit):

    if node == target:
        return True

    if limit == 0:
        return False

    for neighbor in graph.get(node, []):
        if depth_limited(graph, neighbor, target, limit - 1):
            return True

    return False


def iterative_deepening(graph, start, goal, max_depth):

    for level in range(max_depth + 1):

        if depth_limited(graph, start, goal, level):
            return True

    return False


graph_data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

result = iterative_deepening(graph_data, 'A', 'F', 5)

print("IDDFS Result:", result)
