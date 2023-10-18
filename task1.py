def find_maxnumber(numbers):
    n = len(numbers)
    count = {}

    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    max_count = 0
    max_number = 0

    for number, count in count.items():
        if count > max_count:
            max_count = count
            max_number = number
    if max_count > n/2:
        return max_number
    else:
        return 0

numbers = [1,6,6,6,7,7,7,7,7]
result = find_maxnumber(numbers)
print(result)