def decimalTobinaryAny(num):
    binary = ["0", "0", "0", "0", "0", "0", "0", "0"]
    if num > 128 :
        binary[0] = "1"
        num = num-128
    if num > 64:
        binary[1] = "1"
        num = num-64
    if num > 32:
        binary[2] = "1"
        num = num -32
    if num > 16:
        binary[3] = "1"
        num = num-16
    if num > 8:
        binary[4]= "1"
        num = num-8
    if num > 4:
        binary[5] = "1"
        num = num-4
    if num > 2:
        binary[6] = "1"
        num = num-2
    if num > 1:
        binary[7]= "1"
        num = num-1
    else: print ("This cannot be converted into Binary")
    print(binary)


decimalTobinaryAny(100)