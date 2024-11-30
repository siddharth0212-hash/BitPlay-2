# Program to find two number that are odd occuring

def printTwoOdd(arr, size):

    # xorof2 will hold xor of the 2 odd occuring number
    xorof2 = arr[0]

    # These will hold 2 odd occuring number
    x = 0 
    y = 0

    # This will hold the rightmost set bot from xorof2
    Set bit = 0

    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]

    setbit = xorof2 & ~(xorof2 - 1)

    # If number is having set bit at location we need the XOR it with x else y
    for i in range(size):
        if(arr[i] & setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]

    print("The two ODD elements are",x, "&", y)

# Create an empty array
arr = []

# Take array size and elements input
arr_size = int(input("Enter size of array : "))
for i in range(0,arr_size):
    z = int(input("Enter element : "))
    arr.append(z)

printTwoOdd(arr, arr_size)
