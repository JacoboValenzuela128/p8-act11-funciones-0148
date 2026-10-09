## Arath Valenzuela 
## NC:0148

# ==============================================================================
# EJEMPLOS DE FUNCIONES EN PYTHON (PYTHONES)
# ==============================================================================

# Ejemplo 1: Función básica sin parámetros
def ejemplo_01():
    print("--- Ejemplo 1: Declaración e invocación básica ---")

    def saludar():
        print("¡Hola! Bienvenido al curso de Python.")

    saludar()


# Ejemplo 2: Parámetros posicionales
def ejemplo_02():
    print("\n--- Ejemplo 2: Parámetros posicionales ---")

    def sumar(a, b):
        resultado = a + b
        print(f"La suma de {a} + {b} es: {resultado}")

    sumar(10, 20)


# Ejemplo 3: Parámetros nombrados (Keywords)
def ejemplo_03():
    print("\n--- Ejemplo 3: Parámetros nombrados ---")

    def mostrar_perfil(nombre, rol, pais):
        print(f"Usuario: {nombre} | Rol: {rol} | País: {pais}")

    # Se especifican las claves, el orden de envío no afecta
    mostrar_perfil(pais="México", nombre="Ana", rol="Admin")


# Ejemplo 4: Número variable de argumentos posicionales (*args)
def ejemplo_04():
    print("\n--- Ejemplo 4: Argumentos arbitrarios (*args) ---")

    def listar_frutas(*frutas):
        print("Lista de frutas recibidas:")
        for fruta in frutas:
            print(f"- {fruta}")

    listar_frutas("Manzana", "Banana", "Uva", "Naranja")


# Ejemplo 5: Argumentos clave-valor dinámicos (**kwargs) y retorno
def ejemplo_05():
    print("\n--- Ejemplo 5: Argumentos nombrados variables (**kwargs) ---")

    def crear_registro(id_usuario, **datos):
        registro = {"id": id_usuario}
        for clave, valor in datos.items():
            registro[clave] = valor
        return registro

    usuario = crear_registro(101, nombre="Carlos", edad=30, activo=True)
    print("Diccionario generado:", usuario)


# ==============================================================================
# EJECUCIÓN DE LOS 5 EJEMPLOS
# ==============================================================================
if __name__ == "__main__":
    ejemplo_01()
    ejemplo_02()
    ejemplo_03()
    ejemplo_04()
    ejemplo_05()

print("Arath Valenzuela")
print("NC:0148")