def del_duplic_change_elem(numbers):
    result = []
    dupli = []
    swap = []

    for number in numbers:
        if number in result:
            dupli.append(number)
        else:
            result.append(number)

    if len(result) % 2 == 0:
        for n in range(1, len(result),2):
            swap.extend([result[n], result[n - 1]])
    else:
        for n in range(1, len(result) - 1,2):
            swap.extend([result[n], result[n - 1]])

    return swap

numbers = [1,3,3,4,5,6,7,7,7,7,7]
swapped_nums = del_duplic_change_elem(numbers)
print(swapped_nums)
