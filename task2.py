def string_to_32bit(s):
    s = s.strip()

    sign = 1
    if s[0] == "-":
        sign = -1
        s = s[1:]
    elif s[0] == "+":
        s = s[1:]

    number = 0
    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)
        else:
            break

    return sign * number

s1 = "69"
s2 = "          -69"
s3 = "    6969 words"

print(string_to_32bit(s1))
print(string_to_32bit(s2))
print(string_to_32bit(s3))
