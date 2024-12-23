edges = [
    (1, 1, 2), (3, 1, 3), (5, 2, 3), (1, 3, 4), (4, 4, 5),
    (2, 4, 6), (1, 5, 6), (3, 6, 7), (1, 2, 8), (1, 7, 8),
    (5, 8, 11), (1, 11, 12), (2, 7, 9), (1, 10, 12), (2, 9, 10)
] # (вес, вершина_1, вершина_2)

num_vertices = 12

edges.sort()

parent = {i: i for i in range(1, num_vertices + 1)}
rank = {i: 0 for i in range(1, num_vertices + 1)}

def find(vertex):
    """Функция для нахождения родителя вершины."""
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

def union(v1, v2):
    """Функция для объединения двух компонент."""
    root1 = find(v1)
    root2 = find(v2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

mst = []
total_weight = 0

for weight, v1, v2 in edges:
    if find(v1) != find(v2):
        union(v1, v2)
        mst.append((v1, v2, weight))
        total_weight += weight

print("Минимальное остовное дерево включает рёбра:")
for v1, v2, weight in mst:
    print(f"(V{v1}, V{v2}), вес: {weight}")
print(f"WTmin: {total_weight}")
