from app import es_contrasena_segura as cs

def test_contrasena_segura():
    resultado = cs("SecureP@ss123")
    assert resultado["es_segura"] is True

def test_longitud_insegura():
    resultado = cs("P@s1")
    assert resultado["es_segura"] is False
    assert resultado["longitud_aceptada"] is False

def test_sin_mayuscula():
    resultado = cs("securep@ss123")
    assert resultado["es_segura"] is False
    assert resultado["tiene_mayuscula"] is False

def test_sin_minuscula():
    resultado = cs("SECUREP@SS123")
    assert resultado["es_segura"] is False
    assert resultado["tiene_minuscula"] is False

def test_sin_numero():
    resultado = cs("SecureP@ss")
    assert resultado["es_segura"] is False
    assert resultado["tiene_numero"] is False

def test_sin_caracter_especial():
    resultado = cs("SecurePass123")
    assert resultado["es_segura"] is False
    assert resultado["tiene_caracter_especial"] is False