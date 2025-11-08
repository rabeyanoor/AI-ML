def find_min_max(arr):
    minimum =min(arr)
    maximum= max(arr)
    print(minimum,maximum)

n=int(input())
a=list(map(int,input().split()))

find_min_max(a)