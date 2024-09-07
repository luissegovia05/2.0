class Usuario:
    def __init__(self, nombrecompleto, nickname, clave, tipo, fecha_creacion):
       
        self.datos = {
            "nombrecompleto": nombrecompleto,
            "nickname": nickname,
            "clave": clave,
            "tipo": tipo,
            "fecha_creacion": fecha_creacion
        }
    
    def obtener_dato(self, key):
       
        return self.datos.get(key, None)
    
    def eliminar_dato(self, key):

        if key in self.datos:
            del self.datos[key]

def agregar_usuario(usuarios):
    print("Agregar nuevo usuario:")
    nombrecompleto = input("Nombre completo: ")
    nickname = input("Nickname: ")
    clave = input("Clave: ")
    tipo = input("Tipo: ")
    fecha_creacion = input("Fecha de creación (YYYY-MM-DD): ")
    usuario = Usuario(nombrecompleto, nickname, clave, tipo, fecha_creacion)
    usuarios[nickname] = usuario
    print("Usuario agregado.")

def buscar_usuario(usuarios):
    nickname = input("Ingrese el nickname del usuario a buscar: ")
    usuario = usuarios.get(nickname, None)
    if usuario:
        for key, value in usuario.datos.items():
            print(f"{key}: {value}")
    else:
        print("Usuario no encontrado.")

def eliminar_usuario(usuarios):
    nickname = input("Ingrese el nickname del usuario a eliminar: ")
    if nickname in usuarios:
        del usuarios[nickname]
        print("Usuario eliminado.")
    else:
        print("Usuario no encontrado.")

def menu():
    usuarios = {}
    while True:
        print("\nMenu:")
        print("1 Agregar Usuario")
        print("2 Buscar Usuario")
        print("3 Eliminar Usuario")
        print("4 Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_usuario(usuarios)
        elif opcion == "2":
            buscar_usuario(usuarios)
        elif opcion == "3":
            eliminar_usuario(usuarios)
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()