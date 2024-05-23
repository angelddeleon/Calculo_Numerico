def dec_bin(n):
    numeros = []
    cocientes = n
    resultado = ""

    while cocientes >= 2:
        cocientes = cocientes // 2
        resto = cocientes % 2
        numeros = [f"{resto}"] + numeros

    unidades = n % 2
    numeros.append(f"{unidades}")

    resultado = int("".join(numeros))

    return resultado

def dec_ter(n):
    numeros = []
    cocientes = n
    resultado = ""

    while cocientes >= 3:
        cocientes = cocientes // 3
        resto = cocientes % 3
        numeros = [f"{resto}"] + numeros

    unidades = n % 3
    numeros.append(f"{unidades}")

    resultado = int("".join(numeros))

    return resultado

def dec_cua(n):
    numeros = []
    cocientes = n
    resultado = ""

    while cocientes >= 4:
        cocientes = cocientes // 4
        resto = cocientes % 4
        numeros = [f"{resto}"] + numeros

    unidades = n % 4
    numeros.append(f"{unidades}")

    resultado = int("".join(numeros))

    return resultado

def dec_oct(n):
    numeros = []
    cocientes = n
    resultado = ""

    while cocientes >= 8:
        cocientes = cocientes // 8
        resto = cocientes % 8
        numeros = [f"{resto}"] + numeros

    unidades = n % 8
    numeros.append(f"{unidades}")

    resultado = int("".join(numeros))

    return resultado


def dec_hex(n):
    numeros = []
    cocientes = n
    resultado = ""

    while cocientes >= 16:
        cocientes = cocientes // 16
        resto = cocientes % 16
        numeros = [f"{resto}"] + numeros

    unidades = n % 16
    numeros.append(f"{unidades}")

    resultado = int("".join(numeros))

    return resultado

def bin_dec(n):
    numeros = list(map(int, str(n)))
    numerosAlreves = numeros[::-1]

    numeroIteraciones = len(numeros)

    suma = 0

    for x in range(numeroIteraciones):
        
        numerosElevados = numerosAlreves[x] * (2 ** x)

        print(numerosElevados)

        suma += numerosElevados

    return suma

def ter_dec(n):
    numeros = list(map(int, str(n)))
    numerosAlreves = numeros[::-1]

    numeroIteraciones = len(numeros)

    suma = 0

    for x in range(numeroIteraciones):
        
        numerosElevados = numerosAlreves[x] * (3 ** x)

        print(numerosElevados)

        suma += numerosElevados

    return suma

def cua_dec(n):
    numeros = list(map(int, str(n)))
    numerosAlreves = numeros[::-1]

    numeroIteraciones = len(numeros)

    suma = 0

    for x in range(numeroIteraciones):
        
        numerosElevados = numerosAlreves[x] * (4 ** x)

        print(numerosElevados)

        suma += numerosElevados

    return suma

def oct_dec(n):
    numeros = list(map(int, str(n)))
    numerosAlreves = numeros[::-1]

    numeroIteraciones = len(numeros)

    suma = 0

    for x in range(numeroIteraciones):
        
        numerosElevados = numerosAlreves[x] * (8 ** x)

        print(numerosElevados)

        suma += numerosElevados

    return suma

def hex_dec(n):
    numeros = list(map(int, str(n)))
    numerosAlreves = numeros[::-1]

    numeroIteraciones = len(numeros)

    suma = 0

    for x in range(numeroIteraciones):
        
        numerosElevados = numerosAlreves[x] * (16 ** x)

        print(numerosElevados)

        suma += numerosElevados

    return suma

def bin_ter(n):
    resultadoTerADec = bin_dec(n)

    resultado = dec_ter(resultadoTerADec)

    return resultado

def bin_cua(n):
    resultadoTerADec = bin_dec(n)

    resultado = dec_cua(resultadoTerADec)

    return resultado

def bin_oct(n):
    resultadoTerADec = bin_dec(n)

    resultado = dec_oct(resultadoTerADec)

    return resultado

def bin_hex(n):
    resultadoTerADec = bin_dec(n)

    resultado = dec_hex(resultadoTerADec)

    return resultado

def ter_bin(n):
    resultadoTerADec = ter_dec(n)

    resultado = dec_bin(resultadoTerADec)

    return resultado

def ter_cua(n):
    resultadoTerADec = ter_dec(n)

    resultado = dec_cua(resultadoTerADec)

    return resultado

def ter_oct(n):
    resultadoTerADec = ter_dec(n)

    resultado = dec_oct(resultadoTerADec)

    return resultado

def ter_hex(n):
    resultadoTerADec = ter_dec(n)

    resultado = dec_hex(resultadoTerADec)

    return resultado

def cua_bin(n):
    resultadoTerADec = cua_dec(n)

    resultado = dec_bin(resultadoTerADec)

    return resultado

def cua_ter(n):
    resultadoTerADec = cua_dec(n)

    resultado = dec_ter(resultadoTerADec)

    return resultado

def cua_oct(n):
    resultadoTerADec = cua_dec(n)

    resultado = dec_oct(resultadoTerADec)

    return resultado

def cua_hex(n):
    resultadoTerADec = cua_dec(n)

    resultado = dec_hex(resultadoTerADec)

    return resultado

def oct_bin(n):
    resultadoTerADec = oct_dec(n)

    resultado = dec_bin(resultadoTerADec)

    return resultado

def oct_ter(n):
    resultadoTerADec = oct_dec(n)

    resultado = dec_ter(resultadoTerADec)

    return resultado

def oct_cua(n):
    resultadoTerADec = oct_dec(n)

    resultado = dec_cua(resultadoTerADec)

    return resultado

def oct_hex(n):
    resultadoTerADec = oct_dec(n)

    resultado = dec_hex(resultadoTerADec)

    return resultado

def hex_bin(n):
    resultadoTerADec = hex_dec(n)

    resultado = dec_bin(resultadoTerADec)

    return resultado

def hex_ter(n):
    resultadoTerADec = hex_dec(n)

    resultado = dec_ter(resultadoTerADec)

    return resultado

def hex_cua(n):
    resultadoTerADec = hex_dec(n)

    resultado = dec_cua(resultadoTerADec)

    return resultado

def hex_oct(n):
    resultadoTerADec = hex_dec(n)

    resultado = dec_oct(resultadoTerADec)

    return resultado

