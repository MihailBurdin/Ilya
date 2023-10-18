def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary > 0:
        decimal += (binary % 10) * (2 ** power)
        binary //= 10
        power += 1
    return decimal

binary_number = 10101110011
decimal_number = binary_to_decimal(binary_number)
print(decimal_number)