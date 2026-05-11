import random
import time
numPes = 0
numPC = 0
opc = ""
opcPC = ""
soma = 0
qtd = 0
print(''' 
        ── Bem-Vindo ao jogo de impar ou Par ──
    Divirta-se jogando contra o propio sistema!''')
while True: 
    try:
        numPes=int(input("Digite seu número: ")) #escolhe o número
    except ValueError:
        print("ERRO! Digite um número inteiro por favor tente novamente")
        continue
    opc = input("Você escolhe impar(I) ou par(P)? (I ou P?) ").strip().upper()[0]
    if opc != "I" and opc != "P":
          print("ERRO! Digite um número inteiro por favor tente novamente")
          continue
    lista = ["P", "I"]
    opcPC = random.choice(lista)
    numPC =random.randint(1, 100)
    soma = numPes + numPC #faz a soma
    for i in range (1, 4):
          time.sleep(0.5)
          print(i)
    print('JÁ!')
    print(f'''
⤿ Você escolheu {numPes} e {opc}, já o sistema escolheu {numPC} e {opcPC}.
O total deu {soma} e esse número é {"par" if soma%2==0 else "impar"}!
    ''')
    if soma % 2 ==0 and opc == "P" and opcPC == "I" or soma % 2 !=0 and opc == "I" and opcPC =="P": # pessoa ganha
            print("VOCÊ Ganhou!! ")
            qtd+=1
            continue
    elif soma % 2 ==0 and opc == "P" and opcPC == "P" or soma % 2 !=0 and opc == "I" and opcPC =="I": #empate
        print("Houve um empate!!")
        break
    elif soma % 2 ==0 and opc == "I" and opcPC == "I" or soma % 2 !=0 and opc == "P" and opcPC == "P": #td mundo perde
          print("Todo mundo perdeu!!")
          break
    else:
         print("A maquina ganhou e você perdeu!")
         break
print(f"Você ganhou {qtd} vezes.")