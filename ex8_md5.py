import hashlib 
  
# encoding GeeksforGeeks using md5 hash 
# function  
str1 = 'cryptography'
result = hashlib.md5(str1.encode()) 
  
# printing the equivalent byte value. 
print "The byte equivalent of hash is : " 
print result.hexdigest() 
