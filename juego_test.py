import unittest
from juego import Juego

class TestJuego(unittest.TestCase): 
    def test_intentos(self):

        # Arrange
        juego = Juego()

        # Act
        intentos = 3
        juego.setear_intentos(intentos)
        x = juego.devolver_intento()
        
        #Assert
        self.assertEqual(x,intentos)

    def test_palabra_correcta(self):

        # Arrange
        juego = Juego()

        # Act
        a = 'Roma'
        juego.setear_palabra(a)
        x = juego.palabra_correcta(a)
        c = juego.devolver_condicion()

        # Assert
        self.assertEqual(x,True)
        self.assertEqual(c,True)

    def test_palabra_incorrecta(self):

        # Arrange
        juego = Juego()
        juego.setear_palabra("Paris")

        # Act
        intentos=3
        juego.setear_intentos(intentos)
        intentos_test = juego.devolver_intento()
        intentos_test -= 1
        palabra_incorrecta = 'Madrid'
        x = juego.palabra_correcta(palabra_incorrecta)
        intentos_clase = juego.devolver_intento()
        c = juego.devolver_condicion()

        # Assert
        self.assertEqual(intentos_test,intentos_clase)
        self.assertEqual(c,False)

    def test_longitud(self):
        
        # Arrange
        juego = Juego()

        # Act
        juego.setear_palabra("Roma")
        x = juego.devolver_longitud()

        # Assert
        self.assertEqual(x,4)


    def test_dificultad(self):

        # Arrange
        juego = Juego()

        # Act
        dificultad = 3
        juego.setear_dificultad(dificultad)
        x = juego.devolver_dificultad()

        # Assert
        self.assertEqual(x,dificultad)



    def test_puntaje_primero(self):

        # Arrange
        juego = Juego()

        # Act
        dificultad = 3
        palabra_correcta = "Londres"
        intentos = 5
        juego.setear_dificultad(dificultad)
        juego.setear_palabra(palabra_correcta)
        juego.setear_intentos(intentos)

        juego.palabra_correcta("Londres")

        x = juego.calcular_puntajes()

        # Assert

        self.assertEqual(x,300)


    def test_puntaje_segundo(self):

        # Arrange
        juego = Juego()

        # Act
        dificultad = 2
        palabra_correcta = "Londres"
        intentos = 8
        juego.setear_dificultad(dificultad)
        juego.setear_palabra(palabra_correcta)
        juego.setear_intentos(intentos)

        juego.palabra_correcta("Berlin")
        juego.palabra_correcta("Berlin")
        juego.palabra_correcta("Berlin")
        juego.palabra_correcta("Berlin")
        juego.palabra_correcta("Londres")
        
        x = juego.calcular_puntajes()

        # Assert

        self.assertEqual(x,40)




if __name__ == "__main__":
    unittest.main()