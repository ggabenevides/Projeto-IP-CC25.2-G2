import pygame as pg
import sys
import os

class TelaInicial:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pg.time.Clock()
        self.mostrando_instrucoes = False
        
        # Caminhos 
        path_img = os.path.join( "assets", "telas de transição", "tela_inicial.png")
        path_fonte = os.path.join("assets", "fonte", "fonte.ttf")

        # Carregar e ajustar fundo
        self.bg = pg.image.load(path_img).convert()
        self.bg = pg.transform.smoothscale(self.bg, self.screen.get_size())

        # Fontes
        self.fonte = pg.font.Font(path_fonte, 18)
        self.fonte_titulo = pg.font.Font(path_fonte, 22)
        self.fonte_pequena = pg.font.Font(path_fonte, 12)

        # dimensões da tela
        w, h = self.screen.get_size()

        # botão de iniciar
        self.btn_iniciar = pg.Rect(
            int(w * 0.39),
            int(h * 0.80),
            int(w * 0.24),
            int(h * 0.06)
        )

        # botão de instruções
        self.btn_instrucoes = pg.Rect(
            int(w * 0.39),
            int(h * 0.88),
            int(w * 0.24),
            int(h * 0.06)
        )

        self.btn_fechar_inst = pg.Rect(0, 0, 35, 35)

    def desenhar(self):
        self.screen.blit(self.bg, (0, 0))

        if self.mostrando_instrucoes:
            self.desenhar_overlay_instrucoes()


    def desenhar_overlay_instrucoes(self):
        # Fundo escurecido
        overlay = pg.Surface(self.screen.get_size(), pg.SRCALPHA)
        overlay.fill((0, 0, 0, 200))
        self.screen.blit(overlay, (0, 0))

        # Painel central
        caixa = pg.Rect(100, 100, 600, 400)
        pg.draw.rect(self.screen, (230, 210, 250), caixa, border_radius=15)
        
        # Texto
        txt_titulo = self.fonte_titulo.render("INSTRUÇÕES", True, (60, 30, 100))
        self.screen.blit(txt_titulo, (caixa.centerx - txt_titulo.get_width()//2, 140))

        regras = ["Gisele está em um dia comum de trabalho nas", "passarelas quando percebe que está sendo", "sabotada! Ajude a mais mais a acabar o desfile", "REGRAS:", "- Evite as cascas de banana e os flashes dos","paparazzi!", "- Colete o máximo de rosas possíveis", "- Utilize o space para pular"]
        for i, linha in enumerate(regras):
            img_txt = self.fonte_pequena.render(linha, True, (50, 50, 50))
            self.screen.blit(img_txt, (140, 200 + i * 40))

        # Botão X
        self.btn_fechar_inst.topright = (caixa.right - 50, caixa.top + 20)
        pg.draw.rect(self.screen, (180, 70, 70), self.btn_fechar_inst, border_radius=5)
        txt_x = self.fonte.render("X", True, (255, 255, 255))
        self.screen.blit(txt_x, txt_x.get_rect(center=self.btn_fechar_inst.center))


    def rodar(self):
        while True:
            self.desenhar()
            pg.display.flip()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit(); sys.exit()
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        if self.mostrando_instrucoes: 
                            self.mostrando_instrucoes = False
                        else: 
                            pg.quit(); sys.exit()
                    
                    # SE APERTAR ENTER OU ESPAÇO, SAI DO LOOP E RETORNA AO MAIN
                    if not self.mostrando_instrucoes and event.key in (pg.K_RETURN, pg.K_SPACE):
                        return True


                if event.type == pg.MOUSEBUTTONDOWN:
                    if not self.mostrando_instrucoes:
                        # SE CLICAR NO BOTÃO INICIAR, RETORNA AO MAIN
                        if self.btn_iniciar.collidepoint(event.pos): 
                            return True
                        if self.btn_instrucoes.collidepoint(event.pos): 
                            self.mostrando_instrucoes = True
                    elif self.btn_fechar_inst.collidepoint(event.pos):
                        self.mostrando_instrucoes = False
            
            self.clock.tick(60)
