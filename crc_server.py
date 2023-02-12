# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 19:29:47 2023

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

s=socket.socket()

s.bind(('localhost',5000))
print("Socket created")
s.listen()
print('Waiting for client to connect....')
clt,add=s.accept()

print('Connected with ',add)

data=input('Enter the data:')
res= ''.join(format(ord(i), '08b') for i in data)

clt.send(res.encode())

print('Data converted to the binary',res)

key=input('Enter the key:')
data=data+'0'*(len(key)-1)

CRC=Division(data,key)

clt.send(CRC.encode())

print(clt.recv(1024).decode())