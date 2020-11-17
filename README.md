[![codecov](https://codecov.io/gh/PriSacc/tp-agiles/branch/master/graph/badge.svg?token=6NDLZI4VRY)](undefined) [![Build Status](https://travis-ci.com/PriSacc/tp-agiles.svg?branch=master)](https://travis-ci.com/PriSacc/tp-agiles)
# TPI - Ahorcado - Metodologias Ágiles 🌵 
Un clon del famoso juego del ahoracado usando React.js, Bootstrap y Flask para la API. Toda la logica de negocio
es manejada por el backend.

Las instrucciones asumen que el directorio actual será el directorio del proyecto.

## Para la API del Backend 🔥 
Se necesita Python3 y las siguientes librerias, para su funcionamiento:
- Flask (`pip install flask`)
- Flask-CORS (`pip install flask-cors`)

Despues de instalar lo mencionado arriba, correr `python hangman_api.py`, para iniciar el servicio.
Debería estar corriendo en el puerto 5000.

## Para el Frontend 🔥 
Requiere tener instalado Node.js y NPM (http://nodejs.org)

Una vez instalados, ejecutar `npm install` para instalar todas las dependencias necesarias.

Correr `npm start` para iniciar el development web server. Deberia abrirse una ventana al ejecutarse en
http://localhost:3000.

## Ejecutar casos de prueba 🔥 

Correr `python test_hangman_api.py` para correr los tests.
