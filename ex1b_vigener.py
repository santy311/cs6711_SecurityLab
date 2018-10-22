a = raw_input("Enter Plain Text")

key = raw_input("Enter Key")

ec = ''

for i in range(len(a)):
	print(i,a[i],key[i%len(key)])
	ec += chr((ord(a[i])-97*2+ord(key[i%len(key)]))%26+97)

print ec
