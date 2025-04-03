# tests/test_hola.py

from Hola_mundo import saludar

def test_saludar():
    assert saludar() == "Hola Mundo"
