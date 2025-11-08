s= input().strip()

freq={}

for ch in s:
    if ch in freq:
        freq[ch]+=1
    else :
        freq=1      