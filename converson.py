def conversor(horas, minutos):
    novaHora = hora if hora <= 12 else hora - 12
    A_ou_P = "AM" if hora < 12 else "PM"
    return str(novaHora) + ":" + str(minutos) + A_ou_P


while True:
    hora = int(input("Informe a hora : "))
    if hora == 0:
        break
    minutos = int(input("Informe os minutos : "))
    print(conversor(hora, minutos))
