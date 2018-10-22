
a = raw_input("ENTER PLAIN TEXT")

c = int(raw_input("ENTER KEY COUNT"))

ec = ''

for i in a:
	ec+=(chr((ord(i)-97+c)%26+97))

print(ec)
