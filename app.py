def es_contrasena_segura(contrasena: str) -> dict:
    """
    Evalúa si una contraseña es segura cumpliendo con:
    - Mínimo 8 caracteres.
    - Al menos una mayúscula.
    - Al menos una minúscula.
    - Al menos un número.
    - Al menos un carácter especial (@, $, !, %, *, ?, &, #).
    Devuelve un diccionario con el estado general y el detalle de cada criterio.
    """
    caracteres_especiales_aceptados = "@$!%*?&#"

    analisis = {
        "longitud_aceptada": len(contrasena) >= 8,
        "tiene_mayuscula": any(c.isuppper() for c in contrasena),
        "tiene_minuscula": any(c.islower() for c in contrasena),
        "tiene_numero": any(c.isdigit() for c in contrasena),
        "tiene_caracter_especial": any(c in caracteres_especiales_aceptados for c in contrasena)
    }

    # La contraseña es aceptada como segura si cumple todos los criterios

    analisis["es_segura"] = all(analisis.values())

    return analisis

