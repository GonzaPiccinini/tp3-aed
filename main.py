import envios
import utils
import os

def menu():
    utils.limpiar_consola()
    opcion = None
    arreglo_envios = []
    tipo_control = "HC"
    vect_cont_inicializado = False

    while(opcion != "0"):
        opcion = None
        encontrado = False
        if opcion == None:
            opcion = input("\tSistema Simple de Gestión de Envíos por Correo \n" + 
                "1. Cargar archivo y crear arreglo de envíos desde cero \n" +
                "2. Cargar datos de un envío manualmente y agreagarlos al arreglo de envíos \n" +
                "3. Mostrar una cantidad determinada de envíos ordenados alfanuméricamente por sus códigos postales \n" +
                "4. Buscar un envío por su dirección y tipo de envío \n" + 
                "5. Buscar un envío por su código postal y cambiar método de pago \n" +
                "6. (CONTROL) Mostrar cantidad de envíos con dirección válida y separarla por tipo de envío \n" + 
                "7. (CONTROL) Mostrar importe final acumulado y separalo por tipo de envío \n" + 
                "8. Mostrar el tipo de envío con mayor importe final acumulado e indicar el porcentaje que representa sobre el importe total acumulado \n" + 
                "9. Mostrar importe final promedio entre todos los envíos e indicar cuantos envíos tuvieron menor importe final que dicho importe \n" + 
                "0. Salir del programa \n\n" +
                "Elija e ingrese la opción: ")
        

        if not opcion in "0123456789" or opcion == "":
            utils.limpiar_consola()
            print("Opción inválida. Por favor lea el menú de opciones disponibles.")
            input("\n\nPresione una tecla para continuar...")
            utils.limpiar_consola()
            continue
        

        if opcion == "1":
            utils.limpiar_consola()
            if (len(arreglo_envios) != 0):
                adv = input("Se borrarán todos los envíos del arreglo y se generará un nuevo, ¿está seguro de su opción? (1. Sí - 0. No): ")
                while not adv in "01":
                    utils.limpiar_consola()
                    print("Opción inválida. Por favor lea el menú de opciones disponibles. \n")
                    adv = input("Se borrarán todos los envíos del arreglo y se generará un nuevo, ¿está seguro de su opción? (1. Sí - 0. No): ")
                if adv == "0":
                    utils.limpiar_consola()
                    continue
            utils.limpiar_consola()
            nombre_archivo = input("Ingrese el nombre del archivo: ")
            utils.limpiar_consola()
            if not os.path.exists(nombre_archivo):
                print(f"El archivo '{nombre_archivo}' no existe. ")
                input("\n\nPresione una tecla para continuar...")
                utils.limpiar_consola()
                continue
            arreglo_envios = []
            tipo_control, tupla_envios = utils.leer_archivo(nombre_archivo)
            for envio in tupla_envios:
                cp, direccion, tipo, pago = utils.obtener_datos_envio(envio)
                envio = envios.Envio(cp, direccion, tipo, pago)
                arreglo_envios.append(envio)
            print(f"Los registros del archivo '{nombre_archivo}' fueron creados y cargados correctamente. ")
            input("\n\nPresione una tecla para continuar...")
            utils.limpiar_consola()
        

        if opcion == "2":
            utils.limpiar_consola()
            print("El código postal debe contener entre 4 y 9 caracteres y sólo debe contener letras y números. \n")
            cp = input("Ingrese el código postal: ")
            while not 4 <= len(cp.strip()) <= 9 or not cp.strip().isalnum():
                utils.limpiar_consola()
                print("El código postal debe contener entre 4 y 9 caracteres y sólo debe contener letras y números. \n")
                cp = input("Ingrese el código postal: ")
            utils.limpiar_consola()
            print("La dirección: \n" +
                  "\t* Debe contener entre 6 y 20 caracteres \n" + 
                  "\t* Debe contener sólo letras y números \n" +
                  "\t* No debe contener dos mayúsculas seguidas \n" + 
                  "\t* Debe haber una palabra compuesta sólo por dígitos \n")
            direccion = input("Ingrese la dirección: ")
            while not 6 <= len(direccion) <= 20 or not utils.validar_direccion(direccion + "."):
                utils.limpiar_consola()
                print("La dirección: \n" +
                      "\t* Debe contener entre 6 y 20 caracteres \n" + 
                      "\t* Debe contener sólo letras y números \n" +
                      "\t* No debe contener dos mayúsculas seguidas \n" + 
                      "\t* Debe haber una palabra compuesta sólo por dígitos \n")
                direccion = input("Ingrese la dirección: ")
            utils.limpiar_consola()
            print("Tipos de envío disponibles: \n" +
                  "0. Carta Simple      - (peso < 20)         - $1100 \n" +
                  "1. Carta Simple      - (20 <= peso < 150)  - $1800 \n" +
                  "2. Carta Simple      - (150 <= peso < 500) - $2450 \n" +
                  "3. Carte certificada - (peso < 150)        - $8300 \n" +
                  "4. Carte certificada - (150 <= peso < 500) - $10900 \n" +
                  "5. Carta Expresa     - (peso < 150)        - $14300 \n" +
                  "6. Carta Expresa     - (150 <= peso < 500) - $17900 \n")
            tipo = input("Ingrese el tipo de envío: ")
            while not tipo.isnumeric() or not tipo in "0123456":
                utils.limpiar_consola()
                print("El tipo de envío debe ser un número y las opciones disponibles son: ")
                print("0. Carta Simple      - (peso < 20)         - $1100 \n" +
                      "1. Carta Simple      - (20 <= peso < 150)  - $1800 \n" +
                      "2. Carta Simple      - (150 <= peso < 500) - $2450 \n" +
                      "3. Carte certificada - (peso < 150)        - $8300 \n" +
                      "4. Carte certificada - (150 <= peso < 500) - $10900 \n" +
                      "5. Carta Expresa     - (peso < 150)        - $14300 \n" +
                      "6. Carta Expresa     - (150 <= peso < 500) - $17900 \n")
                tipo = input("Ingrese el tipo de envío: ")
            utils.limpiar_consola()
            print("Formas de pago disponibles: ")
            print("1. Efectivo (10% de descuento) \n" +
                  "2. Tarjeta de crédito \n")
            pago = input("Ingrese la forma de pago: ")
            while not pago.isnumeric() or not pago in "12":
                utils.limpiar_consola()
                print("La forma de pago debe ser un número y las opciones disponibles son: \n" +
                      "1. Efectivo (10% de descuento) \n" +
                      "2. Tarjeta de crédito \n")
                pago = input("Ingrese la forma de pago: ")
            utils.limpiar_consola()
            arreglo_envios.append(envios.Envio(cp, direccion.strip() + ".", int(tipo), int(pago)))
            print(f"El envío [{arreglo_envios[-1]}] fue creado y agregado al arreglo de envíos correctamente.")
            input("\n\nPresione una tecla para continuar...")
            utils.limpiar_consola()
        

        if opcion == "3":
            utils.limpiar_consola()
            if len(arreglo_envios) == 0:
                input("\n\nPresione una tecla para continuar...")
                utils.limpiar_consola()
                print("No hay envíos registrados. \n")
                continue
            arreglo_envios = utils.ordenar_codigos_postales(arreglo_envios)
            limite = input("Ingrese la cantidad de envíos que desea mostrar (0. mostrar todos): ")
            utils.limpiar_consola()
            while not limite.isnumeric() or int(limite) > len(arreglo_envios):      
                print(f"La cantidad debe ser un número y debe ser menor o igual a {len(arreglo_envios)}. \n") 
                limite = input("Ingrese la cantidad de envíos que desea mostrar (0. mostrar todos): ")
            if int(limite) != 0:
                for i in range(0, int(limite)):
                    print(f"País destino: {arreglo_envios[i].obtener_pais_destino()}, {arreglo_envios[i]}")
                print("\nCantidad de envíos mostrados:", limite)
            elif int(limite) == 0:
                for envio in arreglo_envios:
                    print(envio)
                print("\nCantidad de envíos mostrados:", len(arreglo_envios))
            input("\n\nPresione una tecla para continuar...")
            utils.limpiar_consola()
        

        if opcion == "4":
            utils.limpiar_consola()
            if len(arreglo_envios) == 0:
                print("No hay envíos registrados. \n")
                input("\n\nPresione una tecla para continuar...")
                utils.limpiar_consola()
                continue
            d = input("Ingrese la dirección del envío que desea encontrar: ")
            e = input("Ingrese el tipo del envío que desea encontrar: ")
            if not d.strip()[-1] == ".":
                d += "."
            for envio in arreglo_envios:
                if (envio.direccion == d.strip()) and (envio.tipo_envio == int(e)):
                    encontrado = True
                    utils.limpiar_consola()
                    print(f"El envío con dirección '{d}' y tipo de envío '{e}' corresponde a: \n{envio}")
                    input("\n\nPresione una tecla para continuar...")
                    utils.limpiar_consola()
                    break
            if not encontrado:
                utils.limpiar_consola()
                print(f"No se encontró ningún envío con dirección '{d}' y tipo de envío '{e}' \n")
                input("\n\nPresione una tecla para continuar...")
                utils.limpiar_consola()
          

        if opcion == "5":
            utils.limpiar_consola()
            if len(arreglo_envios) == 0:
                print("No hay envíos registrados. \n")
                input("\n\nPresione una tecla para continuar...")
                utils.limpiar_consola()
                continue
            codigo_postal = input("Ingrese el código postal del envío que desea encontrar: ")
            for envio in arreglo_envios:
                if envio.codigo_postal.strip() == codigo_postal:
                    encontrado = True
                    utils.limpiar_consola()
                    print(f"El envío con código postal '{codigo_postal}' corresponde a: \n{envio} \n" )
                    print("Cambiando forma de pago... \n")
                    if envio.forma_pago == 1:
                        envio.forma_pago = 2
                    elif envio.forma_pago == 2:
                        envio.forma_pago = 1
                    print(f"Envío actualizado: \n{envio}")
                    input("\n\nPresione una tecla para continuar...")
                    utils.limpiar_consola()
                    break
            if not encontrado:
                utils.limpiar_consola()
                print(f"No se encontró ningún envío con código postal '{codigo_postal}' \n")
                input("\n\nPresione una tecla para continuar...")
                utils.limpiar_consola()


        if opcion == "6":
            utils.limpiar_consola()
            if len(arreglo_envios) == 0:
                print("No hay envíos registrados. \n")
                input("\n\nPresione una tecla para continuar...")
                utils.limpiar_consola()
                continue
            utils.limpiar_consola()
            vector_conteo_tipo = 7 * [0]
            if tipo_control == "HC":
                for envio in arreglo_envios:
                    if utils.validar_direccion(envio.direccion):
                        vector_conteo_tipo[envio.tipo_envio] += 1
            elif tipo_control == "SC":
                for envio in arreglo_envios:
                    vector_conteo_tipo[envio.tipo_envio] += 1
            print("Cantidad de envíos por tipo: ")
            for i in range(len(vector_conteo_tipo)):
                print(f"Tipo {i}: {vector_conteo_tipo[i]}")
            input("\n\nPresione una tecla para continuar...")
            utils.limpiar_consola()

        if opcion == "7":
            utils.limpiar_consola()
            if len(arreglo_envios) == 0:
                print("No hay envíos registrados. \n")
                input("\n\nPresione una tecla para continuar...")
                utils.limpiar_consola()
                continue
            vector_conteo_importe = 7 * [0]
            if tipo_control == "HC":
                for envio in arreglo_envios:
                    if utils.validar_direccion(envio.direccion):
                        importe_final = envio.obtener_importe_final()
                        vector_conteo_importe[envio.tipo_envio] += importe_final
            elif tipo_control == "SC":
                for envio in arreglo_envios:
                    importe_final = envio.obtener_importe_final()
                    vector_conteo_importe[envio.tipo_envio] += importe_final
            vect_cont_inicializado = True
            print("Importes finales acumulados por tipo de envío: ")
            for i in range(len(vector_conteo_importe)):
                print(f"Tipo {i}: ${vector_conteo_importe[i]}")
            input("\n\nPresione una tecla para continuar...")
            utils.limpiar_consola()
            

        if opcion == "8":
            utils.limpiar_consola()
            if len(arreglo_envios) == 0:
                print("No hay envíos registrados. \n")
                input("\n\nPresione una tecla para continuar...")
                utils.limpiar_consola()
                continue
            if not vect_cont_inicializado:
                print("No hay importes acumulados. \n")
                input("\n\nPresione una tecla para continuar...")
                utils.limpiar_consola()
                continue
            porc_importe_mayor = vector_conteo_importe[0]
            for i in range(1, len(vector_conteo_importe)):
                porc_importe_mayor += vector_conteo_importe[i]
                if vector_conteo_importe[i - 1] > vector_conteo_importe[i]:
                    vector_conteo_importe[i - 1], vector_conteo_importe[i] = vector_conteo_importe[i], vector_conteo_importe[i - 1]
            tipo_importe_mayor = len(vector_conteo_importe) - 1
            porc_importe_mayor = vector_conteo_importe[tipo_importe_mayor] * 100 // porc_importe_mayor
            print(f"El mayor importe acumulado corresponde al tipo de envío #{tipo_importe_mayor}.")
            print(f"Dicho importe representa el {porc_importe_mayor}% sobre el 100% del importe final acumulado.")
            input("\n\nPresione una tecla para continuar...")
            utils.limpiar_consola()

        if opcion == "9":
            utils.limpiar_consola()
            if len(arreglo_envios) == 0:
                print("No hay envíos registrados. \n")
                input("\n\nPresione una tecla para continuar...")
                utils.limpiar_consola()
                continue
            importe_final_promedio = 0
            for envio in arreglo_envios:
                importe_final_promedio += envio.obtener_importe_final()
            importe_final_promedio //= len(arreglo_envios)
            cantidad_envio_menores = 0
            for envio in arreglo_envios:
                if envio.obtener_importe_final() < importe_final_promedio:
                    cantidad_envio_menores += 1
            print(f"El importe final promedio entre todos les envíos registrados es ${importe_final_promedio}.")
            print(f"Hay {cantidad_envio_menores} envíos registrados que tuvieron un importe menor al importe final promedio.")
            input("\n\nPresione una tecla para continuar...")
            utils.limpiar_consola()  

    return 
    
def main():  
    menu()

if __name__ == "__main__":
    main()