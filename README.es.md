# Snake Game with Obstacles 🐍

[Read in English](./README.md)

# Presentación

Este proyecto es mi entrega final para la certificación del curso **Code in Place** impartido por la Universidad de Stanford.  
El objetivo fue aplicar los conceptos aprendidos en programación y diseño de juegos, agregando creatividad y mejoras al clásico Snake.

# Descripción

Este es un juego Snake clásico mejorado, desarrollado en Python usando Turtle y Freegames, con las siguientes características:

- Obstáculos aleatorios que aumentan durante la partida y nunca se superponen.
- Obstáculos y comida con detección de colisión realista.
- Obstáculos móviles.
- La comida puede moverse a partir de cierto puntaje.
- Efecto visual al comer la comida (parpadeo).
- Efecto visual de "flash rojo" al perder.
- Mensaje de Game Over con opción de reinicio.
- La serpiente cambia de color según su tamaño.

## Requisitos

- Python 3.x
- [freegames](https://pypi.org/project/freegames/)

Instala freegames con:

```sh
pip install freegames
```

## Cómo jugar

1. Ejecuta el archivo Python:

   ```sh
   python snake.py
   ```

2. Controla la serpiente con las flechas del teclado.
3. Come la comida para crecer y sumar puntos.
4. Evita chocar con los obstáculos, el borde o contigo mismo.
5. Cuando pierdas, presiona la tecla `R` para reiniciar la partida.

## Controles

- Flecha arriba: Mover arriba
- Flecha abajo: Mover abajo
- Flecha izquierda: Mover izquierda
- Flecha derecha: Mover derecha
- R: Reiniciar el juego tras Game Over

## Ideas para futuras mejoras

Este proyecto puede seguir evolucionando con nuevas características y retos. 
Algunas ideas para futuras versiones incluyen:

1. **Mejoras gráficas avanzadas:**  
   Implementar sprites personalizados y animaciones para la serpiente, los obstáculos y la comida, logrando una experiencia visual más atractiva y moderna.

2. **Diseño de niveles progresivos:**  
   Crear diferentes niveles con desafíos únicos, como patrones de obstáculos, velocidad variable y objetivos especiales, aumentando la dificultad de forma gradual.

3. **Menú interactivo y pantalla de inicio:**  
   Añadir un menú principal con opciones para iniciar partida, ver instrucciones, consultar récords y ajustar configuraciones del juego.

4. **Modo multijugador en línea:**  
   Permitir que dos o más jugadores compitan en tiempo real a través de Internet, con tablas de clasificación y emparejamiento automático.

5. **Modo competitivo local para dos jugadores:**  
   Implementar un modo en el que dos jugadores compitan en el mismo dispositivo, cada uno controlando una serpiente y luchando por la comida.

6. **Sistema de logros y recompensas:**  
   Incorporar logros desbloqueables y recompensas visuales por alcanzar ciertos hitos, incentivando la rejugabilidad.

7. **Soporte para dispositivos móviles:**  
   Adaptar la interfaz y controles para que el juego sea jugable en smartphones y tablets, ampliando su accesibilidad.


## Créditos

- Basado en el clásico Snake y el ejemplo de [freegames](https://pypi.org/project/freegames/).
- Mejoras y efectos visuales por Tlaloc Saul.

---

¿Tienes más ideas? ¡Contribuciones y sugerencias son bienvenidas!
¡Diviértete jugando y mejorando el código!