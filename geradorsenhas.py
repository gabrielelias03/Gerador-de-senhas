import random
import string

def gerar_senha(comprimento, caracteres):
    senha = ''
    for i in range(comprimento):
        senha += random.choice(caracteres)
    return senha

# Pedir ao usuário para escolher o comprimento da senha e os caracteres a serem usados
comprimento = int(input("Digite o comprimento da senha: "))
usar_letras_maiusculas = input("Usar letras maiúsculas? (sim ou nao): ")
usar_letras_minusculas = input("Usar letras minúsculas? (sim ou nao): ")
usar_numeros = input("Usar números? (sim ou não): ")
usar_caracteres_especiais = input("Usar caracteres especiais? (sim ou não): ")

# Montar a lista de caracteres a serem usados baseado nas respostas do usuário
caracteres = ''
if usar_letras_maiusculas == 'sim':
    caracteres += string.ascii_uppercase
if usar_letras_minusculas == 'sim':
    caracteres += string.ascii_lowercase
if usar_numeros == 'sim':
    caracteres += string.digits
if usar_caracteres_especiais == 'sim':
    caracteres += string.punctuation

# Gerar a senha
senha = gerar_senha(comprimento, caracteres)

# Exibir a senha
print("Senha gerada:", senha)
