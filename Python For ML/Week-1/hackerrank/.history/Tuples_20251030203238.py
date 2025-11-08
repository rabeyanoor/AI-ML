import os
os.environ['PYTHONHASHS']

n= int(input())
t=tuple(map(int,input().split()))

print(hash(t))