numbers = [4, 6, 1, 21, 5]
max_num = numbers[0]

for number in numbers:
    if number > max_num:
        max_num = number
print(f"Largest number: {max_num}")