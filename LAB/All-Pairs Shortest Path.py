INF = 99999

def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    return dist


graph = [
    [0,   5,  INF, 10],
    [INF, 0,   3,  INF],
    [INF, INF, 0,   1],
    [INF, INF, INF, 0]
]

result = floyd_warshall(graph)

print("All-Pairs Shortest Path:")
for row in result:
    print(row)