import os
os.environ['PYTHON']

n= int(input())
t=tuple(map(int,input().split()))

print(hash(t))