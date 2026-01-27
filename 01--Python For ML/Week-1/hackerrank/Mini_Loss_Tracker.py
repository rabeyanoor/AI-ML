n=int(input())
terget=float(input())
total=0.0

for i in range(n):
    loss=float(input())
    total+=loss

ave =total/n


if ave<=terget:
    print("PASS")
else:
    print("RETRY")    