import pygame, sys
import move1,move2,move3,move4,move5,move6 #importar os níveis


pygame.init() #inicializar o jogo
tela= pygame.display.set_mode((500,500)) #abrir a tela de jogo
n1= pygame.image.load("nivel1.png").convert_alpha()  #imagens para os botões
n2= pygame.image.load("nivel2.png").convert_alpha()
n3= pygame.image.load("nivel3.png").convert_alpha()
n4= pygame.image.load("nivel4.png").convert_alpha()
n5= pygame.image.load("nivel5.png").convert_alpha()
n6= pygame.image.load("nivel6.png").convert_alpha()

class Button(): #classe dos botões do menu
    def __init__(self, x, y, image, scale):
        width = image.get_width()     #tamanho
        height = image.get_height()
        self.image= pygame.transform.scale(image, (int(width*scale), int(height*scale))) #escala
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)   #posição
        self.clicked = False     #verificar se o botão já foi clicado
    def draw(self):
        tela.blit(self.image, (self.rect.x, self.rect.y))  #desenhar o botão na tela


def menu():   #função principal do jogo
    sair=True
    pygame.display.set_caption("Menu")   #nome da janela
    n1_button=Button(190,80,n1,0.3)   #diferentes butões correspondentes a cada nível
    n2_button=Button(190,150,n2,0.3)
    n3_button=Button(190,220,n3,0.3)
    n4_button=Button(190,290,n4,0.3)
    n5_button=Button(190,360,n5,0.3)
    n6_button=Button(190,430,n6,0.3)
    while (sair!=False):
        tela.fill((255,255,255))    #fundo da tela branco
        n1_button.draw()   #desenhar todos os botões no menu
        n1_button.draw()
        n2_button.draw()
        n3_button.draw()
        n4_button.draw()
        n5_button.draw()
        n6_button.draw()
        for event in pygame.event.get(): #verificar eventos no jogo
            if event.type == pygame.QUIT: #precionar o botão de fechar a janela
                sair=False  #fechar o loop principal do jogo
            if event.type == pygame.MOUSEBUTTONDOWN: #verificar toques com o rato em cada botão dos níveis e abrir o respetivo nível
                if event.button == 1 and n1_button.rect.collidepoint(event.pos):
                    move1.nvl1()
                if event.button == 1 and n2_button.rect.collidepoint(event.pos):
                    move2.nvl2()
                if event.button == 1 and n3_button.rect.collidepoint(event.pos):
                    move3.nvl3()
                if event.button == 1 and n4_button.rect.collidepoint(event.pos):
                    move4.nvl4()
                if event.button == 1 and n5_button.rect.collidepoint(event.pos):
                    move5.nvl5()
                if event.button == 1 and n6_button.rect.collidepoint(event.pos):
                    move6.nvl6()

        pygame.display.update() #fazer update do jogo
    pygame.quit()
    sys.exit   #sair do jogo
menu()
