n,m= map(int,input().split())
arr=list(map(int,input().split()))
a=set(map(int,input().split()))
b=set(map(int,input().split()))

happiness=0

for num in arr:
    if num in a:
        happiness+=1
    elif         