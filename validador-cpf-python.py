import os
import random

cpf_inserido= ''
for i in range(9):
    cpf_inserido += str(random.randint(0,9))
os.system('cls')

novedigitos = cpf_inserido[:9]
dezdigitos = cpf_inserido [:10]
contagemregressiva = 10

resultado = 0
digitoreal = 0

for digito1 in novedigitos:
    digitoint = int(digito1)
    resultado += (digitoint * contagemregressiva)
    contagemregressiva -=1

digito1 = (resultado * 10) % 11
digito1 = digito1 if digito1 <-9 else 0

print(f'primeiro digito é {digito1}')

contagemregressiva2 = 11
resultado2 = 0

for digito2 in dezdigitos:
    digitoint = int(digito2)
    resultado2 += (digitoint * contagemregressiva2)
    contagemregressiva2 -=1

digito2= (resultado2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0
print (f'o segundo digito é {digito2}')

cpf_gerado = f'O cpf gerado é {novedigitos[:3]}.{novedigitos[3:6]}.{novedigitos[6:9]} - {digito1}{digito2}'
print (cpf_gerado)

if cpf_gerado == cpf_inserido:
    print(' o cpf é valido')

