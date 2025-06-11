#Libreria pytest para las pruebas
import pytest
from turnero import Turnero

#Prueba para verificar que el primer turno de CAJA sea igual a CAJA-001
def test_turno_correcto():
    t = Turnero()
    turno = t.generar_turno("CAJ")
    assert turno == "CAJ-001"

#Prueba para verificar que los tipos definidos de turnos funcionen
def test_tipos_validos():
    t = Turnero()
    for tipo in ["CAJ", "PERS", "REC", "JOP"]:
        turno = t.generar_turno(tipo)
        assert turno.startswith(tipo)

#Excepción cuando el turno no es válido
def test_tipo_invalido():
    t = Turnero()
    with pytest.raises(ValueError):
        t.generar_turno("X")  # Tipo inválido

#Prueba para verificar el formato 
def test_formato_turno():
    t = Turnero()
    turno = t.generar_turno("REC")
    assert turno.startswith("REC-")
    assert len(turno) == 7  # Ej: REC-001 → 7 caracteres

#Prueba incorrecta para que falle a propósito
#def test_turno_incorrecto_fallido():
    #t = Turnero()
    #turno = t.generar_turno("PERS")
    #assert turno == "PERS-005"  # Error intencional: el primer turno debería ser PERS-001
