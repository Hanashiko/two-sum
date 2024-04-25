def two_sum(numbers: list[int], target: int):
    length: int = len(numbers)
    for i in range(length):
        for m in range(length):
            if i != m:
                if numbers[i] + numbers[m] == target:
                    return (i, m)
 
print(two_sum([2, 2, 3], 4))
