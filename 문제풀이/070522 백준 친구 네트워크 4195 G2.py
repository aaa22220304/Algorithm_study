'''
친구 네트워크 성공다국어
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
3 초	256 MB	32300	8452	5138	25.472%
문제
민혁이는 소셜 네트워크 사이트에서 친구를 만드는 것을 좋아하는 친구이다. 
우표를 모으는 취미가 있듯이, 민혁이는 소셜 네트워크 사이트에서 친구를 모으는 것이 취미이다.

어떤 사이트의 친구 관계가 생긴 순서대로 주어졌을 때, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

친구 네트워크란 친구 관계만으로 이동할 수 있는 사이를 말한다.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 
각 테스트 케이스의 첫째 줄에는 친구 관계의 수 F가 주어지며, 이 값은 100,000을 넘지 않는다. 
다음 F개의 줄에는 친구 관계가 생긴 순서대로 주어진다. 
친구 관계는 두 사용자의 아이디로 이루어져 있으며, 알파벳 대문자 또는 소문자로만 이루어진 길이 20 이하의 문자열이다.

출력
친구 관계가 생길 때마다, 두 사람의 친구 네트워크에 몇 명이 있는지 구하는 프로그램을 작성하시오.

예제 입력 1 
2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty

예제 출력 1 
2
3
4
2
2
4
'''

# https://www.acmicpc.net/problem/4195

import sys
input = sys.stdin.readline

T = int(input())


def getP(x):
    a = x
    while x != p[x]:
        x = p[x]
    p[a] = x
    return x


def uniP(a, b):
    A, B = getP(a), getP(b)
    if A < B:
        p[A] = B
        f[B] += f[A]
    else:
        p[B] = A
        f[A] += f[B]
    return A


for _ in range(T):
    checkList = dict()
    cur = 0
    edges = []
    for __ in range(int(input())):
        a, b = input().split()
        if a not in checkList:
            checkList[a] = cur
            cur += 1
        if b not in checkList:
            checkList[b] = cur
            cur += 1
        a, b = checkList[a], checkList[b]
        if a < b:
            edges.append((a, b))
        else:
            edges.append((b, a))

    p = list(range(cur))
    f = [1]*cur

    for a, b in edges:
        A, B = getP(a), getP(b)
        if A != B:
            uniP(a, b)
        print(f[max(A, B)])
