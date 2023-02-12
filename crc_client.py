# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 19:27:42 2023

@author: LENOVO
"""

import socket

def xor(a,b):
    
		result = []
		for i in range(1,len(b)):
			if a[i] == b[i]:
				result.append('0')
			else:
				result.append('1')


		return  ''.join(result)



def Division(message, key):
		pick = len(key)

		tmp = message[:pick]

		while pick < len(message):
			if tmp[0] == '1':
				tmp = xor(key,tmp)+message[pick]
			else:
				tmp = xor('0'*pick,tmp) + message[pick]

			pick+=1

		if tmp[0] == "1":
			tmp = xor(key,tmp)
		else:
			tmp = xor('0'*pick,tmp)

		checkword = tmp
		return checkword

c=socket.socket()

c.connect(('localhost',5000))
print('Connected to the server......')
data=c.recv(1024).decode()
print('Data Received:',data)

CRC=c.recv(1024).decode()
print('Data Received:',CRC)

print('Enter the key:');
key=input()

data+=CRC
op=Division(data,key)

zeros='0'*(len(key)-1)
if op==zeros:
    c.send(('Received data is Correct......').encode())
else:
    c.send(("Data is not received successfully......").encode())