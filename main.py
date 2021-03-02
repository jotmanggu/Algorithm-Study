# 크기를 입력 받음
n, m = map(int, input().split())

# 그래프의 정보 입력 받음
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 연결된 노드 모두 방문(얼음 덩어리 파악)
def dfs(x, y):
    # 범위를 벗어나는 경우 탐지 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 노드를 방문하지 않은 경우를 0이라고 할 때, 0인 노드를 만나면 1로 바꿔서 방문 처리
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 해당 노드의 상하좌우 노드 모두 재귀적 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드에 대해서 덩어리 파악
result = 0
for i in range(n):
    for j in range(m):
        # (i,j)에서 dfs
        if dfs(i, j) == True:
            result += 1

print(result)