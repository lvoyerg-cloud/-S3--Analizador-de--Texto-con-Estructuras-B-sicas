INSTRUCCIONES DE EJECUCION DEL SISTEMA

Requisitos del entorno

• Python 3.8 o superior instalado.
• Sistema operativo Windows para la funcionalidad de apertura en Bloc de notas (notepad.exe).
• Consola de comandos (CMD o PowerShell).

Estructura del archivo

El sistema esta contenido en el archivo:

analizador_texto.py

Debe ubicarse en un directorio de trabajo accesible, por ejemplo:

C:\ProyectoAnalizador

Procedimiento de ejecucion

Paso 1: Abrir la consola de comandos.
Paso 2: Navegar al directorio del proyecto:

cd C:\ProyectoAnalizador

Paso 3: Ejecutar el programa:

python analizador_texto.py

Flujo de ejecucion

Al iniciar el programa:

a) Se ejecuta automaticamente la funcion run_tests(), que valida el correcto funcionamiento de los metodos principales.
b) Posteriormente se despliega el menu interactivo del sistema.

Menu principal:

Leer archivo y analizar txt

Modo consola

Crear archivo text

Editar archivo text

Abrir archivo en Bloc de notas archivo.text

Eliminar archivo text

Salir

Flujo de analisis de texto

• El usuario selecciona opcion 1 o 2.
• Se obtiene el texto (archivo o entrada manual).
• Se instancia la clase TextAnalyzer.
• Se ejecuta el metodo analyze().
• Se genera el reporte estadistico mediante report().
• Se habilita el modulo de consulta de palabras mediante query() hasta que el usuario escriba exit.

PRUEBAS MINIMAS DEL SISTEMA

Las pruebas minimas verifican el correcto funcionamiento de los componentes esenciales: normalizacion, tokenizacion, conteo, estadisticas y manejo de errores.

I. Pruebas Unitarias Internas

El metodo run_tests() valida automaticamente:

Normalizacion de texto
Entrada: Hola, Mundo!! Python 3.
Salida esperada: hola mundo python 3

Tokenizacion
Entrada: hola mundo python 3
Salida esperada: lista con cuatro elementos

Conteo de frecuencias
Entrada: hola hola mundo
Resultado esperado:
hola = 2
mundo = 1

La ejecucion sin errores indica que los metodos basicos funcionan correctamente.

II. Prueba Funcional – Entrada por Consola

Objetivo: Verificar procesamiento completo del flujo de analisis.

Procedimiento:

Seleccionar opcion 2.

Ingresar el siguiente texto:

Hola mundo hola
END

Resultados esperados:

• Total de tokens: 3
• Tokens unicos: 2
• hola con frecuencia 2
• mundo con frecuencia 1
• Clasificacion de hola: Moderada

Consulta adicional:

Ingresar hola
Debe mostrar frecuencia 2 y porcentaje correspondiente.

III. Prueba Funcional – Entrada por Archivo

Objetivo: Validar lectura y procesamiento de archivo externo.

Preparacion:

Crear archivo prueba.txt con contenido:

Python es potente
Python es versatil

Procedimiento:

Seleccionar opcion 1.

Ingresar la ruta absoluta del archivo.

Resultados esperados:

• python con frecuencia 2
• es con frecuencia 2
• potente con frecuencia 1
• versatil con frecuencia 1

IV. Pruebas de Validacion y Manejo de Errores

Ruta inexistente
Resultado esperado: mensaje indicando que la ruta no existe.

Extension distinta a .txt
Resultado esperado: validacion de extension incorrecta.

Archivo vacio
Resultado esperado: mensaje indicando que el archivo esta vacio.

Texto vacio en modo consola
Resultado esperado: mensaje Texto vacio.

V. Prueba de Consulta de Palabra Inexistente

Durante la fase de consulta, ingresar una palabra que no se encuentre en el texto analizado.

Resultado esperado:

• Mensaje indicando que la palabra no aparece en el texto.
• El sistema no debe detenerse ni generar excepciones.

CRITERIOS DE ACEPTACION

El sistema se considera funcional si:

• Ejecuta sin errores las pruebas internas.
• Procesa correctamente texto desde archivo y consola.
• Genera estadisticas coherentes.
• Clasifica frecuencias correctamente (RARA, Moderada, COMUN).
• Maneja excepciones sin finalizar abruptamente la ejecucion.
• Permite operaciones basicas sobre archivos de texto.
