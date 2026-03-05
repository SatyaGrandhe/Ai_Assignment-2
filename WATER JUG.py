from collections import deque

def solve_water_jug(cap1, cap2, goal):

    visited_states = set()
    q = deque()
    q.append((0, 0))

    while q:

        a, b = q.popleft()

        if (a, b) in visited_states:
            continue

        print("State:", a, b)
        visited_states.add((a, b))

        if a == goal or b == goal:
            print("Goal Achieved!")
            return

        # Fill jug1
        q.append((cap1, b))

        # Fill jug2
        q.append((a, cap2))

        # Empty jug1
        q.append((0, b))

        # Empty jug2
        q.append((a, 0))

        # Pour jug1 → jug2
        move = min(a, cap2 - b)
        q.append((a - move, b + move))

        # Pour jug2 → jug1
        move = min(b, cap1 - a)
        q.append((a + move, b - move))


solve_water_jug(4, 3, 2)
