import os
os.environ['PYTHONHASHSEED']='0'

n= int(input())
t=tuple(map(int,input().split()))

print(hash(t))