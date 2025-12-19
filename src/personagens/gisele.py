import pygame
import os

pygame.init()



class Gisele:

    

    def __init__(self):
        self.og_frames = [
        pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_0.png')).convert_alpha(),
        pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_2.png')).convert_alpha(),
        pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_1.png')).convert_alpha(),
        pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_2.png')).convert_alpha(),]
        self.gisele_frames = [pygame.transform.scale(img, (80, 80)) for img in self.og_frames]
        self.frame_idx = 0
        self.frame_timer = 0.0
        self.frame_interval = 0.06

        self.player_x = 120
        self.velocidade_x = 8
        self.chao = 525
        self.player_y = self.chao

        self.vel_y = 0
        self.gravidade = 1
        self.pulando = False
        self.andando = True # essa flag serve pra sinalizar que no final, ela deve parar a animação

    def atualizar_fisica(self): # VERIFICAR APLICAÇÃO DE SELF E SELF

        self.vel_y += self.gravidade
        self.player_y += self.vel_y

        if self.player_y >= self.chao:
            self.player_y = self.chao
            self.vel_y = 0
            self.pulando = False

    def atualizar_animacao(self, delta_time): # VERIFICAR APLICAÇÃO DE SELF

        if not self.pulando and self.andando:
            self.frame_timer += delta_time
            if self.frame_timer >= self.frame_interval:
                self.frame_timer = 0
                self.frame_idx = (self.frame_idx + 1) % len(self.gisele_frames)
        else:
            self.frame_idx = 1

    def pular(self):
        if not self.pulando:
            self.vel_y = -14
            self.pulando = True

    def desenhar(self, tela): # VERIFICAR APLICAÇÃO DE SELF
        tela.blit(self.gisele_frames[self.frame_idx], (self.player_x, self.player_y))

    def get_rect(self): # VERIFICAR APLICAÇÃO DE SELF
        
        largura_hitbox = 50
        altura_hitbox = 70
        
        # centralizando a hitbox na posição da Gisele
        ajuste_x = (80 - largura_hitbox) // 2
        ajuste_y = (80 - altura_hitbox)

        return pygame.Rect(self.player_x + ajuste_x, self.player_y + ajuste_y, largura_hitbox, altura_hitbox)
    
