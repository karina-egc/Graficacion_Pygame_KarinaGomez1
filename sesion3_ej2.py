import pygame
import sys
import math

pygame.init()
ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Movimiento Circular")

blanco = (255, 255, 255)
azul = (0, 0, 255)

# Parámetros del rectángulo
rect_w, rect_h = 50, 50

# Centro de la órbita (ventana 400x300 => centro 200,150)
center_x, center_y = 200, 150
# Radio de la órbita
radius = 100
# Ángulo inicial
angle = 0.0
# Velocidad angular en radianes por segundo
angular_speed = 1.0

clock = pygame.time.Clock()
corriendo = True
while corriendo:
    # Gestionar eventos (solo cierre)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Tiempo delta en segundos
    dt = clock.tick(60) / 1000.0

    # Actualizar ángulo usando trigonometría
    angle += angular_speed * dt

    # Calcular posición circular (centrando el rectángulo en la órbita)
    x = center_x + math.cos(angle) * radius - rect_w / 2
    y = center_y + math.sin(angle) * radius - rect_h / 2

    # Dibujar
    ventana.fill(blanco)
    pygame.draw.rect(ventana, azul, (int(x), int(y), rect_w, rect_h))
    pygame.display.flip()

pygame.quit()
sys.exit()