Feature: jugar 

  Scenario: perder
     Given entrar en la pagina
      When se arriesga una palabra para perder
      Then se pierde la partida

  Scenario: ganar
     Given entrar en la pagina
      When se arriesga una palabra para ganar
      Then se gana la partida
      