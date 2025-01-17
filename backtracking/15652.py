n, m = map(int, input().split())
    
path = []

def dfs(start, depth):
    if depth == m:
        print(*path)
        return
    for i in range(start, n+1):
        path.append(i)
        dfs(i, depth+1)
        path.pop()

dfs(1, 0)               