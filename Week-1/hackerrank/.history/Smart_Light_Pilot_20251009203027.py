inp =input()
numbers = inp.split()
inp =input()
numbers = inpu.split()

brightness =float(numbers[0])
threshold=float(numbers[1])

if brightness >= threshold:
    print("No")
else:
    print("OFF")