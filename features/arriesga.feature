Feature: Arriesga
    """
        Se arriesga una palabra incorrecta y se espera la UI de fallo
    """
    Scenario: Prueba de éxito para cuando se arriesga una palabra erronea
        Given Que ingreso al Juego
        When Arriesgo una palabra erronea
        Then Juego perdido