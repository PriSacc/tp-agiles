import unittest
from juego import Juego

class TestJuego(unittest.TestCase): 
    def test_intentos(self):

        # Arrange
        juego = Juego()

        # Act
        x = juego.devolver_intento()

        #Assert
        self.assertEqual(x,3)

    def test_palabra_correcta(self):

        # Arrange
        juego = Juego()

        # Act
        a = 'Roma'
        x = juego.palabra_correcta(a)
        c = juego.devolver_condicion()

        # Assert
        self.assertEqual(x,True)
        self.assertEqual(c,True)

    def test_palabra_incorrecta(self):

        # Arrange
        juego = Juego()
        juego.setear_palabra()

        # Act
        intentos_test = juego.devolver_intento()
        intentos_test -= 1
        a = 'Paris'
        x = juego.palabra_correcta(a)
        intentos_clase = juego.devolver_intento()
        c = juego.devolver_condicion()

        # Assert
        self.assertEqual(intentos_test,intentos_clase)
        self.assertEqual(c,False)

    def test_longitud(self):
        
        # Arrange
        juego = Juego()

        # Act
        x = juego.devolver_longitud()

        # Assert
        self.assertEqual(x,4)

if __name__ == "__main__":
    unittest.main()