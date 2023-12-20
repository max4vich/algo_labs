from collections import defaultdict, deque

def topological_sort(dependencies):
    graph = defaultdict(list)
    indegree = defaultdict(int)

    for u, v in dependencies:
        graph[v].append(u)
        indegree[u] += 1

    queue = deque([node for node in graph if indegree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbour in graph[node]:
            indegree[neighbour] -= 1
            if indegree[neighbour] == 0:
                queue.append(neighbour)

    return result


with open('E:/Users/Max4vich/Desktop/third_semester/2курс/algo/lab5/govern.in', 'r') as f:
    dependencies = [line.strip().split() for line in f]

result = topological_sort(dependencies)

with open('E:/Users/Max4vich/Desktop/third_semester/2курс/algo/lab5/govern.out', 'w') as f:
    for doc in result:
        f.write(doc + '\n')
