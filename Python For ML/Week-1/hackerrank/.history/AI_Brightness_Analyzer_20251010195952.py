pixel = map(int,input().split())


ave=sum(pixel)/len(pixel)

if ave <85:
    print("Dark Image")
elif 85<=ave <=170:
    print("Normal Image")
else:
    print("Bright Image")        