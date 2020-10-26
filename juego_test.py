import unittest
from juego import Juego
from random import choice

class TestJuego(unittest.TestCase): 

    def test_seleccionar_palabra(self):

        # Arrange
        juego = Juego()
        
        # Act
        a = juego.seleccionar_palabra(2)
        if a != None:
            x = True
    
        #Assert
        self.assertTrue(x)

       
    def test_letra_incorrecta_restar_intento(self):

        # Arrange
        juego = Juego()
        a = 'Roma'
        juego.setear_palabra(a)
        intentos = 3
        juego.setear_intentos(intentos)
       
        # Act
        letra_incorrecta = 'e'
        juego.letra_correcta(letra_incorrecta)
        intentos_clase = juego.devolver_intento()
        
        #Assert
        self.assertEqual(intentos_clase,2)


    def test_letra_correcta_no_restar_intento(self):

        # Arrange
        juego = Juego()
        a = 'Roma'
        juego.setear_palabra(a)
        intentos = 3
        juego.setear_intentos(intentos)
       
        # Act
        letra_correcta = 'a'
        juego.letra_correcta(letra_correcta)
        intentos_clase = juego.devolver_intento()
        
        #Assert
        self.assertEqual(intentos_clase,3)

    def test_palabra_correcta(self):

        # Arrange
        juego = Juego()

        # Act
        a = 'Roma'
        juego.setear_palabra(a)
        x = juego.palabra_correcta(a)
        c = juego.devolver_condicion()

        # Assert
        self.assertTrue(c)

    def test_palabra_incorrecta_condicion(self):

        # Arrange
        juego = Juego()
        juego.setear_palabra("Paris")

        # Act
        intentos=3
        juego.setear_intentos(intentos)
        palabra_incorrecta = 'Madrid'
        juego.palabra_correcta(palabra_incorrecta)
        c = juego.devolver_condicion()

        # Assert
        self.assertFalse(c)

    def test_palabra_incorrecta_numero_intento(self):

        # Arrange
        juego = Juego()
        juego.setear_palabra("Paris")

        # Act
        intentos=3
        juego.setear_intentos(intentos)
        intentos_test = juego.devolver_intento()
        intentos_test -= 1
        palabra_incorrecta = 'Madrid'
        juego.palabra_correcta(palabra_incorrecta)
        intentos_clase = juego.devolver_intento()
        

        # Assert
        self.assertEqual(intentos_test,intentos_clase)
        

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

    def test_letra_incluida(self):

        # Arrange
        juego = Juego()
        juego.setear_palabra("Londres")

        # Act
        letra = 'o'
        ingreso = juego.esta_incluida(letra)
        
        # Assert
        self.assertTrue(ingreso)

    def test_letra_no_incluida(self):

        # Arrange
        juego = Juego()
        juego.setear_palabra("Londres")

        # Act
        letra = 'a'
        ingreso = juego.esta_incluida(letra)
        
        # Assert
        self.assertFalse(ingreso)


    def test_finalizacion_juego_perdido(self):

        # Arrange
        juego = Juego()

        # Act
        palabra_correcta = "Londres"
        intentos = 4
        juego.setear_palabra(palabra_correcta)
        juego.setear_intentos(intentos)

        letra = 'a'
        ingreso = juego.arriesgar(letra)
        letra = 'e'
        ingreso = juego.arriesgar(letra)
        letra = 'n'
        ingreso = juego.arriesgar(letra)
        letra = 'a'
        ingreso = juego.arriesgar(letra)
        letra = 'a'
        ingreso = juego.arriesgar(letra)
        letra = 'a'
        ingreso = juego.arriesgar(letra)

        resultado = juego.devolver_condicion()

        # Assert
        self.assertFalse(resultado)

    def test_finalizacion_juego_ganado(self):

        # Arrange
        juego = Juego()

        # Act
        palabra_correcta = "Londres"
        intentos = 4
        juego.setear_palabra(palabra_correcta)
        juego.setear_intentos(intentos)

        letra = 'L'
        ingreso = juego.arriesgar(letra)
        letra = 'o'
        ingreso = juego.arriesgar(letra)
        letra = 'n'
        ingreso = juego.arriesgar(letra)
        letra = 'd'
        ingreso = juego.arriesgar(letra)
        letra = 'r'
        ingreso = juego.arriesgar(letra)
        letra = 'e'
        ingreso = juego.arriesgar(letra)
        letra = 's'
        ingreso = juego.arriesgar(letra)

        resultado = juego.devolver_condicion()

        # Assert
        self.assertTrue(resultado)

    
if __name__ == "__main__":
    unittest.main()
