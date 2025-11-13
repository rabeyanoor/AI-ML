import os
os.environ['PYTHONHASHSEE']

n= int(input())
t=tuple(map(int,input().split()))

print(hash(t))