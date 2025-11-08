inp =input()
numbers = inp.split()
c
print(numbers)


brightness =float(numbers[0])
threshold=float(numbers[1])

if brightness >= threshold:
    print("No")
else:
    print("OFF")