
#Dict con características de un juego 
dicDatosJuego = {}   

#Archivo json para guardar/cargar la base de datos:
import json
with open("database.json","r") as archivo:
    dicJuegos = json.load(archivo)             #Dict con todos los juegos. Clave:el nombre del juego, value: dicDatosJuego
    
#Función para editar productos:
def editarDic(dic):
    
    keyAEditar = input("Ingresar característica a editar: ").title()
    
    if keyAEditar == "Código":
        valueEditado = checkCodigo(dicJuegos).title()
        dic[keyAEditar] = valueEditado
        print(f"---------------------------\nEl juego {nombreJuego} fue editado\n---------------------------\n")
        printJuegos()
        return dic
    elif keyAEditar in dic.keys():
        valueEditado = input(f"Ingrese el nuevo valor de {keyAEditar}: ").title()
        dic[keyAEditar] = valueEditado
        print(f"---------------------------\nEl juego {nombreJuego} fue editado\n---------------------------\n")
        printJuegos()
        return dic
    else: 
        print("\nIngresar una característica válida\n")
        return dic
    
#Función para checkear el código que sea una letra seguida de 4 números:
def checkCodigo(dictionary):   #El parámetro será el diccionario con toda la lista de juegos(para checkear que el código no este repetido)
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    y = True
    while y:
        try:
            string = list(input("Ingresar el código del videojuego: ").title())     #Pasaje de string a list para hacer lo siguiente:
            string[1:5] = map(int,string[1:5])      #Pasaje de string a integers de los 4 ultimos dígitos.
            if len(string)!= 5:                     #Check longitud del código.
                print("\nEl código debe ser de 5 carácteres, empezar con una letra, seguida de 4 números")
                continue
            if string[0].lower() not in alfabeto:   #Check 1er char sea una letra.
                print("\nEl código debe ser de 5 carácteres, empezar con una letra, seguida de 4 números")
                continue    
           
            string2 = ''.join(map(str, string))  #pasaje a string de nuevo para comparar con lo que hay en el diccionario, con map sobre toda la lista previa. Luego Join para unir los elementos sin separarlos.

            for i in dictionary.values():       #Check código no repetido en dicctionario.
                if string2 in i.values():
                    print("\nEste código ya esta en uso para otro producto, por favor ingresar otro diferente")    
                    break                    
            else:
                y = False    #Para salir del loop cuando todas sus condiciones sean correctas.
        except ValueError:
            print("\nEl código debe ser de 5 carácteres, empezar con una letra, seguida de 4 números")  #Check por si los otros chars son letras en vez de números u otro error.
            continue      
    return(string2.title())         #Retorna el código que ingresó el usuario, como una string que empieza con mayúscula y el código checkeado.

#Función para mostrar la lista de juegos actualizada
def printJuegos():
    print("\n------Lista de juegos actualizada------\n---------------------------------------")
    for i in dicJuegos.values():
        dict6 = i
        for key,value in dict6.items():
            print(f"{key}: {value}", end = ", ")
        print("\n")
    print("---------------------------------------\n---------------------------------------\n")

# Logo Intro:        
joystick = r"""
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░▄▄▄▄▄▄▄▄▄░░░░░░░░░░▄▄▄▄▄▄▄▄▄░░░
░▄█▀░░░░░░░▀█▄░░░░░░▄█▀░░░░░░░▀█▄░
▄█░░░░░█▀█░░▀█▄░░░░▄█▀░░███░░░░░█▄
█░░░░░░▀▀▀░░░░▀▀▀▀▀▀░░░░▀█▀░░░░░░█
█░░█▀█░░░░░█▀█░░░░░░███▄▄█▄▄███░░█
█░░▀▀▀░░░░░▀▀▀░░░░░░▀▀▀░░█░░▀▀▀░░█
██▄░░░░█▀█░░░▄█▄░▄█▄░░░░███░░░░▄██
████▄░░▀▀▀░▄█▀▀▀█▀▀▀▀█▄░▀▀▀░░▄████
▀█████▄▄▄▄▄█░░░░░░░░░░█▄▄▄▄▄█████▀
░▀███████▀░░░░░░░░░░░░░░▀███████▀░
░░▀█████▀░░░░░░░░░░░░░░░░▀█████▀░░
░░░▀███▀░░░░░░░░░░░░░░░░░░▀███▀░░░
"""
print("-----------------------------------")
print("-----------Bienvenid@--------------")
print("-------Tienda de Videojuegos-------")
print(joystick)


#Programa:
while True:
    try:
        #Menu Principal
        print("-----------------------------------\n----------Menu Principal-----------\n-----------------------------------") 

        opcionPpal = int(input(("Elija una opción:\n[1] Gestionar Productos(Videojuegos)\n[2] Reportes\n[3] Salir\n")))

        if opcionPpal == 1:
            #Opcion 1: Gestionar productos (Editar/agregar/eliminar)
            print("-------------------------------------")
            print("--Gestionar Productos (Videojuegos)--\n-------------------------------------")   
            while True:        
                opcionGestion = int(input("Elija la opción:\n[1] Ingresar un nuevo producto\n[2] Editar un producto\n[3] Eliminar un producto\n[4] Volver al menú principal\n"))           
            
                #Opcion 1.1 : Agregar juego:
                if opcionGestion == 1:
                    print("----Ingresar un nuevo producto----\n")
                    nombreJuego = input("Ingresar el nombre del videojuego: ").title()
                    #Call para la función que checkea si el código es aceptable, y lo agrega:
                    codigo = checkCodigo(dicJuegos).title()  
                    #Ingreso de datos del juego:
                    dicDatosJuego = {
                        "Nombre":nombreJuego,
                        "Código":codigo,                
                        "Rating":float(input("Ingresar el rating del videojuego (1-10): ")),
                        "Precio":float(input("Ingresar el precio del videojuego: ")),
                        "Año":int(input("Ingresar el año de publicación: "))
                        }
                    dicJuegos[nombreJuego] = dicDatosJuego
                    #Copia a archivo externo, código para que guarde bien los acentos:
                    with open("database.json","w") as archivo:
                        json.dump(dicJuegos, archivo, ensure_ascii=False)
                    #Call función que muestra como quedó la lista actualizada de juegos:
                    printJuegos()
                    

                #Opción 1.2: Editar un juego:
                elif opcionGestion == 2:
                    print("\n------Editar un producto------")
                    printJuegos()
                    nombreJuego = input("\nIngresar nombre del juego a editar: ").title()
                    if nombreJuego in dicJuegos.keys():
                        dicDatosJuego = dicJuegos[nombreJuego]
                        x = editarDic(dicDatosJuego)
                        dicJuegos[nombreJuego] = x

                        with open("database.json","w") as archivo:
                            json.dump(dicJuegos, archivo, ensure_ascii=False)
                        
                    else:
                        print("\nIngresar un juego para editar válido\n")           
                    

                #Opción 1.3: Eliminar un juego de la lista:
                elif opcionGestion == 3:              
                    print("------Eliminar un producto------\n")
                    for i in dicJuegos.values():
                        dict5 = i
                        for key,value in dict5.items():
                            print(f"{key}: {value}", end = ", ")
                        print("\n")
                    nombreJuego = input("\nIngresar nombre del juego a eliminar: ").title()
                    if nombreJuego in dicJuegos.keys():
                        dicJuegos.pop(nombreJuego)

                    with open("database.json","w") as archivo:
                        json.dump(dicJuegos, archivo, ensure_ascii=False)

                    printJuegos()
                    

                #Opción 1.4: Volver a menu principal:
                elif opcionGestion == 4:
                    break

                #Opción inválida:
                else: 
                    print("\nDebe ingresar una opción válida\n")
                    
    
        #Opción 2: Reportes:   
        elif opcionPpal == 2:
            print("-------------------------------")
            print("----------Reportes-------------\n-------------------------------")
            while True:  
                opcionReportes = int(input("[1] Mostrar todos los Productos\n[2] Ordenar por Rating\n[3] Ordenar por Precio\n[4] Ordenar por Año \n[5] Volver al menú principal\n"))

                #Opción 2.1: Mostrar la lista de juegos:
                if opcionReportes == 1:
                    print("---------Lista de juegos----------\n")
                    for i in dicJuegos.values():
                        dict7 = i
                        for key,value in dict7.items():
                            print(f"{key}: {value}", end = ", ")
                        print("\n")
                    print("----------------------------------")
                    continue

                #Opción 2.2: Ordenar juegos por Rating:
                elif opcionReportes == 2:
                    ordenRating = dict(sorted(dicJuegos.items(), key = lambda x: x[1]["Rating"])) #Uso de función lambda para la key de sorted()
                    print("---------Juegos por Rating---------\n")                                # para acceder al subdiccionario y a un valor en particular
                    for i in ordenRating.values():
                        dict8 = i
                        for key,value in dict8.items():
                            print(f"{key}: {value}", end = ", ")
                        print("\n")
                    print("-----------------------------------")
                    continue

                #Opción 2.3: Ordenar juegos por Precio:
                elif opcionReportes == 3:
                    ordenPrecio = dict(sorted(dicJuegos.items(), key = lambda x: x[1]["Precio"]))  
                    print("---------Juegos por Precio---------\n")
                    for i in ordenPrecio.values():
                        dict9 = i
                        for key,value in dict9.items():
                            print(f"{key}: {value}", end = ", ")
                        print("\n")
                    print("-----------------------------------")
                    continue

                #Opción 2.4: Ordenar juegos por Año:
                elif opcionReportes == 4:
                    ordenAño = dict(sorted(dicJuegos.items(), key = lambda x: x[1]["Año"])) 
                    print("----------Juegos por Año----------\n")
                    for i in ordenAño.values():
                        dict10 = i
                        for key,value in dict10.items():
                            print(f"{key}: {value}", end = ", ")
                        print("\n")
                    print("----------------------------------")
                    continue

                #Opción 2.5: Volver al menú principal:
                elif opcionReportes == 5:
                    break

                #Opción no válida:
                else: 
                    print("\nDebe ingresar una opción válida\n")
                    continue

        
        #Opción de exit del programa:
        elif opcionPpal == 3:       
            print("-----------------------------------\n------Gracias por la consulta------\n--------------Salida---------------\n-----------------------------------")
            break
        
        #Opción principal inválida:
        else: 
            print("\nDebe ingresar una opción válida\n")
            continue

    except ValueError:
           print("\nDebe ingresar una opción válida\n")
           continue          
        

        


