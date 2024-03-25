file = open("test.txt")
input1 = file.read()
input2 = input1.split(sep=" ")

longest = max(input2, key=len)
print(longest)
