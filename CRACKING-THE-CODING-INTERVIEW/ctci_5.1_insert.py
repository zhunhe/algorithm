#ctci_5.1_insert.py

"""
연습문제 5.1 삽입
두개의 32비트 N과 M이 주어지고, 비트 위치 i와 j가 주어졌을 때,
M을 N에 삽입하는 메서드를 구현하라.
예제
입력: N=10000000000, M=10011, i=2, j=6
출력: N=10001001100
"""

def insert(N, M, i, j):
    return str(N)[:-j-1] + str(M) + str(N)[-i:]

print(insert(10000000000, 10011, 2, 6))
