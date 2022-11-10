from funcoes import operacoes_basicas,raiz,potencia,seno_cos_tang

continuar = ''

while True:
    operacao = int(input('Digite uma opção : [1]operações basicas [2]raiz quadrada [3]potencia [4]funções trigonometricas : '))
    if operacao == 1:
        valor1 = float(input('Digite um valor : '))
        valor2 = float(input('Digite um valor : '))
        opcao = float(input('Escolha uma opção :[1] SOMA  [2] SUBTRAÇÃO [3] MULTIPLICAÇÃO [4] DIVISÃO :  '))
        print(f'O Resultado da operação é {operacoes_basicas(valor1, valor2, opcao):.2f}')
    elif operacao == 2:
        valor = float(input('Digite um valor :'))
        print(f'O valor da raiz quadrada de {valor} é : {raiz(valor):.2f}')
    elif operacao == 3:
        base = float(input('Digite a base : '))
        elevado = float(input('Digite a potencia : ')) 
        print(f'O valor da potencia do número {base} elevado a {elevado} é {potencia(base, elevado):.2f}')
    elif operacao == 4:
        valor1 = float(input('Digite um valor : '))
        opcao = float(input('Escolha uma opção :[1] SENO [2] COSSENO [3] TANGENTE :  '))
        print(f'O Resultado da operação é {seno_cos_tang(valor1, opcao):.2f}')
    else:
        print(f'A opção {operacao} é invalida, por favor digite uma opção valida : ')
    continuar = input('Dejesa continuar ? [S/N] : ').upper().strip()
    if continuar == 'N':
        break


    
    
    