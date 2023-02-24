def convertToBinary(num, length):
    # Vector to store the number
    bits = [0]*(length)
    if (num == 0):
        return bits
    i = length - 1
    while (num != 0):
        bits[i] = (num % 2)
        i -= 1
# Integer division
# gives quotient
        num = num // 2
    return bits
# Function to generate all
# N bit binary numbers


def getAllBinary(n):
    binary_nos = []
# Loop to generate the binary numbers
    for i in range(pow(2, n)):
        bits = convertToBinary(i, n)
        binary_nos.append(bits)
    return binary_nos


# Driver code
if __name__ == "__main__":
    N = 3
    binary_nos = getAllBinary(N)
    for i in range(len(binary_nos)):
        for j in range(len(binary_nos[i])):
            print(binary_nos[i][j], end="")
        print()
