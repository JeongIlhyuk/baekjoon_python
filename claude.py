import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
nums = list(map(int, input().split()))
stack = []  # (인덱스, 값) 저장할 스택
answer = [-1] * N

for i in range(N):
    # 스택이 비어있지 않고, 현재 수가 스택 top의 수보다 크면
    while stack and nums[stack[-1]] < nums[i]:
        # 오큰수를 찾은 인덱스의 답을 현재 수로 업데이트
        answer[stack.pop()] = nums[i]
    stack.append(i)

# 정답 출력
print(" ".join(map(str, answer)))
