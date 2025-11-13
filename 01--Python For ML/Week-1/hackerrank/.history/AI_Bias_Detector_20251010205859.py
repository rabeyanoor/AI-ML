x=input().split()

count_A= x.count('A')
count_B=x.count('B')

total=len(x)

if count_A > 0.7*total or count_B > 0.7*total:
    print("Biased Model")
else:
    print()    
