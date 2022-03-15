from email import message
from tokenize import Number


alphabets = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers = [0,1,2,3,4,5,6,7,8,9]

file = open("message.txt", "r")
lines = file.readlines()

for line in lines:
    message_numbers = line.strip()
    digits = message_numbers.split(" ")
    msg = ""
    for digit in digits:
        val = int(digit.strip())%37
        if val <= 25:
            msg += alphabets[val]
        elif 26 <= val <= 35:
            msg += str(numbers[val-26])
        elif val == 36:
            msg += "_"
    print("The message is: " + msg)


