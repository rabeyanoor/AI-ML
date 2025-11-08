pixel = input().split()

x=int(pixel[0])
y=int(pixel[1])

ave=sum(pixel)/len(pixel)

if ave <85:
    print("Dark Image")
elif 85<=ave <=170:
    print("Normal Image")
else:
    print("")        