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
        self.palabras_1 = [{'palabra' : 'Madrid', 'descripcion': 'Ciudad grande de España'},{'palabra' : 'Paris', 'descripcion': 'Ciudad grande de Francia'}]
        self.palabras_2 = {'palabra' : 'Barcelona', 'descripcion': 'Ciudad grande de España'}
        

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


        