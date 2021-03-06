'''
key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.
lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.
M은 항상 N 이하입니다.
key와 lock의 원소는 0 또는 1로 이루어져 있습니다.
0은 홈 부분, 1은 돌기 부분을 나타냅니다.

돌리고 옮겨서 맞춰봐야 함.
'''


def solution(key, lock):
    def rotate(bumps):
        return {(j, len_key-1-i) for i, j in bumps}

    def check(bumps):
        for x in range(1-len_key, len_lock):
            for y in range(1-len_key, len_lock):
                temp = {(i+x, j+y) for i, j in bumps if 0 <=
                        i+x < len_lock and 0 <= j+y < len_lock}
                if temp == holes:
                    return True
        return False

    len_lock = len(lock)
    len_key = len(key)
    holes = {(i, j) for i in range(len_lock)
             for j in range(len_lock) if not lock[i][j]}
    bumps = {(i, j) for i in range(len_key)
             for j in range(len_key) if key[i][j]}
    for _ in range(4):
        if check(bumps):
            return True
        bumps = rotate(bumps)
    return False


'''
def solution(key, lock):
    lk, ll = len(key), len(lock)
    holes = list()
    up = list()
    for i in range(ll):  # 채워줄 것들
        for j in range(ll):
            if lock[i][j] == 0:
                holes.append((i, j))

    for i in range(lk):  # 채울 것들
        for j in range(lk):
            if key[i][j] == 1:
                up.append((i, j))

    for _ in range(4):  # 4번 회전
        for g1 in range(-ll+1, ll):  # 평행이동
            for g2 in range(-ll+1, ll):
                check = [(i[0]+g1, i[1]+g2) for i in up]  # 움직여준 key
                for c in holes:
                    if c not in check:  # 못 채워주면
                        break
                else:
                    for c in check:
                        if c not in holes and 0 <= c[0] < ll and 0 <= c[1] < ll:
                            break
                    else:
                        return True
        # key를 회전시킴 # x, y >> y, n-1-x [2][0] > [0][0]
        up = [(i[1], lk - i[0] - 1) for i in up]
    return False
'''


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
      [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
