import json

# Clase para representar una mascota
class Mascota:
    def __init__(self, nombre, especie, raza, edad, sexo, dueño, telefono):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        self.dueño = dueño
        self.telefono = telefono

    def to_dict(self):
        return self.__dict__

# Guardar datos en un archivo JSON
def guardar_en_archivo(lista_mascotas, archivo):
    with open(archivo, "w") as f:
        json.dump([mascota.to_dict() for mascota in lista_mascotas], f, indent=4)
    print("✔️ Datos guardados exitosamente en el archivo.")

# Cargar datos desde un archivo JSON
def cargar_desde_archivo(archivo):
    try:
        with open(archivo, "r") as f:
            return [Mascota(**datos) for datos in json.load(f)]
    except FileNotFoundError:
        return []

# Agregar una mascota a la lista
def agregar_mascota(lista, mascota):
    for m in lista:
        if m.nombre.lower() == mascota.nombre.lower():
            print(f"❗ La mascota '{mascota.nombre}' ya está registrada.")
            return
    lista.append(mascota)
    print(f"\n✔️ Los datos de '{mascota.nombre}' fueron exitosamente agregados. 🤗🐾")

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        menores = [m for m in lista[1:] if m.nombre.lower() <= pivot.nombre.lower()]
        mayores = [m for m in lista[1:] if m.nombre.lower() > pivot.nombre.lower()]
        return quicksort(menores) + [pivot] + quicksort(mayores)

# Mostrar mascotas ordenadas alfabéticamente
def mostrar_mascotas(lista):
    if not lista:
        print("📭 No hay mascotas registradas.")
        return
    # manera en la que se muestra los datos de las mascotas ya ordenadas de manera alfabetica
    print("\n🐾 Lista de Mascotas Ordenada:\n")
    lista_ordenada = quicksort(lista)
    for mascota in lista_ordenada:
        print(f"---------------------------------- ") 
        print(f"🐾 Nombre: {mascota.nombre}") 
        print(f"🐾 Especie: {mascota.especie}")
        print(f"🐾 Raza: {mascota.raza} ") 
        print(f"🐾 Edad: {mascota.edad} años") 
        print(f"🐾 Sexo: {mascota.sexo}  ") 
        print(f"🐾 Dueño: {mascota.dueño} ") 
        print(f"🐾 Teléfono: {mascota.telefono}\n") 
        print(f"---------------------------------- ") 

# Eliminar los datos de una mascota de la lista
def eliminar_mascota(lista, nombre):
    for mascota in lista:
        if mascota.nombre.lower() == nombre.lower():
            lista.remove(mascota)
            print(f"✔️ Los datos de'{nombre}' fueron exitosamente eliminados.")
            return
    print(f"❌ No se encontró una mascota con el nombre '{nombre}'.")

# esta es la función principal para la interacción
def principal():
    archivo = "mascotas.json"
    mascotas = cargar_desde_archivo(archivo)

    while True:
        print("\n 🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴🦴")
        print("\nVETERINARIA 24/7🏥 ")
        print("🐾GESTIÓN DE DATOS DE MASCOTAS🐾\n")

        print("1️⃣  Agregar mascota")
        print("2️⃣  Mostrar mascotas ordenadas")
        print("3️⃣  Eliminar una mascota")
        print("4️⃣  Guardar datos y salir")

        opcion = input("Elije una opción: ")

        if opcion == "1":
            nombre = input("🐾 Nombre de la mascota: ")
            especie = input("🦴 Especie (Perro, Gato, etc.): ")
            raza = input("🐕 Raza: ")
            edad = int(input("🎂 Edad: "))
            sexo = input("⚧ Sexo (Macho o Hembra): ")
            dueño = input("👤 Nombre del dueño: ")
            telefono = input("📞 Teléfono del dueño: ")
            nueva_mascota = Mascota(nombre, especie, raza, edad, sexo, dueño, telefono)
            agregar_mascota(mascotas, nueva_mascota)

        elif opcion == "2":
            mostrar_mascotas(mascotas)

        elif opcion == "3":
            nombre = input("❌🔍 Ingrese el nombre de la mascota a eliminar: ")
            eliminar_mascota(mascotas, nombre)
        elif opcion == "4":
            guardar_en_archivo(mascotas, archivo)
            print("Todos los datos ingresados, han sido exitosamente guaradados ¡Chaitoo! 👋")
            
            break

        else:
            print("❗ Opción inválida. Intenta nuevamente.")

principal()
