import pygame as pg
import sys
import os
import textwrap

class TelaFinal:
    def __init__(self, screen, contadores, distancia, meta):
        self.screen = screen
        self.clock = pg.time.Clock()
        self.rodando = True
        self.contadores = contadores
        self.distancia = distancia
        self.meta = meta

        # 1. Lógica de vitória ou derrota
        self.perdeu = contadores["banana"] >= 3 or contadores["camera"] >= 3 or contadores["rosa"] <= 5
        nome_fundo = "tela_derrota.png" if self.perdeu else "tela_vitoria.png"
        
        # 2. Carregamento de Assets
        dir_cenario = os.path.join('assets', 'telas de transição')
        self.bg = pg.image.load(os.path.join(dir_cenario, nome_fundo)).convert()
        self.bg = pg.transform.smoothscale(self.bg, self.screen.get_size())
        
        self.img_botao = pg.image.load(os.path.join(dir_cenario, "botao_reiniciar.png")).convert_alpha()
        
        # Fontes .ttf
        caminho_fonte = os.path.join('assets', 'fonte', 'fonte.ttf')
        self.fonte_titulo = pg.font.Font(caminho_fonte, 26)
        self.fonte_stats = pg.font.Font(caminho_fonte, 18)
        self.fonte_frases = pg.font.Font(caminho_fonte, 14)

        # Configuração da caixa amarela 
        self.x_caixa = 275  
        self.y_caixa = 165
        self.largura_caixa = 450
        self.rect_botao = self.img_botao.get_rect(
            center=(self.screen.get_width() // 2, self.screen.get_height() * 0.9)
        )

    def obter_frases(self):
        frases = []
        rosas = self.contadores["rosa"]
        
        # Frases de penalidade
        if self.contadores["banana"] >= 3:
            frases.append("O chao foi o seu limite. Com tantos tombos, o desfile virou um video de videocassetadas. A sabotagem venceu a sua elegancia desta vez.")
        
        if self.contadores["camera"] >= 3:
            frases.append("Cegada pelos flashes! A luz dos paparazzi te tirou da passarela.")
        
        # Frases de desempenho 
        if rosas <= 0:
            if self.distancia >= self.meta:
                frases.append("Quando o trabalho e bem feito, a inveja e pesada. Infelizmente nao foi dessa vez que voce conseguiu mostrar pras invejosas como e que se faz.")
            else:
                frases.append("Desastre total. Alem de nao conquistar o publico, voce nem sequer conseguiu terminar o percurso. A carreira de Gisele corre perigo!")
        elif 1 <= rosas <= 5:
            frases.append("Um desempenho morno. Voce recebeu algumas flores, mas para uma ubermodel, isso e o equivalente a ser esquecida na proxima edicao.")
        elif 6 <= rosas <= 10:
            frases.append("Muito bom! Voce brilhou apesar das adversidades. O publico reconheceu o esforco e a elegancia de Gisele na passarela.")
        elif rosas > 10:
            frases.append("Espetacular! Nem a sabotagem pode parar a maior de todas. Uma chuva de rosas consagra Gisele como a rainha absoluta da moda!")
        
        return frases

    def draw_texto_quebrado(self, texto, x, y, largura_max):
        linhas = textwrap.wrap(texto, width=38) 
        for linha in linhas:
            img_linha = self.fonte_frases.render(linha, True, (0, 0, 0))
            self.screen.blit(img_linha, (x, y))
            y += 22 
        return y

    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        
        # Desenhar título
        txt_titulo = self.fonte_titulo.render("Resultado do desfile:", True, (0, 0, 0))
        self.screen.blit(txt_titulo, (self.x_caixa + 35, self.y_caixa + 35))
        
        # Desenhar status
        y_atual = self.y_caixa + 85
        status = [
            f"Cascas de banana: {self.contadores['banana']}",
            f"Cameras: {self.contadores['camera']}",
            f"Rosas: {self.contadores['rosa']}"
        ]
        for s in status:
            img_s = self.fonte_stats.render(s, True, (0, 0, 0))
            self.screen.blit(img_s, (self.x_caixa + 50, y_atual))
            y_atual += 32
            
        # Desenhar frases do relatório
        y_atual += 15
        for frase in self.obter_frases():
            y_atual = self.draw_texto_quebrado(frase, self.x_caixa + 35, y_atual, self.largura_caixa)
            y_atual += 12 

        # Desenhar botão reiniciar
        self.screen.blit(self.img_botao, self.rect_botao)

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key in (pg.K_RETURN, pg.K_ESCAPE):
                        return  # volta pra main

            self.draw()
            pg.display.flip()
            self.clock.tick(60)