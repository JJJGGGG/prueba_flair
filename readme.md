# Ejecución del código
## Instalación de los requerimientos del código

Primeramente, se debe instalar python 3.13 para el correcto funcionamiento del código. Para esto, se recomienda el uso de [pyenv](https://github.com/pyenv/pyenv).

El código necesita un par de paquetes de python para funcionar. Para instalarlos, se recomienda fuertemente usar un virtual environment de python. Primero, hacer `cd` a la carpeta root del código, y luego, utilizar el paquete venv, que en linux sería:

```
python -m venv .venv
source .venv/bin/activate
```

Luego de crear y activar el entorno virtual, se deben instalar los paquetes de python
```
pip install -r requirements.txt
```

## Correr el código
Para correr el código, se debe navegar a la carpeta root del código, para primero activar el ambiente virtual, y luego ejecutar directamente el archivo principal del código:

```
source .venv/bin/activate
python main.py
```

# Interfaz por consola

## Menú principal

El menú principal ofrece 2 opciones:
* Start Simulation: Esta opción ofrece al jugador la posibilidad de empezar la simulación. Lo primero que el programa pide al usuario es la cantidad de pisos del edificio, y luego la cantidad de habitaciones por piso. Estos valores deben ser números enteros, y deben estar dentro de los rangos especificados. Luego, el jugador es llevado al menú de turno.
* Exit: Esta opción permite al jugador cerrar el programa.

## Menú de turno
El menú de turno ofrece 3 opciones:
* Advance Simulation: El jugador avanza la simulación. Al hacer esto, los zombies se mueven y se muestran en pantalla los mensajes de los sensores. Luego, el usuario es devuelto al menú de turno para poder avanzar nuevamente o realizar otras opciones.
* Show Current State: El jugador revisa el estado actual del edificio y de los sensores. Esto se especifica en la sección [Mostrar Mapa](#mostrar-mapa).
* End Simulation: El jugador termina la simulación y es llevado al menú principal, donde puede arrancar nuevamente la simulación o terminar el programa.

## Mostrar mapa

Al mostrar el mapa actual de la simulación, se muestran 2 mapas: uno a la izquierda y otro a la derecha. El mapa izquierdo muestra el estado de los sensores de cada habitación. El mapa derecho muestra la cantidad de zombies en cada habitación.


# Clases y relaciones

## Builder
Esta es la clase que construye el edificio a partir de los parámetros indicados por el usuario. Se encarga de agregar pisos al edificio, habitaciones a los pisos, sensores a los habitaciones, que luego se pueden recuperar gracias a sus métodos `getBuilding` y `getSensors`.

## Zombie
Esta clase representa a un zombie cualquiera. El zombie tiene un nombre aleatorio y una habitación en la que está actualmente, y puede moverse a cualquiera de las habitaciones contiguas con los métodos de los que dispone.

## Building
La clase que representa el edificio. Tiene acceso a cada uno de sus pisos, y da fácil acceso a agregar un piso encima y a recuperar el primer piso del edificio.

## Floor
La clase que representa un piso del edificio. El piso tiene habitaciones, referencias al piso anterior y siguiente, su número de piso y referencia al edificio al que pertenece.

## Room
La clase que representa una habitación del edificio. Esta habitación tiene una lista de zombies, referencias a la habitación anterior y siguiente del piso en la que se encuentra, referencia al piso mismo, su propio número de habitación dentro del piso y una referencia al sensor que se encuentra dentro de la habitación. Permite fácil acceso a que entren o salgan zombies de la habitación. Cuando entran zombies a la habitación, gatilla el sensor.

## Sensor
La clase que representa al sensor dentro de una habitación. Posee un estado, su número de piso y de habitación, y una lista de observadores. Cuando el sensor es gatillado, avisa a todos sus observers que fue gatillado. Momentaneamente sólo le avisa a StatePrinter, pero es fácil de extender. 

## StatePrinter
Esta clase tiene dos responsabilidades:
1. Imprime el estado del edificio cuando el usuario lo pide
2. Alerta al usuario de los cambios de estado de los sensores cuando ellos son gatillados.

## Simulation
Esta es la clase que orquesta la simulación. Permite realizar todas las funcionalidades que el usuario necesita para la simulación de los zombies. Los métodos que ofrece son: crear un edificio con número de pisos y habitaciones, agregar una cantidad dada de zombies a habitaciones del primer piso, y avanzar un turno en la simulación moviendo cada zombie a una habitación adyacente.

## Menu
El menú con el que puede interactuar el usuario. Está hecho de forma de que un menú tenga un atributo de clase llamado opciones, que consisten en tuplas con un nombre y un comportamiento. El nombre es el nombre que verá el usuario en pantalla para saber qué opción está seleccionando. El comportamiento corresponde a una función que recibe la simulación, luego imprime mensajes, pide input al usuario y realiza acciones en la simulación, para finalmente devolver el menú al que llega el usuario después de completar la acción.

La clase base de menú contiene el método de clase `printOptions`, que muestra las acciones del menú actual, permite al usuario elegir una opción de entre ellas, realiza el comportamiento necesario y devuelve el menú siguiente.

Los menús actuales que contiene la aplicación son el menú principal y el menú de simulación, con sus respectivos comportamientos.

# Decisiones de diseño
El edificio parte con un número aleatorio de zombies, que entran por las ventanas a habitaciones aleatorias del primer piso. Cada turno, cada zombie puede con igual probabilidad moverse a cualquiera de las habitaciones adyacentes (arriba, abajo, a los lados) o quedarse en la misma habitación. Si el zombie elige moverse a una habitación que no existe, se queda en la habitación en la que está.

Cuando un zombie entra a una habitación, el sensor de esta se activa. El sensor no se apaga nunca, por lo que el mapa que muestra los sensores lo mostrará prendido para siempre.