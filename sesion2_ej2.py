import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO = 800
ALTO = 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Círculos Concéntricos")

# Definir colores (RGB)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
BLANCO = (255, 255, 255)

# Lista de radios y colores
radios = [100, 80, 60, 40, 20]  # Del más grande al más pequeño
colores = [ROJO, VERDE, AZUL, AMARILLO, BLANCO]

# Bucle principal
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                corriendo = False
    
    # Limpiar pantalla con fondo negro
    ventana.fill(NEGRO)
    
    # Dibujar los círculos (del más grande al más pequeño)
    # El centro será el centro de la ventana
    centro_x = ANCHO // 2
    centro_y = ALTO // 2
    
    for i in range(len(radios)):
        pygame.draw.circle(ventana, colores[i], (centro_x, centro_y), radios[i])
    
    # Actualizar la pantalla
    pygame.display.update()

pygame.quit()
sys.exit()