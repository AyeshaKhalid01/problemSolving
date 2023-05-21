def dectobin(input):
    if (input//2)==0:
        return str(input%2)
    return str(dectobin(input//2))+str(input%2)

def sumNN(input):
    if (input==0):
        return 0
    return input+sumNN(input-1)

def reverseString(input):
    if input=="":
        return ""
    return reverseString(input[1:])+input[0]

def palindrome(input):
    if len(input)==1 or len(input)==0:
        return True
    if input[0]==input[-1]:
        return palindrome(input[1:-1])
    return False

def binSearchHelper(input, target, left, right):
    pos = (left+right)//2
    if left>right:
        return -1
    elif input[pos]==target:
        return pos
    elif input[pos]>target:
        return binSearchHelper(input, target, left, pos-1)
    else:
        return binSearchHelper(input, target, pos+1, right)


print(dectobin(233))
print(sumNN(10))
print(reverseString("palindrome"))
print(palindrome("kayak"))
print(palindrome("racecar"))
print(palindrome("Ayesha"))

