import pygame
pygame.init()

# Configuración de ventana
ventana = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Cambio de color con teclas")

# Colores
AZUL = (125, 190, 240)
ROJO = (240, 100, 100)
VERDE = (100, 240, 150)
AMARILLO = (240, 240, 120)

# Color inicial
color_fondo = AZUL

# Variable de control
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Detectar teclas presionadas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_c]:
        color_fondo = ROJO
    elif teclas[pygame.K_v]:
        color_fondo = VERDE
    elif teclas[pygame.K_a]:
        color_fondo = AZUL
    elif teclas[pygame.K_y]:
        color_fondo = AMARILLO

    # Rellenar la ventana con el color actual
    ventana.fill(color_fondo)
    pygame.display.flip()

pygame.quit()


#rojo = (245, 73, 39)
#verde = (126, 204, 128)