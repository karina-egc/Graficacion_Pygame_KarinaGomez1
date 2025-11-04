import pygame
pygame.init()

ancho, alto = 800, 800
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Tablero de Ajedrez")


Azul = (125, 190, 240)
Blanco = (255, 255, 255)

tam_cuadro = ancho // 8  # 8 filas y 8 columnas

corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Dibujar el tablero
    for fila in range(8):
        for col in range(8):
            # Alternar colores
            if (fila + col) % 2 == 0:
                color = Blanco
            else:
                color = Azul

            # Dibujar el cuadro
            x = col * tam_cuadro
            y = fila * tam_cuadro
            pygame.draw.rect(ventana, color, (x, y, tam_cuadro, tam_cuadro))

    pygame.display.flip()

pygame.quit()