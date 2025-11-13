inp =input()
numbers = inp.split()

print(numbers)
print(type(numbers[0]))


brightness =float(numbers[0])
threshold=float(numbers[1])
print(brightness,th)
if brightness >= threshold:
    print("No")
else:
    print("OFF")