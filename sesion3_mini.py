import pygame
import sys
from collections import deque

pygame.init()
ventana = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Rectángulo con Rastro")

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)

# Parámetros del rectángulo
rect_w, rect_h = 30, 30
x = 200  # Posición inicial X (centro)
y = 150  # Posición inicial Y (centro)
velocidad = 3

# Parámetros del rastro
MAX_RASTRO = 50  # Número máximo de círculos en el rastro
radio_circulo = 3  # Radio de los círculos del rastro
# Usar deque con máximo tamaño para el rastro (más eficiente que una lista)
rastro = deque(maxlen=MAX_RASTRO)

clock = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False

    # Obtener teclas presionadas
    teclas = pygame.key.get_pressed()
    
    # Guardar posición anterior
    pos_anterior = (x + rect_w//2, y + rect_h//2)
    
    # Mover el rectángulo
    if teclas[pygame.K_LEFT]:
        x -= velocidad
    if teclas[pygame.K_RIGHT]:
        x += velocidad
    if teclas[pygame.K_UP]:
        y -= velocidad
    if teclas[pygame.K_DOWN]:
        y += velocidad
    
    # Mantener el rectángulo dentro de la ventana
    x = max(0, min(x, 400 - rect_w))
    y = max(0, min(y, 300 - rect_h))
    
    # Si hubo movimiento, añadir posición al rastro
    if (x + rect_w//2, y + rect_h//2) != pos_anterior:
        rastro.append(pos_anterior)
    
    # Dibujar
    ventana.fill(BLANCO)
    
    # Dibujar el rastro (círculos rojos)
    for pos in rastro:
        pygame.draw.circle(ventana, ROJO, pos, radio_circulo)
    
    # Dibujar el rectángulo
    pygame.draw.rect(ventana, AZUL, (x, y, rect_w, rect_h))
    
    pygame.display.flip()
    clock.tick(144)  # Limitar a 144 FPS

pygame.quit()
sys.exit()