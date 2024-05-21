def binary_to_decimal(binary):
    size = len(binary)
    right = len(binary) - 1
    left = 0
    currentValue = 0

    binaryList = [128, 64, 32, 16, 8, 4, 2, 1]
    lengthInBinary = 8 - size
    del binaryList[0:lengthInBinary]

    while left < right:
        if size > 8:
            return "Error. This only supports 1 byte (8bits)"

        elif binary[left] != '1' and binary[left] != '0' or binary[right] != '1' and binary[right] != '0':
            print(binary[left], " and ", binary[right])
            return "Error, not a binary value of 0s and 1s."

        elif binary[left] == '1' and binary[right] == '1':
            leftAndRight = binaryList[left] + binaryList[right]
            currentValue += leftAndRight

        elif binary[left] == '1':
            currentValue += binaryList[left]

        elif binary[right] == '1':
            currentValue += binaryList[right]

        left += 1
        right -= 1

    return "Binary to Decimal: " + str(currentValue)


binary = input("Please enter unsigned bit:" + "\n")

print(binary_to_decimal(binary))
