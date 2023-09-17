print("___________________________________________________")
print("  ======   =====  =====  ==       ==   ====")
print("    ==     =      =    = = =     = = =      =")
print("    ==     =====  =====  =  =   =  = =      =")
print("    ==     =      =   =  =   = =   = =      =")
print("    ==     =====  =    = =    =    =   ==== ")
print("___________________________________________________")

print("Você quer medir a temperatura?")
resp = input().lower().strip()
if resp == "sim":
    print("Qual escala você quer usar?")
    print("[1] Para Kelvin")
    print("[2] Para Fahrenheit"
          "\n[3] Para Celsius")

    while True:
        try:
            rest = int(input())
            break
        except:
            print("Escolher um valor entre 1, 2 e 3")
    if rest == 1:
        print("Qual temperatura está em Kelvin?")
        kel_resp = float(input())
        if 288.15 <= kel_resp <= 293.15:  # frio 20 celsius
            print("Está ficando frio coloque um agasalho")
        elif 282.15 <= kel_resp <= 288.14:  # frio 15 graus
            print("Está Bem frio se aqueça e não fique muito tempo fora")
        elif -273.15 <= kel_resp <= 282.15:  # frio max até 0 graus
            print("Não saia de casa a menos que seja extremamente importante, está congelando.")
        elif 293.25 <= kel_resp <= 297.15:  # fresco 24 graus
            print("Está fresquinho.")
        elif 297.25 <= kel_resp <= 303.15:  # esquentando 30 graus
            print("Está esquentando")
        elif 303.25 <= kel_resp <= 313.15:  # QUENTE
            print("  Está bem quente    "
                  "\nHidrate-se bastante")
        else:
            print("Valor não reconhecido")

    if rest == 2:
        print("Qual temperatura está em Fahrenheit?")
        fah_resp = float(input())
        if 59 <= fah_resp <= 68:  # frio 20 celsius
            print("Está ficando frio coloque um agasalho")
        elif 48.2 <= fah_resp <= 58.982:  # frio 15 graus
            print("Está Bem frio se aqueça e não fique muito tempo fora")
        elif 32 <= fah_resp <= 48.2:  # frio max até 0 graus
            print("Não saia de casa a menos que seja extremamente importante, está congelando.")
        elif 68.18 <= fah_resp <= 75.2:  # fresco 24 graus
            print("Está fresquinho.")
        elif 75.38 <= fah_resp <= 86:  # esquentando 30 graus
            print("Está esquentando")
        elif 86.18 <= fah_resp <= 104:  # QUENTE
            print("  Está bem quente    "
                  "\nHidrate-se bastante")
        else:
            print("Valor não reconhecido")

    if rest == 3:
        print("Qual temperatura está em Fahrenheit?")
        cel_resp = float(input())
        if 15 <= cel_resp <= 20:  # frio 20 celsius
            print("Está ficando frio coloque um agasalho")
        elif 9 <= cel_resp <= 14.99:  # frio 15 graus
            print("Está Bem frio se aqueça e não fique muito tempo fora")
        elif 0 <= cel_resp <= 9:  # frio max até 0 graus
            print("Não saia de casa a menos que seja extremamente importante, está congelando.")
        elif 20.1 <= cel_resp <= 24:  # fresco 24 graus
            print("Está fresquinho.")
        elif 24.1 <= cel_resp <= 30:  # esquentando 30 graus
            print("Está esquentando")
        elif 30.1 <= cel_resp <= 40:  # QUENTE
            print("  Está bem quente    "
                  "\nHidrate-se bastante")
        else:
            print("Valor não reconhecido")
else:
    print("Ok Muito Obrigada"
          "\nPrograma será"
          "\n Encerrado")
