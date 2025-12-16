import pygame
import os

gisele_frames = [
    pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_0.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_2.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_1.png')).convert_alpha(),
    pygame.image.load(os.path.join('assets', 'sprites', 'gisele', 'sprite_2.png')).convert_alpha(),
]

gisele_frames = [pygame.transform.scale(img, (80, 80)) for img in gisele_frames]

frame_idx = 0
frame_timer = 0.0
frame_interval = 0.06

player_x = 120
chao = 525
player_y = chao

vel_y = 0
gravidade = 1
pulando = False


def atualizar_fisica():
    global player_y, vel_y, pulando

    vel_y += gravidade
    player_y += vel_y

    if player_y >= chao:
        player_y = chao
        vel_y = 0
        pulando = False


def atualizar_animacao(delta_time):
    global frame_timer, frame_idx

    if not pulando:
        frame_timer += delta_time
        if frame_timer >= frame_interval:
            frame_timer = 0
            frame_idx = (frame_idx + 1) % len(gisele_frames)
    else:
        frame_idx = 1


def pular():
    global vel_y, pulando
    if not pulando:
        vel_y = -14
        pulando = True


def desenhar(tela):
    tela.blit(gisele_frames[frame_idx], (player_x, player_y))


def get_rect():
    return pygame.Rect(player_x, player_y, 80, 80)
