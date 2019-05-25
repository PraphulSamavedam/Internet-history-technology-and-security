# Code to decode a message sent in 
def code_gen():
	dct = dict()
	dct['PP']=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	for num in list(range(1,27,1)):
		dct[num] = []
		for indx in list(range(0,26,1)):
			if(num+indx<len(dct['PP'])):
				dct[num].append(dct['PP'][indx+num])
			else:
				jil =0
				while jil<num:
					dct[num].append(dct['PP'][jil])
					jil +=1;
	print("Caeser codes generated sucessfully")
	return dct;
def decipher(code,text,code_num):
	decoded_message=''
	for v in text:
		for iter in list(range(0,26,1)):
			#print(v.upper(),code_num,code[code_num][iter])
			if code[code_num][iter] == v.upper():
				#print('decoded_symbol :')
				decoded_symbol=code['PP'][iter];
				#print('decoded_symbol:',decoded_symbol)
				break;
		decoded_message =decoded_message + decoded_symbol;
	return  decoded_message;

Encoder = code_gen();
cipher_txt = input('Enter text to be ciphered: ');
print("Entered ciphered text: ",cipher_txt);
print("Code number","Deciphered text")
for num in list(range(1,27,1)):
	deciphered = decipher(Encoder,cipher_txt,num);
	print(num,"\t\t",deciphered);
