"""
Agenda de peliculas.
Módulo de cálculos.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritmeticas.
* Instrucciones basicas y consola.
* Dividir y conquistar: funciones y paso de parametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.


NOTA IMPORTANTE PARA TENER EN CUENTA EN TODAS LAS FUNCIONES DE ESTE MODULO:
        Los diccionarios de pelicula tienen las siguientes parejas de clave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que día de la semana se planea ver la película
"""


# ---------------------------------------------------------------------------
# Funciones auxiliares (dividir y conquistar)
# ---------------------------------------------------------------------------

def _hora_a_minutos(hora: int) -> int:
    """Convierte una hora en formato HHMM (por ejemplo 1830) a minutos
       transcurridos desde la medianoche (1830 -> 1110).
    """
    return (hora // 100) * 60 + hora % 100


def _tiene_genero(peli: dict, genero_buscado: str) -> bool:
    """Indica si el texto de generos de la pelicula contiene el genero buscado
       (sin importar mayusculas o minusculas).
    """
    return genero_buscado.lower() in peli["genero"].lower()


def _es_entre_semana(dia: str) -> bool:
    """Indica si el dia es de lunes a viernes (es decir, no es sabado ni domingo)."""
    dia = dia.lower()
    return dia not in ("sabado", "sábado", "domingo")


def _hay_conflicto_con(peli: dict, nueva_hora: int, nuevo_dia: str, otra: dict) -> bool:
    """Indica si programar 'peli' en la nueva hora y dia se superpone con la
       pelicula 'otra'. Una pelicula no entra en conflicto consigo misma.
    """
    if otra is peli:
        return False
    if otra["dia"].lower() != nuevo_dia.lower():
        return False
    inicio_nueva = _hora_a_minutos(nueva_hora)
    fin_nueva = inicio_nueva + peli["duracion"]
    inicio_otra = _hora_a_minutos(otra["hora"])
    fin_otra = inicio_otra + otra["duracion"]
    # Dos intervalos se superponen si cada uno empieza antes de que termine el otro
    return inicio_nueva < fin_otra and inicio_otra < fin_nueva


def _agregar_si_estreno(texto: str, peli: dict, anio: int) -> str:
    """Si la pelicula es posterior al anio dado, agrega su nombre al texto
       (separado por coma si ya habia nombres). Retorna el texto resultante.
    """
    if peli["anio"] > anio:
        if texto == "":
            return peli["nombre"]
        return texto + ", " + peli["nombre"]
    return texto


def _viola_control_horario(peli: dict, nueva_hora: int, nuevo_dia: str) -> bool:
    """Indica si la nueva hora y dia incumplen alguna regla del control horario."""
    # Documentales: no a las 10:00 p. m. o más tarde
    if _tiene_genero(peli, "documental") and nueva_hora >= 2200:
        return True
    # Dramas: no los viernes
    if _tiene_genero(peli, "drama") and nuevo_dia.lower() == "viernes":
        return True
    # Entre semana: no desde las 11:00 p. m. ni antes de las 6:00 a. m.
    if _es_entre_semana(nuevo_dia) and (nueva_hora >= 2300 or nueva_hora < 600):
        return True
    return False


# ---------------------------------------------------------------------------
# Funciones del módulo
# ---------------------------------------------------------------------------

def crear_pelicula(nombre: str, genero: str, duracion: int, anio: int, 
                  clasificacion: str, hora: int, dia: str) -> dict:
    """Crea un diccionario que representa una nueva película con toda su información 
       inicializada.
    Parámetros:
        nombre (str): Nombre de la pelicula agendada.
        genero (str): Generos de la pelicula separados por comas.
        duracion (int): Duracion en minutos de la pelicula
        anio (int): Anio de estreno de la pelicula
        clasificacion (str): Clasificacion de restriccion por edad
        hora (int): Hora a la cual se planea ver la pelicula, esta debe estar entre 
                    0 y 2359
        dia (str): Dia de la semana en el cual se planea ver la pelicula.
    Retorna:
        dict: Diccionario con los datos de la pelicula
    """    
    pelicula = {
        "nombre": nombre,
        "genero": genero,
        "duracion": duracion,
        "anio": anio,
        "clasificacion": clasificacion,
        "hora": hora,
        "dia": dia,
    }
    return pelicula

def encontrar_pelicula(nombre_pelicula: str, p1: dict, p2: dict, p3: dict, p4: dict,  p5: dict) -> dict:
    """Encuentra en cual de los 5 diccionarios que se pasan por parametro esta la 
       pelicula cuyo nombre es dado por parametro.
       Si no se encuentra la pelicula se debe retornar None.
    Parametros:
        nombre_pelicula (str): El nombre de la pelicula que se desea encontrar.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: Diccionario de la pelicula cuyo nombre fue dado por parametro. 
        None si no se encuentra una pelicula con ese nombre.
    """
    nombre = nombre_pelicula.strip().lower()
    if p1["nombre"].lower() == nombre:
        return p1
    if p2["nombre"].lower() == nombre:
        return p2
    if p3["nombre"].lower() == nombre:
        return p3
    if p4["nombre"].lower() == nombre:
        return p4
    if p5["nombre"].lower() == nombre:
        return p5
    return None

def encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> dict:
    """Encuentra la pelicula de mayor duracion entre las peliculas recibidas por
       parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        dict: El diccionario de la pelicula de mayor duracion
    """
    # Se parte de la primera y se reemplaza cada vez que aparece una más larga
    mas_larga = p1
    if p2["duracion"] > mas_larga["duracion"]:
        mas_larga = p2
    if p3["duracion"] > mas_larga["duracion"]:
        mas_larga = p3
    if p4["duracion"] > mas_larga["duracion"]:
        mas_larga = p4
    if p5["duracion"] > mas_larga["duracion"]:
        mas_larga = p5
    return mas_larga

def duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> str:
    """Calcula la duracion promedio de las peliculas que entran por parametro. 
       Esto es, la duración total de todas las peliculas dividida sobre el numero de peliculas. 
       Retorna la duracion promedio en una cadena de formato 'HH:MM' ignorando los posibles decimales.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        str: la duracion promedio de las peliculas en formato 'HH:MM'
    """
    total = p1["duracion"] + p2["duracion"] + p3["duracion"] + p4["duracion"] + p5["duracion"]
    promedio = total // 5          # división entera: ignora los decimales
    horas = promedio // 60
    minutos = promedio % 60
    return f"{horas:02d}:{minutos:02d}"

def encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict, anio: int) -> str:
    """Busca entre las peliculas cuales tienen como anio de estreno una fecha estrictamente
       posterior a la recibida por parametro.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
        anio (int): Anio limite para considerar la pelicula como estreno.
    Retorna:
        str: Una cadena con el nombre de la pelicula estrenada posteriormente a la fecha recibida. 
        Si hay mas de una pelicula, entonces se retornan los nombres de todas las peliculas 
        encontradas separadas por comas. Si ninguna pelicula coincide, retorna "Ninguna".
    """
    resultado = ""
    resultado = _agregar_si_estreno(resultado, p1, anio)
    resultado = _agregar_si_estreno(resultado, p2, anio)
    resultado = _agregar_si_estreno(resultado, p3, anio)
    resultado = _agregar_si_estreno(resultado, p4, anio)
    resultado = _agregar_si_estreno(resultado, p5, anio)
    if resultado == "":
        return "Ninguna"
    return resultado

def cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> int:
    """ Indica cuantas peliculas de clasificación '18+' hay entre los diccionarios recibidos.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
       
     int: Numero de peliculas con clasificacion 18+.
     """
    
    contador = 0

    if p1["clasificacion"] == "18+":
        contador += 1

    if p2["clasificacion"] == "18+":
        contador += 1

    if p3["clasificacion"] == "18+":
        contador += 1

    if p4["clasificacion"] == "18+":
        contador += 1

    if p5["clasificacion"] == "18+":
        contador += 1

    return contador


def reagendar_pelicula(peli:dict, nueva_hora: int, nuevo_dia: str, 
                       control_horario: bool, p1: dict, p2: dict, p3: dict, p4: dict, p5: dict)->bool: 
    """Verifica si es posible reagendar la pelicula que entra por parametro. Para esto verifica
       si la nueva hora y el nuevo dia no entran en conflicto con ninguna otra pelicula, 
       y en caso de que el usuario haya pedido control horario verifica que se cumplan 
       las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula a reagendar
        nueva_hora (int): Nueva hora a la cual se quiere ver la pelicula
        nuevo_dia (str): Nuevo dia en el cual se quiere ver la pelicula
        control_horario (bool): Representa si el usuario quiere o no controlar
                                el horario de las peliculas.
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorna:
        bool: True en caso de que se haya podido reagendar la pelicula, False de lo contrario.
    """
    # 1. No debe haber superposición con ninguna otra película
    hay_conflicto = (_hay_conflicto_con(peli, nueva_hora, nuevo_dia, p1)
                     or _hay_conflicto_con(peli, nueva_hora, nuevo_dia, p2)
                     or _hay_conflicto_con(peli, nueva_hora, nuevo_dia, p3)
                     or _hay_conflicto_con(peli, nueva_hora, nuevo_dia, p4)
                     or _hay_conflicto_con(peli, nueva_hora, nuevo_dia, p5))
    if hay_conflicto:
        return False

    # 2. Si el usuario pidió control horario, se validan las restricciones
    if control_horario and _viola_control_horario(peli, nueva_hora, nuevo_dia):
        return False

    # 3. Todo en orden: se actualiza el diccionario de la película
    peli["hora"] = nueva_hora
    peli["dia"] = nuevo_dia
    return True
    
def decidir_invitar(peli: dict, edad_invitado: int, autorizacion_padres: bool)->bool:
    """Verifica si es posible invitar a la persona cuya edad entra por parametro a ver la 
       pelicula que entra igualmente por parametro. 
       Para esto verifica el cumplimiento de las restricciones correspondientes.
    Parametros:
        peli (dict): Pelicula que se desea ver con el invitado
        edad_invitado (int): Edad del invitado con quien se desea ver la pelicula
        autorizacion_padres (bool): Indica si el invitado cuenta con la autorizacion de sus padres 
        para ver la pelicula
    Retorna:
        bool: True en caso de que se pueda invitar a la persona, False de lo contrario.
    """
    # Los mayores de edad pueden ver cualquier película
    if edad_invitado >= 18:
        return True

    # Menores de 15 no pueden ver terror (ni siquiera con autorización)
    if edad_invitado < 15 and _tiene_genero(peli, "terror"):
        return False

    # Invitados de 10 años o menos: solo películas familiares
    if edad_invitado <= 10 and not _tiene_genero(peli, "familiar"):
        return False

    # Edad mínima según la clasificación: 'todos' -> 0, '13+' -> 13, etc.
    clasificacion = peli["clasificacion"].lower()
    if clasificacion == "todos":
        edad_minima = 0
    else:
        edad_minima = int(clasificacion.replace("+", ""))

    # Si la edad no alcanza, se necesita autorización (excepto en documentales)
    if edad_invitado < edad_minima:
        if _tiene_genero(peli, "documental"):
            return True
        return autorizacion_padres

    return True
