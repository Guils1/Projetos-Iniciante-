from random import randint as r
import math as m

menor = int(input("Escolha o número de inicio: "))
maior = int(input("Escolha o número de parada: "))

# Número mínimo de adivinhação = log 2 (limite superior - limite inferior + 1)
tentativas = int(m.log2(maior-menor+1))
num_sorteado = r(menor, maior)

print()
print(f'Você terá {tentativas} tentativas')

cont=0
while cont!=tentativas:
    num= int(input("--> "))
    if num==num_sorteado:
        print('Parabéns, você acertou!!!')
        break
    if num<num_sorteado:
        print('Tente novamente! Você adivinhou muito pequeno.')
    elif num>num_sorteado:
        print('Tente novamente! Você adivinhou muito alto.')
    cont+=1
    print()
else:
    print(f'Não foi dessa vez, o número era o {num_sorteado}, boa sorte na próxima.')