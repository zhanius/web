n = int(input())
arr = input().split(" ")
cnt = 0
for x in range(1, n):
    if int(arr[x]) > int(arr[x-1]):
        cnt+=1
print(cnt)

