def somador_de_imposto(t, c):
    Imposto = c + (c * t / 100)
    return Imposto


print(f'O resultado é igual a {somador_de_imposto(5, 12):.2f}')