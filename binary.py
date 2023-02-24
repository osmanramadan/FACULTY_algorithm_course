def binary(n):
    count = 1
    while n > 1:
        count += 1
        n //= 2

    return count


print(binary(16))
