import sys
input = sys.stdin.readline

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()
arr2.reverse()

sum = 0
for i in range(n):
    sum += arr1[i] * arr2[i]
    
print(sum)