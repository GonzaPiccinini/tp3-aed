import os

def leer_archivo(archivo):
    # ... inicializar variables ...
    lineas = ()

    # ... inicializar variables auxiliares ...
    indice_car = 0
    saltos_linea = 0
    saltos_indice = ()

    # ... abrir archivo ...
    archivo_abierto = open(archivo, 'rt')
    tipo_control = "SC"
    if "HC" in archivo_abierto.readline():
        tipo_control = "HC"

    # ... leer archvo ...
    archivo_leido = archivo_abierto.read()
    
    # ... iterar caracteres del archivo leído ...
    for caracter in archivo_leido:
        # ... validar si el caracter es un salto de línea ...
        if caracter == '\n':
            # ... acumular cantidad de veces que se repite el salto de línea y agregar el índice del mismo a una tupla ...
            saltos_linea += 1
            saltos_indice += indice_car,
        
        # ... acumular índice del caracter ...
        indice_car += 1

    # ... iterar índices de todos los saltos de línea ...
    for i in range(saltos_linea):
        # ... validar si es la primer iteración ...
        if i == 0:
            # ... inicializar variable que contendrá el índice del caracter inicial de cada línea nueva ...
            inicio_linea = 0

            # ... agregar línea nueva a la tupla que contendrá todas las líneas del archivo mediante un slice
            # que toma como índice inicial al índice del caracter inicial de cada línea nueva, y toma como índice final
            # al índice del salto de línea final de cada línea ...
            lineas += archivo_leido[inicio_linea:saltos_indice[i]],
        
        else:
            # ... inicializar variable que contendrá el índice del caracter inicial de cada línea nueva ...
            inicio_linea = saltos_indice[i-1] 

            # ... validar si existe algún caracter en la nueva línea ...
            if archivo_leido[inicio_linea + 1:saltos_indice[i]] != '':
                # ... agregar línea nueva a la tupla que contendrá todas las líneas del archivo mediante un slice
                # que toma como índice inicial al índice del caracter inicial de cada línea nueva, y toma como índice final
                # al índice del salto de línea final de cada línea ...
                lineas += archivo_leido[inicio_linea + 1:saltos_indice[i]],
    
    # ... validar si existe algún caracter en la última línea ...
    if archivo_leido[saltos_indice[-1] + 1:len(archivo_leido)] != '':
        # ... agregar la última línea a la tupla que contendrá todas las líneas del archivo mediante un slice
        # que toma como índice inicial al índice del salto de línea final, y toma como índice final
        # al índice del último elemento de la última línea ...
        lineas += archivo_leido[saltos_indice[-1] + 1:len(archivo_leido)],

    # ... retornar líneas del archivo ...
    return tipo_control, lineas

def validar_direccion(direccion):
    cl = cd = 0
    td = False
    ant = " "
    for car in direccion:
        if car in " .":
            # fin de palabra...
            # un flag si la palabra tenia todos sus caracteres digitos...
            if cl == cd:
                td = True

            # resetear variables de uso parcial...
            cl = cd = 0
            ant = " "

        else:
            # en la panza de la palabra...
            # contar la cantidad de caracteres de la palabra actual...
            cl += 1

            # si el caracter no es digito ni letra, la direccion no es valida... salir con False...
            if not car.isdigit() and not car.isalpha():
                return False

            # si hay dos mayusculas seguidas, la direccion no es valida... salir con False...
            if ant.isupper() and car.isupper():
                return False

            # contar digitos para saber si hay alguna palabra compuesta solo por digitos...
            if car.isdigit():
                cd += 1

            ant = car

    # si llegamos acá, es porque no había dos mayusculas seguidas y no habia caracteres raros...
    # ... por lo tanto, habria que salir con True a menos que no hubiese una palabra con todos digitos...
    return td

def obtener_datos_envio(envio): 
    cp = envio[0:9].strip()
    direccion = envio[9:29].strip()
    tipo = int(envio[29])
    pago = int(envio[30])
    return (cp, direccion, tipo, pago)  

def obtener_pais_destino(codigo_postal):
        n = len(codigo_postal)
        if n < 4 or n > 9:
            return 'Otro'

        # ¿es Argentina?
        if n == 8:
            if codigo_postal[0].isalpha() and codigo_postal[0] not in 'IO' and codigo_postal[1:5].isdigit() and codigo_postal[5:8].isalpha():
                return 'Argentina'
            else:
                return 'Otro'

        # ¿es Brasil?
        if n == 9:
            if codigo_postal[0:5].isdigit() and codigo_postal[5] == '-' and codigo_postal[6:9].isdigit():
                return 'Brasil'
            else:
                return 'Otro'

        if codigo_postal.isdigit():
            # ¿es Bolivia?
            if n == 4:
                return 'Bolivia'

            # ¿es Chile?
            if n == 7:
                return 'Chile'

            # ¿es Paraguay?
            if n == 6:
                return 'Paraguay'

            # ¿es Uruguay?
            if n == 5:
                return 'Uruguay'

        # ...si nada fue cierto, entonces sea lo que sea, es otro...
        return 'Otro'  

def generar_arreglo_cp(arreglo_envios):
    arreglo_cp = []
    for envio in arreglo_envios:
        arreglo_cp.append(envio.codigo_postal.strip())
    return arreglo_cp

def ordenar_codigos_postales(arreglo_envios):
    codigos = generar_arreglo_cp(arreglo_envios)
    n = len(codigos)

    for i in range(n):
        for j in range(0, n - i - 1):
            if (codigos[j].isdigit() and codigos[j + 1].isdigit()) or \
               (not codigos[j].isdigit() and not codigos[j + 1].isdigit()):
                if codigos[j] > codigos[j + 1]:
                    codigos[j], codigos[j + 1] = codigos[j + 1], codigos[j]
                    arreglo_envios[j], arreglo_envios[j + 1] = arreglo_envios[j + 1], arreglo_envios[j]
            elif not codigos[j].isdigit() and codigos[j + 1].isdigit():
                codigos[j], codigos[j + 1] = codigos[j + 1], codigos[j]
                arreglo_envios[j], arreglo_envios[j + 1] = arreglo_envios[j + 1], arreglo_envios[j]

    return arreglo_envios

def limpiar_consola():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')        
