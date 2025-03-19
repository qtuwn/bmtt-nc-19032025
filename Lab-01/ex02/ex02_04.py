# Find numbers divisible by 7 but not by 5 in range 2000-3200
numbers = []
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        numbers.append(str(num))

# Print numbers separated by commas
print(','.join(numbers))