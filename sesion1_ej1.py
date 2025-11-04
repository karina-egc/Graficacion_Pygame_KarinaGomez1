import pygame
pygame.init()

ventana = pygame.display.set_mode((1000, 800))
azul = (125, 190, 240)
COLOR_FONDO = azul
pygame.display.set_caption("Mi primer Programa Grafico")
corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False


    ventana.fill(COLOR_FONDO)
    pygame.display.flip()
        
pygame.quit()