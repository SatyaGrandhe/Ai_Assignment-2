def depth_limited_search(graph, current, target, limit):

    if current == target:
        return True

    if limit == 0:
        return False

    for neighbor in graph.get(current, []):
        found = depth_limited_search(graph, neighbor, target, limit - 1)
        if found:
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

result = depth_limited_search(graph_data, 'A', 'F', 2)

print("Result of Depth Limited Search:", result)
