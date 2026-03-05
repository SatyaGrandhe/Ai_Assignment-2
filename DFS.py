def depth_first_search(graph, start_node, target):

    visited_nodes = set()
    stack = [start_node]

    while stack:

        current = stack.pop()

        if current not in visited_nodes:

            print("Node Visited:", current)
            visited_nodes.add(current)

            if current == target:
                print("Target Node Found!")
                return

            for next_node in reversed(graph.get(current, [])):
                stack.append(next_node)


graph_data = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

depth_first_search(graph_data, 'A', 'F')
