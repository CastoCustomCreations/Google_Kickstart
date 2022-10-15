def sort_the_fabrics():
    N = int(input())
    fabrics = [input().split() for _ in range(N)]
    A = sorted((C, int(U)) for C, _, U in fabrics)
    B = sorted((int(D), int(U)) for _, D, U in fabrics)
    return sum(a == b for (_, a), (_, b) in zip(A, B))

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, sort_the_fabrics()))