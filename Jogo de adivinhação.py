#colocar no git hub
import random
palpites = 0
num = random.randint(0, 5)
tentativa = 1
while tentativa != num:
    tentativa = int(input("Adivinhe o número que eu escolhi entre 0 e 5!! Escreva aqui: "))
    palpites  +=  1
print("Você venceu uhuuu! Você tentou", palpites," vezes antes de acertar")
