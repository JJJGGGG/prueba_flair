# Ejecución del código

# Interfaz por consola

## Mostrar mapa

El mapa izquierdo muestra el estado de los sensores de cada habitación.


# Clases y relaciones

# Decisiones de diseño
El edificio parte con un número aleatorio de zombies, que entran por las ventanas a habitaciones aleatorias del primer piso. Cada turno, cada zombie puede con igual probabilidad moverse a cualquiera de las habitaciones adyacentes (arriba, abajo, a los lados) o quedarse en la misma habitación. Si el zombie elige moverse a una habitación que no existe, se queda en la habitación en la que está.

El sensor se apaga luego de que todos los zombies salen de la habitación.