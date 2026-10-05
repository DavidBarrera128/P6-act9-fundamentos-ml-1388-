# Barrera contreras Luis David NC = 1388
# ==============================================================================
# EJERCICIOS DE PROGRAMACIÓN EN PYTHON - W3SCHOOLS
# Todos los ejercicios organizados por sección con 3 ejemplos cada uno.
# ==============================================================================

# ==============================================================================
# SECCIÓN 1: PYTHON VARIABLES
# Referencia: https://www.w3schools.com/python/python_variables.asp
# ==============================================================================

print("=== SECCIÓN 1: PYTHON VARIABLES ===")

# Ejemplo 1: Creación y asignación básica de variables
# Python determina el tipo de dato automáticamente al asignar el valor.
nombre_estudiante = "Carlos"
edad_estudiante = 20
promedio_calificaciones = 9.5

print("Ejemplo 1:")
print("Nombre:", nombre_estudiante)
print("Edad:", edad_estudiante)
print("Promedio:", promedio_calificaciones)
print()

# Ejemplo 2: Convenciones de nombres de variables
# Demostración de Camel Case, Pascal Case y Snake Case (estándar en Python)
miVariableCamel = "Camel Case"
MiVariablePascal = "Pascal Case"
mi_variable_snake = "Snake Case"

print("Ejemplo 2:")
print("Estilo Camel Case:", miVariableCamel)
print("Estilo Pascal Case:", MiVariablePascal)
print("Estilo Snake Case:", mi_variable_snake)
print()

# Ejemplo 3: Impresión combinada y f-strings
producto = "Lápiz"
precio = 15.5
cantidad = 3

print("Ejemplo 3:")
print("Producto:", producto, "| Cantidad:", cantidad, "| Precio unitario: $", precio)
print(f"Total a pagar por {cantidad} {producto}(s): ${precio * cantidad}")
print("-" * 50)


# ==============================================================================
# SECCIÓN 2: ASSIGN MULTIPLE VALUES
# Referencia: https://www.w3schools.com/python/python_variables_multiple.asp
# ==============================================================================

print("\n=== SECCIÓN 2: ASSIGN MULTIPLE VALUES ===")

# Ejemplo 1: Múltiples valores a múltiples variables en una sola línea
x, y, z = "Manzana", "Banana", "Cereza"

print("Ejemplo 1:")
print("x:", x)
print("y:", y)
print("z:", z)
print()

# Ejemplo 2: Un mismo valor asignado a múltiples variables
a = b = c = "Python 3"

print("Ejemplo 2:")
print("a:", a)
print("b:", b)
print("c:", c)
print()

# Ejemplo 3: Desempaquetar una colección (Unpacking)
frutas = ["Mango", "Uva", "Naranja"]
fruta1, fruta2, fruta3 = frutas

print("Ejemplo 3:")
print("Colección original:", frutas)
print(f"Desempaquetado -> Fruta 1: {fruta1} | Fruta 2: {fruta2} | Fruta 3: {fruta3}")
print("-" * 50)


# ==============================================================================
# SECCIÓN 3: DATA TYPES
# Referencia: https://www.w3schools.com/python/python_datatypes.asp
# ==============================================================================

print("\n=== SECCIÓN 3: DATA TYPES ===")

# Ejemplo 1: Tipos de datos numéricos (int, float, complex)
entero = 42
flotante = 3.1416
complejo = 2 + 3j

print("Ejemplo 1 (Tipos Numéricos):")
print(f"Valor: {entero} -> Tipo: {type(entero)}")
print(f"Valor: {flotante} -> Tipo: {type(flotante)}")
print(f"Valor: {complejo} -> Tipo: {type(complejo)}")
print()

# Ejemplo 2: Colecciones y secuencias (str, list, tuple, dict)
cadena_texto = "Hola VS Code"
lista_colores = ["rojo", "verde", "azul"]
tupla_coordenadas = (10.5, -20.8)
diccionario_usuario = {"nombre": "Ana", "rol": "Admin"}

print("Ejemplo 2 (Colecciones y Secuencias):")
print(f"Texto: {cadena_texto} -> {type(cadena_texto)}")
print(f"Lista: {lista_colores} -> {type(lista_colores)}")
print(f"Tupla: {tupla_coordenadas} -> {type(tupla_coordenadas)}")
print(f"Diccionario: {diccionario_usuario} -> {type(diccionario_usuario)}")
print()

# Ejemplo 3: Booleanos y conversión explícita de tipos (Casting)
es_activo = True
numero_string = "100"
numero_convertido = int(numero_string)

print("Ejemplo 3 (Booleanos y Casting):")
print(f"Booleano: {es_activo} -> Tipo: {type(es_activo)}")
print(f"String '{numero_string}' ({type(numero_string)}) a entero: {numero_convertido} ({type(numero_convertido)})")
print("-" * 50)


# ==============================================================================
# SECCIÓN 4: ARITHMETIC OPERATORS
# Referencia: https://www.w3schools.com/python/python_operators_arithmetic.asp
# ==============================================================================

print("\n=== SECCIÓN 4: ARITHMETIC OPERATORS ===")

# Ejemplo 1: Operaciones aritméticas básicas (+, -, *, /)
num1 = 15
num2 = 4

print("Ejemplo 1 (Suma, Resta, Multiplicación, División):")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
print()

# Ejemplo 2: Operadores avanzados (Módulo %, Exponente **, División entera //)
base = 2
exponente = 5
dividendo = 17
divisor = 5

print("Ejemplo 2 (Módulo, Potencia, División Entera):")
print(f"Módulo ({dividendo} % {divisor}): {dividendo % divisor} (Residuo)")
print(f"Exponente ({base} ** {exponente}): {base ** exponente}")
print(f"División Entera ({dividendo} // {divisor}): {dividendo // divisor}")
print()

# Ejemplo 3: Aplicación práctica (Cálculo financiero con descuento e IVA)
precio_base = 250.0
porcentaje_descuento = 15
impuesto_iva = 0.16

descuento = precio_base * (porcentaje_descuento / 100)
subtotal = precio_base - descuento
total = subtotal * (1 + impuesto_iva)

print("Ejemplo 3 (Cálculo Financiero):")
print(f"Precio Base: ${precio_base}")
print(f"Descuento ({porcentaje_descuento}%): -${descuento}")
print(f"Subtotal: ${subtotal}")
print(f"Total con IVA (16%): ${total:.2f}")
print("-" * 50)


# ==============================================================================
# SECCIÓN 5: COMPARISON OPERATORS
# Referencia: https://www.w3schools.com/python/python_operators_comparison.asp
# ==============================================================================

print("\n=== SECCIÓN 5: COMPARISON OPERATORS ===")

# Ejemplo 1: Igualdad (==) y Desigualdad (!=)
a = 10
b = 20

print("Ejemplo 1 (Igualdad y Desigualdad):")
print(f"¿{a} == {b}? -> {a == b}")
print(f"¿{a} != {b}? -> {a != b}")
print()

# Ejemplo 2: Comparaciones de magnitud (>, <, >=, <=)
calificacion = 85
nota_minima_aprobatoria = 70
nota_excelencia = 90

print("Ejemplo 2 (Comparaciones de Orden):")
print(f"¿Calificación ({calificacion}) >= {nota_minima_aprobatoria}? -> {calificacion >= nota_minima_aprobatoria}")
print(f"¿Calificación ({calificacion}) < {nota_excelencia}? -> {calificacion < nota_excelencia}")
print()

# Ejemplo 3: Comparación entre cadenas de texto
usuario_ingresado = "admin"
usuario_correcto = "ADMIN"

print("Ejemplo 3 (Comparación de Cadenas):")
print(f"¿'{usuario_ingresado}' == '{usuario_correcto}'? -> {usuario_ingresado == usuario_correcto}")
print(f"Comparación ignorando mayúsculas: -> {usuario_ingresado.lower() == usuario_correcto.lower()}")
print("-" * 50)


# ==============================================================================
# SECCIÓN 6: LOGICAL OPERATORS
# Referencia: https://www.w3schools.com/python/python_operators_logical.asp
# ==============================================================================

print("\n=== SECCIÓN 6: LOGICAL OPERATORS ===")

# Ejemplo 1: Operador `and` (Requiere que ambas condiciones sean verdaderas)
edad = 22
tiene_licencia = True

puedo_conducir = (edad >= 18) and tiene_licencia

print("Ejemplo 1 (Operador AND):")
print(f"Edad: {edad} (>=18), Licencia: {tiene_licencia}")
print(f"¿Puede conducir? (edad >= 18 and tiene_licencia): {puedo_conducir}")
print()

# Ejemplo 2: Operador `or` (Requiere que al menos una condición sea verdadera)
es_fin_de_semana = False
es_dia_feriado = True

hay_descanso = es_fin_de_semana or es_dia_feriado

print("Ejemplo 2 (Operador OR):")
print(f"Fin de semana: {es_fin_de_semana}, Día feriado: {es_dia_feriado}")
print(f"¿Hay descanso? (es_fin_de_semana or es_dia_feriado): {hay_descanso}")
print()

# Ejemplo 3: Operador `not` (Invierte el resultado lógico)
sistema_bloqueado = False

print("Ejemplo 3 (Operador NOT):")
print(f"Estado 'sistema_bloqueado': {sistema_bloqueado}")
print(f"¿El sistema está disponible? (not sistema_bloqueado): {not sistema_bloqueado}")
print("-" * 50)

print("Fundamentos David Barrera NC = 1388")