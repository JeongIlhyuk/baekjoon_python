import sys
import heapq, copy
from math import comb

input = sys.stdin.readline
print = sys.stdout.write
from collections import deque
from itertools import permutations, product


# # 1 input
N = int(input())
# input_str = input().rstrip()
# bomb_str = input().rstrip()

##### Commonly used #####

stack = []
for i in range(N):
    int(input())

print(" ".join(map(str, answer)) + "\n")
