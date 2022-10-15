def bfs(adj):
    capacity = []
    lookup = [False]*len(adj)
    q = [0]
    lookup[0] = True
    while q:
        capacity.append(len(q))
        new_q = []
        for u in q:
            for v in adj[u]:
                if lookup[v]:
                    continue
                lookup[v] = True
                new_q.append(v)
        q = new_q
    return capacity

def water_container_system():
    N, Q = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        i, j = map(int, input().split())
        adj[i-1].append(j-1)
        adj[j-1].append(i-1)
    _ = [input() for _ in range(Q)]
    result = 0
    for c in bfs(adj):
        if result+c > Q:
            break
        result += c
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, water_container_system()))