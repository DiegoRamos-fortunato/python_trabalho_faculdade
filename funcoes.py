from math import sin, cos, tan, sqrt

# funções

def operacoes_basicas(a, b, opcao):
    if opcao == 1:
        soma = a + b
        return soma
    elif opcao == 2:
        subtracao = a - b
        return subtracao
    elif opcao == 3:
        multiplicacao = a * b
        return multiplicacao
    elif opcao == 4:
        divisao = a / b
        return divisao

def raiz(a):
    raizquadrada = sqrt(a)
    return raizquadrada

def potencia(a,b):
    potencia = pow(a,b)
    return potencia

def seno_cos_tang(a,opcao):
    if opcao == 1:
        seno = sin(a)
        return seno
    elif opcao == 2:
        cosseno = cos(a)
        return cosseno
    elif opcao == 3:
        tangente = tan(a)
        return tangente