import pygame
pygame.init()
ventana = pygame.display.set_mode((1000, 800))
azul = (125, 190, 240)
COLOR_FONDO = azul
clock = pygame.time.Clock()
pygame.display.set_caption("Mi primer Programa Grafico")
corriendo = True
contador_frames = 0
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        elif evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_ESCAPE:
                corriendo = False    

    ventana.fill(COLOR_FONDO)
    pygame.display.flip() 
pygame.quit()