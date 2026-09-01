def validar_nombre(nombre):
    if not nombre or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")

    if len(nombre.strip()) < 2:
        raise ValueError("El nombre debe tener al menos 2 caracteres.")

    return nombre.strip()


def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa.")

    if edad > 120:
        raise ValueError("La edad ingresada no es válida.")

    return edad