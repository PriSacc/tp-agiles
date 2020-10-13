import random

class Juego(): 
    def __init__(self):
        self.intento = 0
        self.intentos_originales = 0
        self.long = 0
        self.palabra = ""
        self.condicion = False
        self.dificultad = 0
        self.puntaje = 0
        self.palabras_1 = [{'palabra' : 'Madrid', 'descripcion': 'Ciudad grande de España'},{'palabra' : 'Paris', 'descripcion': 'Ciudad grande de Francia'},{'palabra' : 'Elefante', 'descripcion': 'Animal grande'},{'palabra' : 'Gallina', 'descripcion': 'Animal de granja'}]
        self.palabras_2 = [{'palabra' : 'Barcelona', 'descripcion': 'Ciudad grande de España'},{'palabra' : 'Lyon', 'descripcion': 'Ciudad grande de Francia'},{'palabra' : 'Rinoceronte', 'descripcion': 'Animal grande'},{'palabra' : 'Oveja', 'descripcion': 'Animal de granja'}]
        self.letras_ingresadas_correctas = []
        self.letras_ingresadas_incorrectas = []

    def tirar(self): 
        return 0

    def score_final(self, puntaje): 
        return puntaje

    def devolver_intento(self):
        return self.intento

    def palabra_correcta(self, pal):
        if self.palabra.lower == pal.lower:
            self.condicion = True
            return True
        else:
            self.intento -= 1
            if self.intento == 0: #termina juego
                self.condicion = False
                return False

    def devolver_longitud(self):
        return self.long

    def devolver_condicion(self):
        return self.condicion

    def devolver_palabra(self):
        return self.palabra

    def setear_palabra(self,pal):
        self.palabra = pal
        self.long = len(pal)

    def setear_intentos(self,inte):
        self.intento = inte
        self.intentos_originales = inte

    def devolver_dificultad(self):
        return self.dificultad

    def setear_dificultad(self,dificultad):
        self.dificultad = dificultad

    def calcular_puntajes(self):
        if self.condicion == True:
            self.puntaje = 100 * (self.dificultad / (1 + self.intentos_originales - self.intento))
            return  self.puntaje
        else:
            self.puntaje = 0
            return  self.puntaje

    def seleccionar_palabra(self,dificultad):
        if dificultad == 1:
            a = random.choice(list(self.palabras_1))
            return a

        if dificultad == 2:
            a = random.choice(list(self.palabras_2))
            return a

    def esta_incluida(self,letra):
        if self.palabra.find(letra) != -1:
            return True
        else:
            return False

    def letra_correcta(self, pal):
        if self.esta_incluida(pal):
            return True
        else:
            self.intento -= 1
            if self.intento == 0: #termina juego
                self.condicion = False
            return False

    def arriesgar(self, letra):
        if letra not in self.letras_ingresadas_correctas and letra not in self.letras_ingresadas_incorrectas: 
            cont = 0
            palabra = self.devolver_palabra()
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    self.letras_ingresadas_correctas.append(palabra[i]) 
                    cont += 1
            if cont == 0:
                self.intento -= 1
                self.letras_ingresadas_incorrectas.append(letra)
        self.obtener_resultado()

    def obtener_resultado(self):
        if len(self.palabra)==len(self.letras_ingresadas_correctas):
            self.condicion = True
        else:
            self.condicion = False

        




        