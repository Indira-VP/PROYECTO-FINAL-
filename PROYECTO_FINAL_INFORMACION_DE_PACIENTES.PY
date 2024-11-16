class Mascota:
    def __init__(self, nombremascota, edad, raza, especie, sexo, nombredueño, numerocontacto):
        self.nombremascota = nombremascota
        self.edad = edad
        self.raza = raza
        self.especie = especie
        self.sexo = sexo
        self.nombredueño = nombredueño
        self.numerocontacto = numerocontacto

mascota1 = Mascota("Bailey", 2, "🐶 Beagle", "Perro", "Macho", "Deymer", 3156789456)
mascota2 = Mascota("Simon", 2, "🐩 Poodle", "Perro", "Macho", "Indira", 3116554678)
mascota3 = Mascota("Bonnie", 7, "🐕‍🦺 Shih Tzu", "Perro", "Hembra", "Sara", 3178694512)
mascota4 = Mascota("Toño", 3, "🐦Cacatua ", "pajaro", "Macho", "Rick", 3147896523)
mascota5 = Mascota("Mago", 1, "🐈 Siames", "Gato", "Macho", "Carlos", 3105678421)

mascotas = [mascota1, mascota2, mascota3, mascota4, mascota5]
print("📋✨ INFORMACIÓN DE PACIENTES ✨📋\n")
for mascota in mascotas:
    print(f"🐾 Nombre: {mascota.nombremascota}")
    print(f"🎂 Edad: {mascota.edad} años")
    print(f"🐾 Raza: {mascota.raza}")
    print(f"🐾 Especie: {mascota.especie}")
    print(f"⚧ Sexo: {mascota.sexo}")
    print(f"👤 Dueño: {mascota.nombredueño}")
    print(f"📞 Número de contacto: {mascota.numerocontacto}\n")