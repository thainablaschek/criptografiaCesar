import requests,json

r=requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=3764324cf4cc4bb53bf416d692a2f9dd5e7983af')

dados = r.json()
cifrado = dados['cifrado']
numero=int(dados['numero_casas'])
print(numero)
print(cifrado)

nova_mensagem=[]

alfabeto= (['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

for i in range(len(cifrado)):

	for j in range(len(alfabeto)):
		if (cifrado[i] == alfabeto[j]):
			posicao=j
			print(posicao)
			if (posicao<numero):
				posicao = 26+posicao
			print(posicao)
			nova_posicao = posicao - numero
			nova_mensagem.append(alfabeto[nova_posicao])
		elif(cifrado[i] == ''):
			nova_mensagem.append('')
		elif(cifrado[i] == '.'):
			nova_mensagem.append('.')

print(nova_mensagem)