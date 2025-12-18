import pygame
import os

gisele_frames = [
    pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_0.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_2.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_1.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_2.png')).convert_alpha(),
]

class Gisele:

    gisele_frames = [pygame.transform.scale(img, (80, 80)) for img in gisele_frames]

    def __init__(self):
        self.frame_idx = 0
        self.frame_timer = 0.0
        self.frame_interval = 0.06

        self.player_x = 120
        self.chao = 525
        self.player_y = self.chao

        self.vel_y = 0
        self.gravidade = 1
        self.pulando = False

    def atualizar_fisica(self): # VERIFICAR APLICAÇÃO DE SELF E SELF
        global player_y, vel_y, pulando

        vel_y += self.gravidade
        player_y += vel_y

        if player_y >= self.chao:
            player_y = self.chao
            vel_y = 0
            pulando = False

    def atualizar_animacao(self, delta_time): # VERIFICAR APLICAÇÃO DE SELF
        global frame_timer, frame_idx

        if not pulando:
            frame_timer += delta_time
            if frame_timer >= self.frame_interval:
                frame_timer = 0
                frame_idx = (frame_idx + 1) % len(gisele_frames)
        else:
            frame_idx = 1

    def pular():
        global vel_y, pulando
        if not pulando:
            vel_y = -14
            pulando = True

    def desenhar(self, tela): # VERIFICAR APLICAÇÃO DE SELF
        tela.blit(gisele_frames[frame_idx], (self.player_x, player_y))

    def get_rect(self): # VERIFICAR APLICAÇÃO DE SELF
        return pygame.Rect(self.player_x, player_y, 80, 80)
