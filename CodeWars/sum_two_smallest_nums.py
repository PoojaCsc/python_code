def sum_two_smallest_numbers(numbers):
    low1 = numbers[0]
    for i in range(len(numbers)):
        if numbers[i]<low1:
            low1 = numbers[i]
