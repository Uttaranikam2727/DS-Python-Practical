"""GD9 - BFS (adjacency list) and DFS (adjacency matrix) on a map of locations"""
from collections import deque

nodes = ["A", "B", "C", "D", "E", "F"]
edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "F"), ("E", "F")]


def build_matrix(nodes, edges):
    n = len(nodes)
    idx = {name: i for i, name in enumerate(nodes)}
    m = [[0] * n for _ in range(n)]
    for u, v in edges:
        m[idx[u]][idx[v]] = 1
        m[idx[v]][idx[u]] = 1
    return m


def build_list(nodes, edges):
    adj = {name: [] for name in nodes}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    for name in adj:
        adj[name].sort()
    return adj


def dfs(matrix, nodes, start):
    visited = [False] * len(nodes)
    order = []

    def visit(i):
        visited[i] = True
        order.append(nodes[i])
        for j in range(len(nodes)):
            if matrix[i][j] == 1 and not visited[j]:
                visit(j)

    visit(nodes.index(start))
    return order


def bfs(adj, start):
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                queue.append(v)
    return order


def show(nodes, matrix, adj):
    print("Adjacency matrix:")
    print("   ", " ".join(nodes))
    for i, row in enumerate(matrix):
        print(nodes[i], " ", " ".join(map(str, row)))
    print("Adjacency list:")
    for k, v in adj.items():
        print(" ", k, "->", v)


def enter_graph():
    n = int(input("Number of locations: "))
    names = [input("  Location name %d: " % (i + 1)).strip() for i in range(n)]
    e = []
    print("Enter routes as 'A B' (blank line to stop):")
    while True:
        line = input("  ").split()
        if len(line) != 2:
            break
        e.append((line[0], line[1]))
    return names, e


def main():
    global nodes, edges
    while True:
        matrix = build_matrix(nodes, edges)
        adj = build_list(nodes, edges)
        print("\n--- Graph: BFS & DFS ---")
        print("1.Enter my own graph  2.Show matrix & list  3.DFS (matrix)  4.BFS (list)  0.Exit")
        ch = input("Choice: ").strip()
        if ch == "1":
            nodes, edges = enter_graph()
        elif ch == "2":
            show(nodes, matrix, adj)
        elif ch == "3":
            s = input("Start node: ").strip()
            print("DFS order:", " -> ".join(dfs(matrix, nodes, s)))
            print("Time: O(V^2) with matrix  Space: O(V)")
        elif ch == "4":
            s = input("Start node: ").strip()
            print("BFS order:", " -> ".join(bfs(adj, s)))
            print("Time: O(V+E) with list  Space: O(V)")
        elif ch == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
