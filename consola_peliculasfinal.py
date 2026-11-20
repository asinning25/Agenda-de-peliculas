"""
Agenda de peliculas.
Modulo de interacci0n por consola.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.

"""
import modulo_peliculas as mod

# ---------------------------------------------------------------------------
# Funciones auxiliares para pedir y validar datos al usuario
# ---------------------------------------------------------------------------

def pedir_entero(mensaje: str) -> int:
    """Pide un numero entero positivo al usuario y repite la pregunta hasta que
       el valor ingresado sea valido.
    Parametros:
        mensaje (str): Texto que se le muestra al usuario al pedir el dato.
    Retorna:
        int: El numero entero ingresado por el usuario.
    """
    texto = input(mensaje).strip()
    while not texto.isdigit():
        print("Valor no valido. Debe ingresar un numero entero positivo.")
        texto = input(mensaje).strip()
    return int(texto)

def pedir_hora(mensaje: str) -> int:
    """Pide una hora en formato HHMM (de 0000 a 2359, por ejemplo 1830 para las
       6:30 p. m.) y repite la pregunta hasta que sea valida.
    Parametros:
        mensaje (str): Texto que se le muestra al usuario al pedir el dato.
    Retorna:
        int: La hora ingresada en formato HHMM.
    """
    hora = pedir_entero(mensaje)
    while hora > 2359 or hora % 100 > 59:
        print("Hora no valida. Use el formato HHMM de 24 horas (entre 0 y 2359, minutos hasta 59).")
        hora = pedir_entero(mensaje)
    return hora

def pedir_dia(mensaje: str) -> str:
    """Pide un dia de la semana y repite la pregunta hasta que sea valido.
       Retorna el dia con el mismo formato que usa la agenda (ej. 'Miércoles').
    Parametros:
        mensaje (str): Texto que se le muestra al usuario al pedir el dato.
    Retorna:
        str: El dia de la semana normalizado (primera letra en mayuscula, con tilde).
    """
    dia = input(mensaje).strip().lower()
    while dia not in ("lunes", "martes", "miercoles", "miércoles", "jueves",
                      "viernes", "sabado", "sábado", "domingo"):
        print("Dia no valido. Escriba un dia de la semana (ej. Lunes, Miércoles, Sábado).")
        dia = input(mensaje).strip().lower()
    # Se unifica el formato para que coincida con los dias de la agenda
    if dia == "miercoles":
        dia = "miércoles"
    if dia == "sabado":
        dia = "sábado"
    return dia.capitalize()

def pedir_si_no(mensaje: str) -> bool:
    """Hace una pregunta de si/no y repite hasta obtener una respuesta valida.
    Parametros:
        mensaje (str): Pregunta que se le muestra al usuario.
    Retorna:
        bool: True si la respuesta es 's' (si), False si es 'n' (no).
    """
    respuesta = input(mensaje + " (s/n): ").strip().lower()
    while respuesta != "s" and respuesta != "n":
        print("Respuesta no valida. Escriba 's' para si o 'n' para no.")
        respuesta = input(mensaje + " (s/n): ").strip().lower()
    return respuesta == "s"

# ---------------------------------------------------------------------------
# Funciones del esqueleto
# ---------------------------------------------------------------------------

def mostrar_informacion_pelicula(pelicula: dict)-> None:
    """Imprime los detalles de la pelicula
    Parametros:
        pelicula(dict): La pelicula de la cual se van a mostrar los detalles
        El diccionario que representa una pelicula contiene las siguientes parejas de
        llave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que dia de la semana se planea ver la pelicula
    """       
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]
    
    print("Nombre: " + nombre + " - Anio: " + str(anio) + " - Duracion: " + str(duracion) + "  mins" )
    print("Genero: " + genero + " - Clasificacion: " + clasificacion)
    
    if (hora//100 < 10):
        hora_formato = "0"+ str(hora//100)
    else:
        hora_formato = str(hora//100)
    
    if (hora%100 < 10):
        min_formato = "0"+ str(hora%100)
    else:
        min_formato = str(hora%100)

    print("Dia: " + dia + " Hora: " + hora_formato + ":" + min_formato)

def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de encontrar la pelicula mas larga.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Consultar la pelicula mas larga de la agenda")

    mas_larga = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)

    print("La pelicula mas larga de la agenda es:")
    mostrar_informacion_pelicula(mas_larga)

def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de consultar la duracion promedio de las peliculas.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Consultar la duracion promedio de las peliculas")

    promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)

    print("La duracion promedio de las peliculas es " + promedio + " (HH:MM).")

def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """ Ejecuta la opcion de buscar peliculas de estreno. Esto es: las peliculas que sean 
        mas recientes que un anio dado.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Buscar peliculas de estreno")

    anio = pedir_entero("Ingrese el anio a partir del cual desea buscar estrenos: ")

    estrenos = mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio)

    if estrenos == "Ninguna":
        print("Ninguna pelicula de la agenda se estreno despues de " + str(anio) + ".")
    else:
        print("Peliculas estrenadas despues de " + str(anio) + ": " + estrenos)

def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de consultar cuantas peliculas de la agenda tienen clasificacion
    18+.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Consultar cuantas peliculas tienen clasificacion 18+")

    cantidad = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)

    if cantidad == 1:
        print("Hay 1 pelicula con clasificacion 18+ en la agenda.")
    else:
        print("Hay " + str(cantidad) + " peliculas con clasificacion 18+ en la agenda.")
    
def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de reagendar una pelicula
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Reagendar una pelicula de la agenda")

    nombre = input("Ingrese el nombre de la pelicula que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre,p1,p2,p3,p4,p5)
    
    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        print("Pelicula encontrada:")
        mostrar_informacion_pelicula(pelicula)

        nuevo_dia = pedir_dia("Ingrese el nuevo dia de la semana: ")
        nueva_hora = pedir_hora("Ingrese la nueva hora en formato HHMM (ej. 1830): ")
        control_horario = pedir_si_no("Desea activar el control horario?")

        se_pudo = mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_horario,
                                         p1, p2, p3, p4, p5)

        if se_pudo:
            print("La pelicula fue reagendada con exito. Nueva programacion:")
            mostrar_informacion_pelicula(pelicula)
        else:
            print("No fue posible reagendar la pelicula: el nuevo horario genera un "
                  "conflicto con otra pelicula o incumple las restricciones del control horario.")

def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->None:
    """Ejecuta la opcion de decidir si se puede invitar a alguien a ver una pelicula o no.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Decidir si se puede invitar a alguien a ver una pelicula")

    nom_peli = input("Ingrese el nombre de la pelicula: ")
    pelicula = mod.encontrar_pelicula(nom_peli,p1,p2,p3,p4,p5)

    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        edad = pedir_entero("Ingrese la edad del invitado: ")
        autorizacion = pedir_si_no("El invitado cuenta con autorizacion de sus padres?")

        puede_ver = mod.decidir_invitar(pelicula, edad, autorizacion)

        if puede_ver:
            print("Si se puede invitar a la persona de " + str(edad) + " anios a ver '"
                  + pelicula["nombre"] + "'.")
        else:
            print("No se puede invitar a la persona de " + str(edad) + " anios a ver '"
                  + pelicula["nombre"] + "'.")
  
def iniciar_aplicacion():
    """Inicia la ejecución de la aplicación por consola.
    Esta funcion primero crea las cinco peliculas que se van a manejar en la agenda.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    pelicula1 = mod.crear_pelicula("Shrek",  "Familiar, Comedia", 92, 2001, 'Todos', 1700, "Viernes")
    pelicula2 = mod.crear_pelicula("Get Out",  "Suspenso, Terror", 104, 2017, '18+', 2330, "Sábado")  
    pelicula3 = mod.crear_pelicula("Icarus",  "Documental, Suspenso", 122, 2017, '18+', 800, "Domingo")
    pelicula4 = mod.crear_pelicula("Inception",  "Acción, Drama", 148, 2010, '13+', 1300, "Lunes")
    pelicula5 = mod.crear_pelicula("The Empire Strikes Back",  "Familiar, Ciencia-Ficción", 124, 1980, '7+', 1415, "Miércoles")   
    
    ejecutando = True
    while ejecutando:            
        print("\n\nMi agenda de peliculas para la semana de receso" +"\n"+("-"*50))
        print("Pelicula 1")
        mostrar_informacion_pelicula(pelicula1)
        print("-"*50)
        
        print("Pelicula 2")
        mostrar_informacion_pelicula(pelicula2)
        print("-"*50)
        
        print("Pelicula 3")
        mostrar_informacion_pelicula(pelicula3)
        print("-"*50)
        
        print("Pelicula 4")
        mostrar_informacion_pelicula(pelicula4)
        print("-"*50)
        
        print("Pelicula 5")
        mostrar_informacion_pelicula(pelicula5)
        print("-"*50)
        
        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4:dict, p5:dict) -> bool:
    """Le muestra al usuario las opciones de ejecución disponibles.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente 
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opción para salir 
        de la aplicacion.
    """
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien")    
    print(" 7 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)
    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)        
    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5) 
    elif opcion_elegida == "7":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando


iniciar_aplicacion()
