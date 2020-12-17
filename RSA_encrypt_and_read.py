import random

e_list, d_list, letters_in_text, encrypted_text, ascii_val_text=[], [], [], [], []
ascii_val_text_mixed=[]

p=23
q=17
n=p*q
print('n: ', n)
phi=(p-1)*(q-1)
print('phi: ', phi)

for i in range(1,phi):
	if phi%i == 0:
		i+=1
	for divider in range(2,phi):
		if i%divider == 0 and i != divider:
			break
	else:
		e_list.append(i)
e = e_list[random.randint(0, len(e_list)-1)]
#e=5

while True:
	for i in range(2,phi):
		if i*e%phi == 1:
			d_list.append(i)
	if len(d_list)!=0:
		break
	else:
		e = e_list[random.randint(0, len(e_list)-1)]
d = d_list[random.randint(0, len(d_list)-1)]
#d=17
print('e: ', e)
print('d: ', d)

while True:
	cmd = input('Enter command (encrypt, read, quit, manual_ed): ')

	if cmd=='manual_ed':
		e = int(input('e: '))
		d = int(input('d: '))

	if cmd=='encrypt':
		#READ DATA
		with open('text.txt', 'r') as data:
			data_new = data.read()
			for i in range(len(data_new)):
				letters_in_text.append(data_new[i])
		
		#GET ASCII VALUES FROM TEXT
		for i in range(len(letters_in_text)):
			ascii_val_text.append(ord(letters_in_text[i]))

		print('Numerical values of the text: ',ascii_val_text)
		#MIXING VALUES
		for i in range(1, len(ascii_val_text)):
			ascii_val_text[i]=(ascii_val_text[i]+ascii_val_text[i-1])%n
		
		#print(ascii_val_text)
		#ENCRYPT
		for i in range(len(ascii_val_text)):
			encrypted_text.append(ascii_val_text[i]**e%n)

		#SAVE DATA
		file = open('encrypted_text.txt','w')
		for i in range(len(encrypted_text)):
			file.write(str(encrypted_text[i])+str(' '))
		file.close()
		ascii_val_text, encrypted_text, letters_in_text=[], [], []
		print('Done')

	if cmd=='read':
		#READ DATA
		with open('encrypted_text.txt', 'r') as data:
			encrypted_text=data.read().split()
		
		#DECRYPT
		for i in range(len(encrypted_text)):
			ascii_val_text_mixed.append(int(encrypted_text[i])**d%n)

		#print(ascii_val_text_mixed)
		#ARRANGE VALUES
		ascii_val_text.append(ascii_val_text_mixed[0])
		for i in range(1, len(ascii_val_text_mixed)):
			ascii_val_text.append((ascii_val_text_mixed[i]-ascii_val_text_mixed[i-1])%n)

		#print(ascii_val_text)
		#CONVERT ASCII TO LETTERS
		for i in range(len(ascii_val_text)):
			letters_in_text.append(chr(ascii_val_text[i]))
		#print(letters_in_text)
		#SAVE DATA
		file = open('decrypted_text.txt','w')
		for i in range(len(letters_in_text)):
			file.write(str(letters_in_text[i]))
		file.close()
		ascii_val_text, encrypted_text, letters_in_text=[], [], []
		print('Done')

	if cmd=='exit':
		break