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