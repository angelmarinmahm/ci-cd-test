from app import es_contrasena_segura

def test_contrasena_segura():
    resultado = es_contrasena_segura("SecureP@ss123")
    assert resultado["es_segura"] is True

def test_longitud_insegura():
    resultado = es_contrasena_segura("P@s1")
    assert resultado["es_segura"] is False
    assert resultado["longitud_aceptada"] is False

def test_sin_mayuscula():
    resultado = es_contrasena_segura("securep@ss123")
    assert resultado["es_segura"] is False
    assert resultado["tiene_mayuscula"] is False

def test_sin_minuscula():
    resultado = es_contrasena_segura("SECUREP@SS123")
    assert resultado["es_segura"] is False
    assert resultado["tiene_minuscula"] is False

def test_sin_numero():
    resultado = es_contrasena_segura("SecureP@ss")
    assert resultado["es_segura"] is False
    assert resultado["tiene_numero"] is False

def test_sin_caracter_especial():
    resultado = es_contrasena_segura("SecurePass123")
    assert resultado["es_segura"] is False
    assert resultado["tiene_caracter_especial"] is False