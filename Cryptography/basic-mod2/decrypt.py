from email import message
from tokenize import Number

def modInverse(a, m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

alphabets = ["0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = [0,1,2,3,4,5,6,7,8,9]

file = open("message.txt", "r")
lines = file.readlines()

for line in lines:
    message_numbers = line.strip()
    digits = message_numbers.split(" ")
    msg = ""
    for digit in digits:
        num = int(digit.strip())%41
        val = modInverse(num, 41)
        print("val: "+str(val))
        if val <= 26:
            msg += alphabets[val].lower()
        elif 27 <= val <= 36:
            msg += str(numbers[val-27])
        elif val == 37:
            msg += "_"
    print("The message is: " + msg)


