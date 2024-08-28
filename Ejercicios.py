import math

#Crea un código que imprima en pantalla la expresión “Mi Primer Código En Python.” 

print ("Mi primer Código en Python\n")

#Crea un código que imprima en pantalla la siguiente expresión. 
# A B C
# D E F
# G H I

print (" A B C \n D E F \n G H I\n")

#Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:
#¿Qué estás estudiando?
#El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print).

pregunta = input(" ¿Qué estás estudiando?: ")
print (f" Estudio: {pregunta}")

#Crea un código que le permita ingresar una respuesta al usuario, haciéndole la siguiente pregunta:
#¿En qué país vives?
#El código debe poder imprimir en pantalla lo ingresado por el usuario (utilizando print).

pregunta = input(" ¿En qué país vives?: ")
print (f" Paísli: {pregunta}")


#Declara dos variables, llamadas nombre y edad.
#Asigna a la variable nombre el valor "David Bowman", y a la edad, el valor 51.

nombre = "David Bowman"
edad = 51

#Crea tres variables:
#nombre
#apellido
#nombrecompleto
#A nombre, asígnale el valor "Julia", y en apellido, asigna el valor "Roberts". Finalmente, construye la variable nombrecompleto concatenando 
#las variables (recuerda sumar un espacio intermedio).

nombre1 = "Julia "
apellido = "Roberts"
nombrecompleto = nombre1 + apellido
print(f"Nombre: {nombrecompleto}")

#Declara la variable materia, asígnale el valor "Ingeniería del conocimiento", y muestra en pantalla la frase:
#Estás estudiando “materia”
#Para ello deberás concatenar la primera parte de la frase con el valor que asumirá la variable. Recuerda agregar un espacio antes de concatenar la variable al resto del texto.

materia = "Ingeniería del conocimiento"
print(f"Estás estudiando {materia}")

#Convierte el valor de num1 (num1=35) en un int e imprime el tipo de dato que resulta

num1 = 35
print("El num es de tipo: ",type(num1))

#Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:
#“Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)”
nombre_asociado = "nombre"
numero_asociado = "numero"
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

#Muestra en pantalla el cociente (división al piso) de los siguientes dos números: 874 dividido entre 27.
#Debes mostrar sólo el valor numérico que resulta de esta operación.

div = 874 / 27
print(f"Resultado de la div= {div}")

#Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.

num2 = 10.676767
redondeo_num2 = math.ceil(num2)
print (f"El redondeo de {num2} es: {redondeo_num2}")

#Gestión de inventario con tuplas:
#Consigna: Una tienda tiene un inventario de productos, cada producto tiene un nombre, precio y cantidad disponible. 
#Representa cada producto como una tupla (nombre, precio, cantidad). Escribe una función que reciba una lista de productos (tuplas) y devuelva el producto más caro.
#productos = [ ("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30) ]

def producto_mas_caro(productos):
    # Inicializamos el producto más caro con el primer producto de la lista
    mas_caro = productos[0]
    
    # Recorremos la lista de productos
    for producto in productos:
        # Comparamos el precio del producto actual con el precio del producto más caro
        if producto[1] > mas_caro[1]:
            mas_caro = producto
    
    return mas_caro

# Lista de productos
productos = [("laptop", 1200, 5), ("mouse", 25, 50), ("teclado", 100, 30)]

# Llamamos a la función y mostramos el producto más caro
print(producto_mas_caro(productos))


#Registro de estudiantes con diccionarios:
#Consigna: Una escuela lleva un registro de estudiantes donde la clave es el número de matrícula y el valor es un diccionario con nombre, edad y calificaciones en distintas materias. 
#Escribe una función que reciba el registro de estudiantes y devuelva el promedio de calificaciones de un estudiante dado su número de matrícula.
#estudiantes = {
#    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
#    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}}

def promedio_calificaciones(registro, matricula):
    # Verificamos si el número de matrícula está en el registro
    if matricula in registro:
        # Obtenemos las calificaciones del estudiante
        calificaciones = registro[matricula]["calificaciones"]
        
        # Calculamos el promedio de las calificaciones
        promedio = sum(calificaciones.values()) / len(calificaciones)
        
        return promedio
    else:
        return "Número de matrícula no encontrado"

# Registro de estudiantes
estudiantes = {
    101: {"nombre": "Ana", "edad": 16, "calificaciones": {"matemáticas": 85, "ciencias": 90}},
    102: {"nombre": "Luis", "edad": 17, "calificaciones": {"matemáticas": 78, "ciencias": 88}}
}

# Ejemplo de uso
matricula = 101
print(f"El promedio de calificaciones del estudiante con matrícula {matricula} es:", promedio_calificaciones(estudiantes, matricula))



#Análisis de datos meteorológicos con arrays:
#Consigna: Un meteorólogo registra las temperaturas diarias durante un mes y las almacena en un array. Escribe una función que reciba este array y devuelva la temperatura media del mes, la máxima y la mínima.
#temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

def analizar_temperaturas(temperaturas):
    # Calcular la temperatura media
    temperatura_media = sum(temperaturas) / len(temperaturas)
    
    # Encontrar la temperatura máxima
    temperatura_maxima = max(temperaturas)
    
    # Encontrar la temperatura mínima
    temperatura_minima = min(temperaturas)
    
    return temperatura_media, temperatura_maxima, temperatura_minima

# Array de temperaturas
temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

# Llamar a la función y mostrar los resultados
media, maxima, minima = analizar_temperaturas(temperaturas)
print(f"Temperatura media del mes: {media:.2f}")
print(f"Temperatura máxima del mes: {maxima:.2f}")
print(f"Temperatura mínima del mes: {minima:.2f}")




#Manejo de parámetros variables con *args:
#Consigna: Escribe una función que reciba un número variable de notas de estudiantes y devuelva la nota promedio. Utiliza *args para recibir las notas.
#calcular_promedio(85, 90, 78, 92)

def calcular_promedio(*args):
    # Verificar si se han pasado notas
    if len(args) == 0:
        return "No se han proporcionado notas."
    
    # Calcular el promedio de las notas
    promedio = sum(args) / len(args)
    
    return promedio

# Ejemplo de uso
notas = (85, 90, 78, 92)
promedio = calcular_promedio(*notas)
print(f"El promedio de las notas es: {promedio:.2f}")

#2.16.	Creación de un perfil de usuario con **kwargs:
#Consigna: Escribe una función que reciba datos de un usuario como nombre, edad, correo electrónico, y cualquier otro dato adicional usando **kwargs. 
#La función debe devolver un diccionario con toda la información del usuario.
#crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza")

def crear_perfil(**kwargs):
    # Retornar un diccionario con todos los datos proporcionados
    return kwargs

# Ejemplo de uso
perfil = crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza")

# Imprimir el perfil del usuario
print(perfil)

#2.17.	Administración de empleados con tuplas y diccionarios:
#Consigna: Una empresa quiere administrar la información de sus empleados, donde cada empleado se representa como una tupla (nombre, edad, salario). 
#Escribe una función que reciba un diccionario donde la clave es el ID del empleado y el valor es la tupla con su información. 
#La función debe devolver un diccionario con los empleados que ganan más de un salario dado.
empleados = {
    1: ("Ana", 30, 3000),
    2: ("Luis", 25, 2500),
    3: ("María", 35, 4000)
}
def empleados_con_sueldo_mayor(empleados, salario_umbral):
    # Crear un diccionario para almacenar los empleados que ganan más que el salario umbral
    empleados_mayores = {}
    
    # Recorrer el diccionario de empleados
    for id_empleado, info in empleados.items():
        nombre, edad, salario = info
        # Verificar si el salario del empleado es mayor que el umbral
        if salario > salario_umbral:
            empleados_mayores[id_empleado] = info
    
    return empleados_mayores

# Ejemplo de uso
salario_umbral = 2800
resultado = empleados_con_sueldo_mayor(empleados, salario_umbral)

# Imprimir el resultado
print(resultado)

#2.18.	Procesamiento de ventas con arrays:
#Consigna: Una tienda quiere procesar sus ventas diarias almacenadas en un array. 
#Escribe una función que reciba el array de ventas diarias y devuelva el total de ventas y el promedio de ventas por día.
ventas_diarias = [200, 450, 300, 400, 350, 500, 600]
def procesar_ventas(ventas_diarias):
    # Calcular el total de ventas
    total_ventas = sum(ventas_diarias)
    
    # Calcular el promedio de ventas por día
    if len(ventas_diarias) > 0:
        promedio_ventas = total_ventas / len(ventas_diarias)
    else:
        promedio_ventas = 0
    
    return total_ventas, promedio_ventas

# Llamar a la función y mostrar los resultados
total, promedio = procesar_ventas(ventas_diarias)
print(f"Total de ventas: {total}")
print(f"Promedio de ventas por día: {promedio:.2f}")

#2.19.	Análisis de resultados deportivos con diccionarios:
#Consigna: Un club deportivo registra los resultados de sus partidos en un diccionario donde la clave es el nombre del equipo rival y el valor es una tupla con los goles anotados y recibidos. 
#Escribe una función que calcule el total de goles anotados y recibidos en la temporada.

resultados = {
    "Equipo A": (3, 2),
    "Equipo B": (1, 1),
    "Equipo C": (4, 0)
}

def calcular_totales(resultados):
    # Inicializar los contadores de goles anotados y recibidos
    total_goles_anotados = 0
    total_goles_recibidos = 0
    
    # Recorrer el diccionario de resultados
    for goles_anotados, goles_recibidos in resultados.values():
        total_goles_anotados += goles_anotados
        total_goles_recibidos += goles_recibidos
    
    return total_goles_anotados, total_goles_recibidos

# Llamar a la función y mostrar los resultados
total_anotados, total_recibidos = calcular_totales(resultados)
print(f"Total de goles anotados: {total_anotados}")
print(f"Total de goles recibidos: {total_recibidos}")

#2.20.	Configuración de una aplicación con **kwargs:
#Consigna: Escribe una función que reciba configuraciones opcionales para una aplicación como modo oscuro, idioma, notificaciones, etc., usando **kwargs.
#La función debe devolver un diccionario con las configuraciones aplicadas.

def configurar_app(**kwargs):
    # Retornar un diccionario con las configuraciones aplicadas
    return kwargs

# Ejemplo de uso
configuracion = configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)

# Imprimir la configuración aplicada
print(configuracion)



#2.21.	Ordenamiento de datos con tuplas:
#Consigna: Escribe una función que reciba una lista de tuplas donde cada tupla contiene un nombre y una puntuación. 
#La función debe devolver la lista ordenada por puntuación de mayor a menor.

puntuaciones = [("Ana", 85), ("Luis", 90), ("María", 78)]

def ordenar_por_puntuacion(puntuaciones):
    # Ordenar la lista de tuplas por la puntuación en orden descendente
    return sorted(puntuaciones, key=lambda x: x[1], reverse=True)

# Llamar a la función y mostrar el resultado
puntuaciones_ordenadas = ordenar_por_puntuacion(puntuaciones)
print(puntuaciones_ordenadas)

#2.22.	Planificación de viajes con tuplas y diccionarios:
#Consigna: Una agencia de viajes tiene diferentes paquetes turísticos, cada uno representado como una tupla (destino, precio, duración en días). 
#Escribe una función que reciba una lista de estos paquetes y devuelva un diccionario con los destinos como claves y el precio total (precio por día * duración) como valor.

paquetes = [
    ("Paris", 200, 5),
    ("Roma", 150, 4),
    ("Londres", 180, 3)
]

def calcular_precio_total(paquetes):
    # Crear un diccionario para almacenar el precio total por destino
    precios_totales = {}
    
    # Recorrer la lista de paquetes
    for destino, precio_por_dia, duracion in paquetes:
        # Calcular el precio total para el paquete
        precio_total = precio_por_dia * duracion
        # Añadir el destino y el precio total al diccionario
        precios_totales[destino] = precio_total
    
    return precios_totales

# Llamar a la función y mostrar el resultado
resultados = calcular_precio_total(paquetes)
print(resultados)


#2.23.	Gestión de inventario con arrays:
#Consigna: Una tienda maneja su inventario de productos en un array donde cada índice representa un producto específico y su valor es la cantidad disponible.
#Escribe una función que reciba el array de inventario y un número de productos vendidos (otro array) y devuelva el inventario actualizado.

inventario = [50, 30, 20, 10]
ventas = [5, 10, 5, 2]

def actualizar_inventario(inventario, ventas):
    # Verificar que las listas de inventario y ventas tengan el mismo tamaño
    if len(inventario) != len(ventas):
        raise ValueError("El tamaño de las listas de inventario y ventas debe ser el mismo.")
    
    # Actualizar el inventario restando las ventas
    inventario_actualizado = [inventario[i] - ventas[i] for i in range(len(inventario))]
    
    return inventario_actualizado


# Llamar a la función y mostrar el inventario actualizado
inventario_actualizado = actualizar_inventario(inventario, ventas)
print(inventario_actualizado)

#2.24.	Organización de eventos con *args:
#Consigna: Escribe una función que reciba un número variable de nombres de eventos y los imprima en un formato de lista numerada. Utiliza *args para recibir los nombres de los eventos.

def organizar_eventos(*args):
    # Imprimir los eventos en un formato de lista numerada
    for i, evento in enumerate(args, start=1):
        print(f"{i}. {evento}")

# Ejemplo de uso
organizar_eventos("Concierto", "Exposición de arte", "Conferencia")

#2.25.	Análisis financiero con **kwargs:
#Consigna: Escribe una función que reciba diferentes tipos de ingresos y gastos como **kwargs y calcule el balance final. 
#La función debe manejar ingresos como positivos y gastos como negativos.

def analizar_finanzas(**kwargs):
    # Calcular el balance sumando todos los valores en kwargs
    balance = sum(kwargs.values())
    return balance

# Ejemplo de uso
balance_final = analizar_finanzas(sueldo=2000, renta=-800, transporte=-150, comida=-300, freelance=500)
print(f"Balance final: {balance_final}")


#2.26.	Registro de empleados con tuplas y **kwargs:
#Consigna: Escribe una función que reciba el nombre, edad, y salario de un empleado como parámetros obligatorios, y otros datos como dirección, número de teléfono, etc., como **kwargs. 
#La función debe devolver un diccionario con toda la información del empleado.


def registro_empleado(nombre, edad, salario, **kwargs):
    # Crear el diccionario con la información obligatoria
    empleado = {
        "Nombre": nombre,
        "Edad": edad,
        "Salario": salario
    }
    
    # Añadir los datos opcionales al diccionario
    empleado.update(kwargs)
    
    return empleado

# Ejemplo de uso
empleado_info = registro_empleado(
    "Ana", 
    30, 
    3000, 
    direccion="Calle Falsa 123", 
    telefono="123456789"
)

# Mostrar la información del empleado
print(empleado_info)


#2.27.	Estadísticas de ventas con arrays:
#Consigna: Escribe una función que reciba un array con las ventas de cada mes y devuelva un diccionario con el total de ventas, el promedio mensual, y el mes con mayores ventas.

ventas_mensuales = [2000, 2500, 3000, 2800, 3500, 4000, 4200, 3800, 3600, 3900, 4100, 4500]

def analizar_ventas(ventas_mensuales):
    # Calcular el total de ventas
    total_ventas = sum(ventas_mensuales)
    
    # Calcular el promedio mensual
    promedio_mensual = total_ventas / len(ventas_mensuales)
    
    # Encontrar el mes con mayores ventas (índice del máximo valor)
    mes_max_ventas = ventas_mensuales.index(max(ventas_mensuales)) + 1  # +1 para que sea 1-indexado
    
    # Crear el diccionario con las estadísticas
    estadisticas = {
        "Total de ventas": total_ventas,
        "Promedio mensual": promedio_mensual,
        "Mes con mayores ventas": mes_max_ventas
    }
    
    return estadisticas


# Llamar a la función y mostrar el resultado
estadisticas_ventas = analizar_ventas(ventas_mensuales)
print(estadisticas_ventas)

#2.28.	Organización de una biblioteca con diccionarios:
#Consigna: Una biblioteca registra sus libros en un diccionario donde la clave es el título del libro y el valor es otro diccionario con la información del autor, año de publicación, y género.
#Escribe una función que reciba este diccionario y devuelva una lista de todos los libros publicados después del año 2000.

biblioteca = {
    "El señor de los anillos": {"autor": "J.R.R. Tolkien", "año": 1954, "género": "Fantasía"},
    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "género": "Realismo mágico"},
    "El código Da Vinci": {"autor": "Dan Brown", "año": 2003, "género": "Suspenso"}
}

def libros_post_2000(biblioteca):
    # Crear una lista para almacenar los títulos de los libros publicados después del año 2000
    libros_recientes = []
    
    # Recorrer el diccionario de la biblioteca
    for titulo, info in biblioteca.items():
        # Verificar si el año de publicación es mayor a 2000
        if info["año"] > 2000:
            libros_recientes.append(titulo)
    
    return libros_recientes


# Llamar a la función y mostrar el resultado
libros_recientes = libros_post_2000(biblioteca)
print(libros_recientes)

#2.29.	Registro de notas con tuplas y arrays:
#Consigna: Escribe una función que reciba una lista de tuplas donde cada tupla contiene el nombre de un estudiante y sus calificaciones en un array.
#La función debe devolver un diccionario con el nombre del estudiante como clave y su promedio de calificaciones como valor.

notas_estudiantes = [
    ("Ana", [85, 90, 78]),
    ("Luis", [88, 92, 80]),
    ("María", [75, 85, 70])
]

def calcular_promedios(notas_estudiantes):
    # Crear un diccionario para almacenar los promedios de calificaciones
    promedios = {}
    
    # Recorrer la lista de tuplas
    for nombre, calificaciones in notas_estudiantes:
        # Calcular el promedio de las calificaciones
        promedio = sum(calificaciones) / len(calificaciones)
        # Añadir el promedio al diccionario
        promedios[nombre] = promedio
    
    return promedios


# Llamar a la función y mostrar el resultado
promedios_estudiantes = calcular_promedios(notas_estudiantes)
print(promedios_estudiantes)

#2.30.	Configuración de perfiles de usuario con **kwargs y arrays:
#Consigna: Escribe una función que reciba una lista de usuarios y sus preferencias de configuración como **kwargs. 
#La función debe devolver un diccionario donde la clave es el nombre del usuario y el valor es un array con las configuraciones aplicadas.

def configurar_perfiles(usuarios, **kwargs):
    # Crear un diccionario para almacenar las configuraciones de cada usuario
    perfiles = {}
    
    # Convertir las configuraciones de kwargs en una lista
    configuraciones = list(kwargs.values())
    
    # Asignar las configuraciones a cada usuario
    for usuario in usuarios:
        perfiles[usuario] = configuraciones
    
    return perfiles

# Lista de usuarios
usuarios = ["Ana", "Luis", "María"]

# Llamar a la función y mostrar el resultado
perfiles_configurados = configurar_perfiles(
    usuarios, 
    idioma="es", 
    modo_oscuro=True, 
    notificaciones=False
)
print(perfiles_configurados)


#2.31.	Gestión de una red social con **kwargs y arrays:
#Consigna: Escribe una función que administre publicaciones de una red social. La función debe recibir el nombre del usuario, el texto de la publicación y un número variable de etiquetas usando **kwargs y arrays. 
#Además, debe manejar opciones adicionales como visibilidad pública o privada. La función debe devolver un diccionario con todos los detalles de la publicación.

def publicar(nombre_usuario, texto_publicacion, etiquetas=None, **kwargs):
    # Crear un diccionario para almacenar los detalles de la publicación
    publicacion = {
        "nombre_usuario": nombre_usuario,
        "texto_publicacion": texto_publicacion,
        "etiquetas": etiquetas if etiquetas is not None else []
    }
    
    # Añadir las opciones adicionales desde kwargs al diccionario
    for clave, valor in kwargs.items():
        publicacion[clave] = valor
    
    return publicacion

# Ejemplo de uso
resultado = publicar(
    "Juan", 
    "Mi primer post!", 
    etiquetas=["#hola", "#primerPost"], 
    visibilidad="publica", 
    likes=100
)

print(resultado)


#2.32.	Simulación de ventas con tuplas, arrays, y *args:
#Consigna: Una empresa quiere simular las ventas de diferentes productos. Escribe una función que reciba un número variable de ventas (tuplas) donde cada tupla contiene el producto, la cantidad vendida, y el precio por unidad. 
#La función debe devolver el total de ingresos generados por las ventas.



def simular_ventas(*ventas):
    total_ingresos = 0
    
    # Recorrer cada venta en *ventas
    for venta in ventas:
        producto, cantidad, precio = venta
        # Calcular el ingreso de esta venta y agregarlo al total
        total_ingresos += cantidad * precio
    
    return total_ingresos

total = simular_ventas(("Producto A", 10, 15.0), ("Producto B", 5, 25.0), ("Producto C", 3, 50.0))

print(total)

#2.33.	Sistema de reservas con tuplas y diccionarios:
#Consigna: Un hotel maneja sus reservas utilizando un diccionario donde la clave es la fecha y el valor es una lista de tuplas, cada tupla contiene el nombre del huésped, la habitación asignada y el precio. 
#Escribe una función que permita hacer una nueva reserva verificando primero si la habitación está disponible en la fecha seleccionada.

reservas = {
    "2024-08-15": [("Juan", 101, 150), ("Ana", 102, 180)],
    "2024-08-16": [("Luis", 101, 150)]
}

def hacer_reserva(reservas, fecha, nombre_huesped, habitacion, precio):
    # Verificar si la fecha ya existe en el diccionario de reservas
    if fecha not in reservas:
        # Si la fecha no existe, crear una nueva entrada con una lista vacía
        reservas[fecha] = []
    
    # Verificar si la habitación está disponible en la fecha seleccionada
    for reserva in reservas[fecha]:
        _, habitacion_asignada, _ = reserva
        if habitacion_asignada == habitacion:
            print(f"La habitación {habitacion} ya está ocupada en la fecha {fecha}.")
            return reservas
    
    # Si la habitación está disponible, agregar la nueva reserva
    reservas[fecha].append((nombre_huesped, habitacion, precio))
    print(f"Reserva realizada para {nombre_huesped} en la habitación {habitacion} en la fecha {fecha}.")
    
    return reservas

# Ejemplo de uso
reservas_actualizadas = hacer_reserva(reservas, "2024-08-15", "Marta", 103, 200)
reservas_actualizadas = hacer_reserva(reservas, "2024-08-15", "Carlos", 101, 160)  # Habitación ocupada
reservas_actualizadas = hacer_reserva(reservas, "2024-08-17", "Laura", 101, 150)  # Nueva fecha

# Mostrar el diccionario actualizado
print(reservas_actualizadas)


#2.34.Análisis de resultados de encuestas con diccionarios y arrays:
#Consigna: Una empresa realiza encuestas de satisfacción y registra las respuestas en un diccionario donde la clave es la pregunta y el valor es un array con las respuestas recibidas. 
#Escribe una función que calcule la frecuencia de cada respuesta para cada pregunta y devuelva un diccionario con estos resultados.

encuestas = {
    "¿Cómo califica el servicio?": [5, 4, 5, 3, 5, 4],
    "¿Recomendaría nuestro producto?": [1, 1, 0, 1, 1, 0]
}

def analizar_encuestas(encuestas):
    resultado = {}
    
    # Recorrer cada pregunta en el diccionario de encuestas
    for pregunta, respuestas in encuestas.items():
        # Crear un diccionario para almacenar las frecuencias de cada respuesta
        frecuencias = {}
        
        # Contar las frecuencias de cada respuesta
        for respuesta in respuestas:
            if respuesta in frecuencias:
                frecuencias[respuesta] += 1
            else:
                frecuencias[respuesta] = 1
        
        # Añadir el diccionario de frecuencias al resultado para la pregunta actual
        resultado[pregunta] = frecuencias
    
    return resultado

# Ejemplo de uso
resultado_analisis = analizar_encuestas(encuestas)

# Mostrar el resultado
print(resultado_analisis)

#2.35.	Optimización de rutas con arrays y tuplas:
#Consigna: Una empresa de logística necesita optimizar sus rutas de entrega. Cada ruta se representa como una tupla (origen, destino, distancia). 
#Escribe una función que reciba una lista de rutas y un array con las distancias máximas permitidas para cada ruta. La función debe devolver las rutas que cumplen con las restricciones.
rutas = [("Madrid", "Barcelona", 620), ("Madrid", "Valencia", 350), ("Barcelona", "Valencia", 350)]
distancias_max = [600, 400, 500]

def filtrar_rutas(rutas, distancias_max):
    rutas_validas = []
    
    # Asegurarse de que la lista de rutas y la lista de distancias máximas tengan la misma longitud
    if len(rutas) != len(distancias_max):
        raise ValueError("La longitud de la lista de rutas debe ser igual a la longitud de la lista de distancias máximas")
    
    # Recorrer la lista de rutas y distancias máximas
    for ruta, distancia_max in zip(rutas, distancias_max):
        origen, destino, distancia = ruta
        
        # Comparar la distancia de la ruta con la distancia máxima permitida
        if distancia <= distancia_max:
            rutas_validas.append(ruta)
    
    return rutas_validas

# Ejemplo de uso
rutas_filtradas = filtrar_rutas(rutas, distancias_max)

# Mostrar el resultado
print(rutas_filtradas)

#2.36.Gestión de inventarios en múltiples tiendas con diccionarios y **kwargs:
#Consigna:Escribe una función que gestione el inventario de una cadena de tiendas. La función debe recibir el nombre de la tienda, el producto y la cantidad a actualizar usando **kwargs. 
#Debe manejar un diccionario donde la clave es el nombre de la tienda y el valor es otro diccionario con los productos y sus cantidades. La función debe actualizar el inventario y devolver el estado actual.

inventario = {

    "Tienda A": {"producto_1": 50, "producto_2": 30},
    "Tienda B": {"producto_1": 20, "producto_2": 40}
}
actualizar_inventario(tienda="Tienda A", producto_1=10, producto_2=-5)


#2.37.	Análisis de tendencias en redes sociales con arrays y tuplas:
#Consigna: Una empresa de marketing digital desea analizar las tendencias de hashtags en las redes sociales. 
#Escribe una función que reciba un array de hashtags y una lista de tuplas donde cada tupla contiene un hashtag y su frecuencia de uso.
#La función debe devolver los hashtags que han sido mencionados más de una cierta cantidad de veces.
hashtags = ["#verano", "#moda", "#viajes", "#verano", "#moda", "#tecnologia"] 
tendencias = [("#verano", 120), ("#moda", 80), ("#tecnologia", 150)]

def analizar_tendencias(hashtags, tendencias, frecuencia_minima):
    # Contar las menciones de cada hashtag en el array de hashtags
    conteo_hashtags = {}
    
    for hashtag in hashtags:
        if hashtag in conteo_hashtags:
            conteo_hashtags[hashtag] += 1
        else:
            conteo_hashtags[hashtag] = 1
    
    # Crear un diccionario para las frecuencias de tendencias
    tendencias_dict = dict(tendencias)
    
    # Filtrar los hashtags que superan la frecuencia mínima
    hashtags_filtrados = [hashtag for hashtag, conteo in conteo_hashtags.items()
                          if conteo >= frecuencia_minima and hashtag in tendencias_dict and tendencias_dict[hashtag] >= frecuencia_minima]
    
    return hashtags_filtrados

# Especificar la frecuencia mínima
frecuencia_minima = 2

# Obtener los hashtags que cumplen con la frecuencia mínima
resultados = analizar_tendencias(hashtags, tendencias, frecuencia_minima)

# Mostrar el resultado
print(resultados)

#2.38.	Administración de suscripciones con diccionarios, arrays, y **kwargs:
#Consigna: Escribe una función que gestione las suscripciones a un servicio en línea. La función debe recibir el nombre del usuario, el tipo de suscripción (mensual, anual), y cualquier otra opción adicional usando **kwargs. 
#La función debe actualizar un diccionario que almacene el historial de suscripciones de los usuarios y devolver el estado actualizado.

suscripciones = {
    "Jose": ["mensual", "anual"],
    "Ana": ["mensual"]
}

def actualizar_suscripcion(suscripciones, **kwargs):
    # Extraer el nombre del usuario y el tipo de suscripción del diccionario kwargs
    usuario = kwargs.pop('usuario', None)
    suscripcion = kwargs.pop('suscripcion', None)
    
    # Verificar si el usuario ya tiene suscripciones
    if usuario not in suscripciones:
        suscripciones[usuario] = []
    
    # Actualizar el historial de suscripciones
    if suscripcion:
        suscripciones[usuario].append(suscripcion)
    
    # Aquí puedes manejar otras opciones adicionales, como auto-renovación
    opciones_adicionales = kwargs
    if opciones_adicionales:
        print(f"Opciones adicionales para {usuario}: {opciones_adicionales}")
    
    return suscripciones

# Actualizar la suscripción
suscripciones_actualizadas = actualizar_suscripcion(suscripciones, usuario="Luis", suscripcion="mensual", auto_renovacion=True)

# Mostrar el estado actualizado de las suscripciones
print(suscripciones_actualizadas)


#2.39.	Simulación de mercado bursátil con arrays y tuplas:
#Consigna: Escribe una función que simule el comportamiento de acciones en un mercado bursátil. 
#La función debe recibir un array con los precios diarios de una acción y una lista de tuplas donde cada tupla contiene un día y un precio de compra o venta. 
#La función debe devolver el beneficio o pérdida total si las acciones se hubieran comprado y vendido en los días especificados.

precios_diarios = [100, 105, 102, 110, 108]
operaciones = [("compra", 0), ("venta", 3), ("compra", 2), ("venta", 4)]

def simular_mercado(precios_diarios, operaciones):
    saldo = 0
    acciones = 0
    precio_compra = 0

    for operacion, dia in operaciones:
        precio = precios_diarios[dia]
        if operacion == "compra":
            # Comprar acciones
            precio_compra = precio
            acciones += 1
        elif operacion == "venta":
            # Vender acciones
            if acciones > 0:
                saldo += precio - precio_compra
                acciones -= 1
            else:
                print(f"No hay acciones para vender en el día {dia}")
    
    # Si aún queda alguna acción sin vender, el beneficio o pérdida no se calcula para esas acciones.
    if acciones > 0:
        print(f"Aún quedan {acciones} acciones sin vender.")

    return saldo


# Ejecutar la simulación
beneficio_o_perdida = simular_mercado(precios_diarios, operaciones)

# Mostrar el resultado
print(f"Beneficio o pérdida total: {beneficio_o_perdida}")


#2.40.	Análisis de rendimiento académico con diccionarios y arrays:
#Consigna: Una universidad lleva un registro de las calificaciones de los estudiantes en diferentes materias. 
#Cada estudiante tiene un ID único y su información se almacena en un diccionario donde la clave es el ID y el valor es otro diccionario con las materias y sus respectivas calificaciones (arrays). 
#Escribe una función que reciba este diccionario y devuelva un ranking de estudiantes basado en su promedio general.

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def ranking_estudiantes(estudiantes):
    promedios_estudiantes = {}

    for id_estudiante, materias in estudiantes.items():
        total_promedio = 0
        total_materias = 0
        
        for notas in materias.values():
            total_promedio += calcular_promedio(notas)
            total_materias += 1
        
        promedio_general = total_promedio / total_materias
        promedios_estudiantes[id_estudiante] = promedio_general

    # Ordenar estudiantes por promedio general (de mayor a menor)
    ranking = sorted(promedios_estudiantes.items(), key=lambda x: x[1], reverse=True)
    
    return ranking

# Ejemplo de uso
estudiantes = {
    101: {"matemáticas": [85, 90, 78], "ciencias": [88, 85, 80]},
    102: {"matemáticas": [92, 88, 84], "ciencias": [75, 80, 85]},
    103: {"matemáticas": [78, 85, 88], "ciencias": [90, 95, 92]}
}

ranking = ranking_estudiantes(estudiantes)
print(ranking)
