import pygame
pygame.init()

ancho, alto = 800, 600
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Casa con Figuras Geométricas")

AZUL = (4, 99, 179)
CAFE = (139, 69, 19)
GRIS = (120, 120, 120)
AMARILLO = (255, 255, 100)
ROJO = (255, 0, 0)
FONDO = (200, 230, 255)

# Variable para saber si la casa debe estar toda roja
todo_rojo = False

corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        # Si se presiona la tecla R  toda la casa se vuelve roja
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                todo_rojo = True

    ventana.fill(FONDO)

    color_casa = ROJO if todo_rojo else AZUL
    color_techo = ROJO if todo_rojo else GRIS
    color_puerta = ROJO if todo_rojo else CAFE
    color_ventana = ROJO if todo_rojo else AMARILLO


    casa = pygame.Rect(250, 250, 300, 250)
    pygame.draw.rect(ventana, color_casa, casa)

    puntos_techo = [(250, 250), (550, 250), (400, 150)]
    pygame.draw.polygon(ventana, color_techo, puntos_techo)

    puerta = pygame.Rect(370, 380, 60, 120)
    pygame.draw.rect(ventana, color_puerta, puerta)

    pygame.draw.circle(ventana, color_ventana, (320, 320), 25)
    pygame.draw.circle(ventana, color_ventana, (480, 320), 25)

    
    pygame.display.flip()

pygame.quit()