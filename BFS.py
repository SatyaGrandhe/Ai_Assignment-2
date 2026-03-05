from collections import deque

def breadth_first_search(graph, start_node, target):

    visited_nodes = set()
    q = deque([start_node])

    while q:

        current = q.popleft()

        if current not in visited_nodes:
            print("Node Visited:", current)
            visited_nodes.add(current)

            if current == target:
                print("Target Node Reached!")
                return

            for next_node in graph.get(current, []):
                q.append(next_node)


network = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

breadth_first_search(network, 'A', 'F')
