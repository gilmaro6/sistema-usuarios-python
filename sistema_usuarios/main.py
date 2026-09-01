from app.config.settings import APP_NAME, APP_VERSION, ADMIN_USER
from app.usuarios.gestor import GestorUsuarios


def mostrar_menu():
    print("\n" + "=" * 40)
    print(f"{APP_NAME} - versión {APP_VERSION}")
    print("=" * 40)
    print("1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Buscar usuario")
    print("4. Mostrar configuración")
    print("5. Salir")


def registrar_usuario(gestor):
    try:
        nombre = input("Ingrese el nombre: ")
        edad = int(input("Ingrese la edad: "))

        usuario = gestor.registrar_usuario(nombre, edad)

        print(
            f"\nUsuario registrado correctamente: "
            f"{usuario['nombre']} ({usuario['edad']} años)"
        )

    except ValueError as error:
     if "invalid literal" in str(error):
        print("\nError: La edad debe ser un número entero.")
    else:
        print(f"\nError: {error}")


def listar_usuarios(gestor):
    usuarios = gestor.listar_usuarios()

    if not usuarios:
        print("\nNo hay usuarios registrados.")
        return

    print("\nUsuarios registrados:")

    for posicion, usuario in enumerate(usuarios, start=1):
        print(
            f"{posicion}. "
            f"{usuario['nombre']} - "
            f"{usuario['edad']} años"
        )


def buscar_usuario(gestor):
    nombre = input("Ingrese el nombre que desea buscar: ")

    usuario = gestor.buscar_usuario(nombre)

    if usuario:
        print(
            f"\nUsuario encontrado: "
            f"{usuario['nombre']} - "
            f"{usuario['edad']} años"
        )
    else:
        print("\nNo se encontró el usuario.")


def mostrar_configuracion():
    print("\nConfiguración del sistema")
    print(f"Nombre de la aplicación: {APP_NAME}")
    print(f"Versión: {APP_VERSION}")
    print(f"Usuario administrador: {ADMIN_USER}")


def main():
    gestor = GestorUsuarios()

    while True:
        mostrar_menu()

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            registrar_usuario(gestor)

        elif opcion == "2":
            listar_usuarios(gestor)

        elif opcion == "3":
            buscar_usuario(gestor)

        elif opcion == "4":
            mostrar_configuracion()

        elif opcion == "5":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpción no válida.")


if __name__ == "__main__":
    main()