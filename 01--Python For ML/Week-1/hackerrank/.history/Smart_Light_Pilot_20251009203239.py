inp =input()
numbers = inp.split()

print(numbers)
print()


brightness =float(numbers[0])
threshold=float(numbers[1])

if brightness >= threshold:
    print("No")
else:
    print("OFF")