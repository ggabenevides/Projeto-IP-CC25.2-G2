import pygame 
from pygame.locals import *
from sys import exit
import os
import math

pygame.init() 
pygame.display.set_caption('Gisele Bundchen VS As Forças Do Mal') # nome do jogo

# inicializando variáveis
altura_tela = 700
largura_tela = 900
dimensoes_tela = (largura_tela, altura_tela)
buff_ativo = False
debuff_ativo = False
tempo_ativo = 0
relogio = pygame.time.Clock()
run = True
scroll = 0

# configurando cenario
tela = pygame.display.set_mode(dimensoes_tela)
original_bg_image = pygame.image.load(os.path.join('assets', 'cenario', 'passarela.png')).convert()
bg_image = pygame.transform.scale(original_bg_image, dimensoes_tela)
bg_width = bg_image.get_width()
tiles = math.ceil(largura_tela / bg_width) + 1 # variavel para o mecanismo de rolagem infinita da tela

# colocando gisele no cenário
gisele_frames = [
    pygame.image.load(os.path.join('assets', 'gisele', 'sprite_0.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'gisele', 'sprite_2.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'gisele', 'sprite_1.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'gisele', 'sprite_2.png')).convert_alpha(),
]

gisele_frames = [pygame.transform.scale(img, (80, 80)) for img in gisele_frames]

frame_idx = 0
frame_timer = 0.0
frame_interval = 0.06

player_x = 120
chao = 525 # altura dela
player_y = chao

vel_y = 0
gravidade = 1
pulando = False

while run:  # loop principal
        delta_time = relogio.tick(30) / 1000.0  # tempo decorrido em segundos

        for event in pygame.event.get():  # fechar a janela do jogo
            if event.type == QUIT:
                run = False
                pygame.quit()
                exit()

            if event.type == KEYDOWN: # identificar o w ou a seta do pulo
                if (event.key == K_w or event.key == K_UP) and not pulando:
                    vel_y = -14
                    pulando = True

        # gravidade do pulo (voltar depois de pular)
        vel_y += gravidade
        player_y += vel_y

        if player_y >= chao:
            player_y = chao
            vel_y = 0
            pulando = False

        # animação andar
        if not pulando:
            frame_timer += delta_time
            if frame_timer >= frame_interval:
                frame_timer = 0
                frame_idx = (frame_idx + 1) % len(gisele_frames)
        else:
            frame_idx = 1  # pulo com os pés juntos

        # desenhando o cenário
        for i in range(0, tiles):
            tela.blit(bg_image, (i * bg_width + scroll, 0))
                    
        # scroll background
        if buff_ativo:
            debuff_ativo = False
            scroll -= 7
            tempo_ativo += 1
            if tempo_ativo >= 100:
                buff_ativo = False
                tempo_ativo = 0
        else:
            scroll -= 7

        if debuff_ativo:
            buff_ativo = False
            scroll -= 1
            tempo_ativo += 1
            if tempo_ativo >= 100:
                debuff_ativo = False
                tempo_ativo = 0
        else:
            scroll -= 7

        # reset scroll do cenario
        if abs(scroll) > bg_width:
            scroll = 0 

        tela.blit(gisele_frames[frame_idx], (player_x, player_y)) # rodar gisele
        pygame.display.update()           