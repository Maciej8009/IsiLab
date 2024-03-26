import random

chars = "abcdefghijklmnoprstuwxyzABCDEFGHIJKLMNOPRSTUWXYZ0123456789"
array = []
for x in range(0, 1000):
    string = ''
    for y in range(0, 6):
        string += random.choice(chars)
    array.append(string)

toWrite = ''
lastItem = array[-1]
for x in array:
    toWrite += x
    if x == lastItem:
        break
    toWrite += '\n'

f = open('passwords.txt', 'w')
f.write(toWrite)
f.close()
