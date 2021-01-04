# Write your code here
n = int(input())
if 1 <= n<=10:
    arr = list(map(int, input().split()))
print(sum(arr))