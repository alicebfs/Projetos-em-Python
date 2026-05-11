opc = 1
valortotal = 0
qtd = 0
pedidos = ""
while opc !=0:
    try:
        opc = int(input('''
              ⤿ Menu de categorias  
1- Filmes
2- Combos (Pipocas e bebidas)
3- finalizar compra
Informe a categoria escolhida:     '''))
    except ValueError:
        print("ERRO! Digite um número inteiro, por favor tente novamente")
        continue
    if opc == 3:
        break
    match opc:
        case 1:
            filmes = int(input('''
               | Filmes |     
1- Filme 2D (R$12)
2- Filme 3D (R$18)
Informe o tipo de filme escolhido:    '''))
            match filmes:
                case 1:
                    quantidadeingressos= int(input("Quantidade: "))
                    valor2d = quantidadeingressos * 12
                    qtd += quantidadeingressos
                    valortotal += valor2d
                    pedidos += f"{quantidadeingressos}x ingressos. \n" 
                    print(f'''
Você escolheu o ingresso para filmes 2D.
Subtotal: R${valor2d} ''')
                    if quantidadeingressos <= 0:
                        print("Valor inválido, tente novamente!")
                        continue
                case 2:
                    quantidade3d = int(input("Quantidade: "))
                    valor3d = quantidade3d * 18
                    qtd += quantidade3d
                    valortotal += valor3d
                    print(f'''
Você escolheu o ingresso para filmes 3D.
Subtotal: R${valor3d} ''')
                    if quantidade3d <= 0:
                        print("Valor inválido, tente novamente!")
                        continue
                case _:
                    print("Valor inválido, tente novamente!")
                    continue
        case 2:
            combos = int(input('''
               | Combos |     
1- Pipoca pequena (R$6)
2- Combo pipoca + refrigerante (R$10)
Informe o produto escolhido:  '''))
            match combos:
                case 1:
                    quantidadepipoca = int(input("Quantos pacotes de pipoca pequena você quer: "))
                    valorpp = quantidadepipoca * 6
                    qtd += quantidadepipoca
                    valortotal += valorpp
                    print(f'''
Você escolheu {quantidadepipoca} unidade(s).
Subtotal: R${valorpp} ''')
                    if quantidadepipoca <= 0:
                        print("Valor inválido, tente novamente!")
                        continue
                case 2:
                    quantidadepr = int(input("Quantos combos você deseja: "))
                    valorpr = quantidadepr * 10
                    qtd += quantidadepr
                    valortotal += valorpr
                    print(f'''
Você escolheu {quantidadepr} unidade(s).
Subtotal: R${valorpr} ''')
                    if quantidadepr <=0:
                        print("Valor inválido, tente novamente!")
                        continue
                case _:
                    print("Valor inválido, tente novamente!")
                    continue
print(pedidos)
print(f"Total de itens: {qtd}")
if valortotal > 50:
    print(f"Valor total: R${valortotal}")
    valortotal = valortotal - valortotal * 0.1
    print(f'''
Desconto aplicado!
Valor total: R${valortotal}''')
else:
    print(f"Valor total: R${valortotal}")
print("obrigado pela compra!")
            