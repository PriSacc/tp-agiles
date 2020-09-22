class Juego(): 
    def __init__(self):
        self.intento = 6
        self.long = 4
        self.palabra = 'Roma'

    def tirar(self): 
        return 0

    def score_final(self, puntaje): 
        return puntaje

    def devolver_intento(self):
        return self.intento

    def palabra_correcta(self, pal):
        if self.palabra.lower == pal.lower:
            return True
        else:
            self.intento -= 1
            return False

    def devolver_longitud(self):
        return self.long