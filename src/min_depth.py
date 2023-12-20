from collections import defaultdict, deque


def min_depth(root, edges):
    graph = defaultdict(list)
    for start, end in edges:
        graph[start].append(end)
    queue = [(root, 1)]
    visited = set([root])
    while queue:
        node, depth = queue.pop(0)
        if node not in graph or not graph[node]:
            return depth
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.insert(0, (neighbor, depth + 1))


def reading(reading_path):
    with open(reading_path, 'r') as file:
        root = int(file.readline())
        edges = [tuple(map(int, line.split(','))) for line in file]
    return root, edges


def writting(writting_path, data):
    with open(writting_path, 'w') as file:
        file.write(str(data))


def main():
    # with open('C:/Users/Max4vich/Desktop/third_semester/2курс/algo/lab4/src/input.txt', 'r') as file:
    #     root = int(file.readline())
    #     edges = [tuple(map(int, line.split(','))) for line in file]

    # with open('C:/Users/Max4vich/Desktop/third_semester/2курс/algo/lab4/src/output.txt', 'w') as file:
    #     file.write(str(depth))
    reading_path = 'C:/Users/Max4vich/Desktop/third_semester/2курс/algo/lab4/src/input.txt'
    writting_path = 'C:/Users/Max4vich/Desktop/third_semester/2курс/algo/lab4/src/output.txt'
    root, edges = reading(reading_path)
    depth = min_depth(root, edges)
    writting(writting_path, depth)


if __name__ == "__main__":
    main()
