import os
os.environ['PYTHONHAS']

n= int(input())
t=tuple(map(int,input().split()))

print(hash(t))