string = str(raw_input())
key = int(raw_input())
for i in range (0,len(string)):
	print chr(ord(string[i])+key),
