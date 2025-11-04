import pygame
import sys

pygame.init()
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
blanco = (255, 255, 255)
azul = (0, 0, 255)
rojo = (255, 0, 0)

RECT_W, RECT_H = 50, 50
x, y = 400, 300
velocidad = 2
rect_color = azul

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_ESCAPE]:
        corriendo = False
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad

    # Evitar que el rectángulo salga de la ventana y cambiar color al tocar bordes
    if x < 0:
        x = 0
        rect_color = rojo  # toca borde izquierdo -> rojo
    elif x + RECT_W > ANCHO:
        x = ANCHO - RECT_W
        rect_color = azul  # toca borde derecho -> azul

    if y < 0:
        y = 0
        rect_color = rojo  # toca borde superior -> rojo
    elif y + RECT_H > ALTO:
        y = ALTO - RECT_H
        rect_color = azul  # toca borde inferior -> azul

    ventana.fill(blanco)
    pygame.draw.rect(ventana, rect_color, (x, y, RECT_W, RECT_H))
    pygame.display.flip()

pygame.quit()
sys.exit()