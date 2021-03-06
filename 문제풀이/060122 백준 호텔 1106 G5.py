'''
호텔 성공

시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
2 초	128 MB	4863	1480	1103	31.309%
문제
세계적인 호텔인 형택 호텔의 사장인 김형택은 이번에 수입을 조금 늘리기 위해서 홍보를 하려고 한다.

형택이가 홍보를 할 수 있는 도시가 주어지고, 각 도시별로 홍보하는데 드는 비용과, 
그 때 몇 명의 호텔 고객이 늘어나는지에 대한 정보가 있다.

예를 들어, “어떤 도시에서 9원을 들여서 홍보하면 3명의 고객이 늘어난다.”와 같은 정보이다. 
이때, 이러한 정보에 나타난 돈에 정수배 만큼을 투자할 수 있다. 
즉, 9원을 들여서 3명의 고객, 18원을 들여서 6명의 고객, 27원을 들여서 9명의 고객을 늘어나게 할 수 있지만, 
3원을 들여서 홍보해서 1명의 고객, 12원을 들여서 4명의 고객을 늘어나게 할 수는 없다.

각 도시에는 무한 명의 잠재적인 고객이 있다. 
이때, 호텔의 고객을 적어도 C명 늘이기 위해 형택이가 투자해야 하는 돈의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 C와 형택이가 홍보할 수 있는 도시의 개수 N이 주어진다. 
C는 1,000보다 작거나 같은 자연수이고, N은 20보다 작거나 같은 자연수이다. 
둘째 줄부터 N개의 줄에는 각 도시에서 홍보할 때 대는 비용과 그 비용으로 얻을 수 있는 고객의 수가 주어진다.
이 값은 100보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.

예제 입력 1 
12 2
3 5
1 1
예제 출력 1 
8

예제 입력 2 
10 3
3 1
2 2
1 3
예제 출력 2 
4

예제 입력 3 
10 10
1 1
2 2
3 3
4 4
5 5
6 6
7 7
8 8
9 9
10 10
예제 출력 3 
10

예제 입력 4 
100 6
4 9
9 11
3 4
8 7
1 2
9 8
예제 출력 4 
45

'''

# https://www.acmicpc.net/problem/1106

# 풀이 1 visited를 2차원 배열로 하여, 몇 개 고려했을 때, 몇 명의 사람을 얼마에 구할 수 있는 지 저장하였다.
city, n = map(int, input().split())
pc = [tuple(map(int, input().split())) for _ in range(n)]

v = [[float('inf')]*2001 for _ in range(len(pc)+1)]
for i in range(len(v)):
    v[i][0] = 0
for idx, (p, c) in enumerate(pc, 1):
    for i in range(0, 2001):
        if i >= c:
            v[idx][i] = min(v[idx][i-c]+p, v[idx-1][i-c]+p, v[idx-1][i])
        else:
            v[idx][i] = v[idx-1][i]
print(min(v[-1][city:]))

# 풀이 2 visited를 1차원 배열로 하여 매 칸마다 모든 pc를 순회하도록 하였다.
city, n = map(int, input().split())
pc = [tuple(map(int, input().split())) for _ in range(n)]

visited = [float('inf')]*2001
visited[0] = 0
for i in range(1, 2001):
    for p, c in pc:
        if i >= c:
            visited[i] = min(visited[i], visited[i-c]+p)
print(min(visited[city:]))
