def incrementBinary(binaryString, iterations):
    for i in range(iterations):
        print(f"Original Binary: {binaryString}")
        binaryString = '0' + binaryString
        binaryCharList = list(binaryString)
        len1 = len(binaryString)
        len2 = len1 - 1
        while binaryCharList[len2] == '1':
            binaryCharList[len2] = '0'
            len2 -= 1
            binaryCharList[len2] = '1'
            finalBinaryString = ''.join(binaryCharList)
            if len2 > 0:
                finalBinaryString = finalBinaryString[1:]
                print(f"After Incrementing: {finalBinaryString}\n")
                binaryString = finalBinaryString


num = int(input("Enter Integer: "))
incrementBy = int(input("Enter number of times you want to increment: "))
incrementBinary(bin(num)[2:], incrementBy)
