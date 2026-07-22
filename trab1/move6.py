import pygame
from collections import deque
# Definir as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
COR_PECA_1 = (255, 0, 0)  # Vermelho
COR_PECA_2 = (0, 0, 255)  # Azul
COR_PECA_6 = (128,128,128) # cinzento
board=[[3,3,3,3,3,3,3],[3,3,0,0,3,3,3],[3,2,0,0,3,0,3],[3,0,3,1,0,1,3],[3,0,0,0,0,0,3],[3,2,3,3,0,3,3],[3,3,3,3,3,3,3]]
class peca1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def posicao(self,a):
        if a==2:
            return(self.y)
        elif a==1:
            return(self.x)
    def desenhar(self, tela):
        TAMANHO_TABULEIRO = 500
        pygame.draw.rect(tela, COR_PECA_1, (self.x * TAMANHO_TABULEIRO // 5, self.y * TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5))
        pygame.draw.rect(tela, PRETO, (self.x * TAMANHO_TABULEIRO // 5, self.y * TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5),2)
    def move(self, move, n):
        if move == 'up':
            while (board[self.x+1][self.y+1-1]!=3 and board[self.x+1][self.y+1-1]!=1 and self.y>0):
                board[self.x+1][self.y+1-1]=1
                board[self.x+1][self.y+1]=0
                self.y-=1
        if move == 'down':
            while (board[self.x+1][self.y+1+1]!=3 and board[self.x+1][self.y+1+1]!=1 and self.y<=n):
                board[self.x+1][self.y+1+1]=1
                board[self.x+1][self.y+1]=0
                self.y+=1
        if move == 'left':
            while (board[self.x+1-1][self.y+1]!=3 and board[self.x+1-1][self.y+1]!=1 and self.x>0):
                board[self.x+1-1][self.y+1]=1
                board[self.x+1][self.y+1]=0
                self.x-=1
        if move == 'right':
            while (board[self.x+1+1][self.y+1]!=3 and board[self.x+1+1][self.y+1]!=1 and self.x<=n):
                board[self.x+1+1][self.y+1]=1
                board[self.x+1][self.y+1]=0
                self.x+=1
        return 0
    def descobrir(self):
        return (self.x, self.y, COR_PECA_1)
    def match(self):
        s=0
        for posicao, cor in pecas_circulo.items():
            x, y = posicao
            if (self.x, self.y, COR_PECA_1)==(x,y,cor):
                s+=1
        return s
class peca2:
    def __init__(self,x,y):
        self.x= x
        self.y= y
    def posicao(self,a):
        if a==2:
            return(self.y)
        elif a==1:
            return(self.x)
    def desenhar(self, tela):
        TAMANHO_TABULEIRO = 500
        pygame.draw.rect(tela, COR_PECA_2, (self.x * TAMANHO_TABULEIRO // 5, self.y * TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5))
        pygame.draw.rect(tela, PRETO, (self.x * TAMANHO_TABULEIRO // 5, self.y * TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5),2)
    def move(self, move, n):
        if move == 'up':
            while (board[self.x+1][self.y+1-1]!=3 and board[self.x+1][self.y+1-1]!=1 and self.y>0):
                board[self.x+1][self.y+1-1]=1
                board[self.x+1][self.y+1]=0
                self.y-=1
        if move == 'down':
            while (board[self.x+1][self.y+1+1]!=3 and board[self.x+1][self.y+1+1]!=1 and self.y<=n):
                board[self.x+1][self.y+1+1]=1
                board[self.x+1][self.y+1]=0
                self.y+=1
        if move == 'left':
            while (board[self.x+1-1][self.y+1]!=3 and board[self.x+1-1][self.y+1]!=1 and self.x>0):
                board[self.x+1-1][self.y+1]=1
                board[self.x+1][self.y+1]=0
                self.x-=1
        if move == 'right':
            while (board[self.x+1+1][self.y+1]!=3 and board[self.x+1+1][self.y+1]!=1 and self.x<=n):
                board[self.x+1+1][self.y+1]=1
                board[self.x+1][self.y+1]=0
                self.x+=1
        return 0
    def match(self):
        s=0
        for posicao, cor in pecas_circulo.items():
            x, y = posicao
            if (self.x, self.y, COR_PECA_2)==(x,y,cor):
                s+=1
        return s

def nvl6():
    peca_1=peca1(2,2)
    peca_2=peca2(2,4)
    pygame.init()
    TAMANHO_TABULEIRO = 500
    tela = pygame.display.set_mode((TAMANHO_TABULEIRO, 100+TAMANHO_TABULEIRO))
    pygame.display.set_caption('Match the tiles')
    relogio = pygame.time.Clock()
    sair=False
    while sair != True:
        relogio.tick(27)
        tela.fill(BRANCO)
        desenhar_tabuleiro(tela, TAMANHO_TABULEIRO)
        peca_1.desenhar(tela)
        peca_2.desenhar(tela)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    direcao = "up"
                    if (peca_1.posicao(2)==(peca_2.posicao(2)+1) or peca_1.posicao(2)==(peca_2.posicao(2)+2) or peca_1.posicao(2)==(peca_2.posicao(2)+3) or peca_1.posicao(2)==(peca_2.posicao(2)+4)):
                        peca_2.move(direcao, 6)
                        peca_1.move(direcao, 6)
                    else:
                        peca_1.move(direcao, 6)
                        peca_2.move(direcao, 6)
                elif event.key == pygame.K_DOWN:
                    direcao = "down"
                    if (peca_1.posicao(2)==(peca_2.posicao(2)-1) or peca_1.posicao(2)==(peca_2.posicao(2)-2) or peca_1.posicao(2)==(peca_2.posicao(2)-3) or peca_1.posicao(2)==(peca_2.posicao(2)-4)):
                        peca_2.move(direcao, 6)
                        peca_1.move(direcao, 6)
                    else:
                        peca_1.move(direcao, 6)
                        peca_2.move(direcao, 6)
                elif event.key == pygame.K_LEFT:
                    direcao = "left"
                    if (peca_1.posicao(1)==(peca_2.posicao(1)+1) or peca_1.posicao(1)==(peca_2.posicao(1)+2) or peca_1.posicao(1)==(peca_2.posicao(1)+3) or peca_1.posicao(1)==(peca_2.posicao(1)+4)):
                        peca_2.move(direcao, 6)
                        peca_1.move(direcao, 6)
                    else:
                        peca_1.move(direcao, 6)
                        peca_2.move(direcao, 6)
                elif event.key == pygame.K_RIGHT:
                    direcao = "right"
                    if (peca_1.posicao(1)==(peca_2.posicao(1)-1) or peca_1.posicao(1)==(peca_2.posicao(1)-2) or peca_1.posicao(1)==(peca_2.posicao(1)-3) or peca_1.posicao(1)==(peca_2.posicao(1)-4)):
                        peca_2.move(direcao, 6)
                        peca_1.move(direcao, 6)
                    else:
                        peca_1.move(direcao, 6)
                        peca_2.move(direcao, 6)
                elif event.key == pygame.K_h:
                    dica = bfs(board, (peca_1.x, peca_1.y), (peca_2.x, peca_2.y))
                    if dica:
                        print("Dica:", dica)
                elif event.key == pygame.K_r:
                    peca_1.x, peca_1.y = 2, 2
                    peca_2.x, peca_2.y = 2, 4
                    board_reset()
                    print("Jogo reiniciado.")
                peca_1.desenhar(tela)
                peca_2.desenhar(tela)
                a=peca_1.match()
                b=peca_2.match()
                if a==1 and b==1:
                    sair=True
                    print('terminou')

pecas_circulo = {
    (1, 0): COR_PECA_1,
    (4, 0): COR_PECA_2,
}
def desenhar_tabuleiro(tela, TAMANHO_TABULEIRO):
    for i in range(1, 6):
        pygame.draw.line(tela, PRETO, (i * TAMANHO_TABULEIRO // 5, 0), (i * TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO))
        pygame.draw.line(tela, PRETO, (0, i * TAMANHO_TABULEIRO // 5), (TAMANHO_TABULEIRO, i * TAMANHO_TABULEIRO // 5))
    pecas_fixas = {
        (0, 0): COR_PECA_6,
        (2, 1): COR_PECA_6,
        (4, 1): COR_PECA_6,
        (4, 2): COR_PECA_6,
        (0, 3): COR_PECA_6,
        (1, 3): COR_PECA_6,
        (0, 4): COR_PECA_6,
        (4, 4): COR_PECA_6
    }
    # Desenhar as peças
    for posicao, cor in pecas_fixas.items():
        x, y = posicao
        # Calcular o centro da peça
        centro_x = x * TAMANHO_TABULEIRO // 5 + TAMANHO_TABULEIRO // 10
        centro_y = y * TAMANHO_TABULEIRO // 5 + TAMANHO_TABULEIRO // 10
        pygame.draw.rect(tela, cor, (x * TAMANHO_TABULEIRO // 5, y * TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5))
        pygame.draw.rect(tela, PRETO, (x * TAMANHO_TABULEIRO // 5, y * TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5),2)
    for posicao, cor in pecas_circulo.items():
        x, y = posicao
        # Calcular o centro da peça
        centro_x = x * TAMANHO_TABULEIRO // 5 + TAMANHO_TABULEIRO // 10
        centro_y = y * TAMANHO_TABULEIRO // 5 + TAMANHO_TABULEIRO // 10
        pygame.draw.rect(tela, BRANCO, (x * TAMANHO_TABULEIRO // 5, y * TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5))
        pygame.draw.circle(tela, cor, (centro_x, centro_y), TAMANHO_TABULEIRO // 20)
        pygame.draw.rect(tela, PRETO, (x * TAMANHO_TABULEIRO // 5, y * TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5),2)

# Movimentos possíveis
MOVIMENTOS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def bfs(board, start, objetivo):
    queue = deque()
    visitado = set()
    parent = {}

    queue.append(start)
    visitado.add(start)

    while queue:
        atual = queue.popleft()
        if atual == objetivo:
            caminho = [objetivo]
            while caminho[-1] != start:
                caminho.append(parent[caminho[-1]])
            return caminho[::-1]

        for movimento in MOVIMENTOS:
            nova_posicao = (atual[0] + movimento[0], atual[1] + movimento[1])
            if 0 <= nova_posicao[0] < len(board) and 0 <= nova_posicao[1] < len(board[0]) and board[nova_posicao[0]][nova_posicao[1]] != 3 and nova_posicao not in visitado:
                queue.append(nova_posicao)
                visitado.add(nova_posicao)
                parent[nova_posicao] = atual

    dist_x = objetivo[0] - start[0]
    dist_y = objetivo[1] - start[1]
    if abs(dist_x) > abs(dist_y):
        if dist_x > 0:
            return "Mova para baixo"
        else:
            return "Mova para cima"
    else:
        if dist_y > 0:
            return "Mova para a direita"
        else:
            return "Mova para a esquerda"

    return "Não há dica disponível"

def board_reset():
    global board
    board =[[3,3,3,3,3,3,3],[3,3,0,0,3,3,3],[3,2,0,0,3,0,3],[3,0,3,1,0,1,3],[3,0,0,0,0,0,3],[3,2,3,3,0,3,3],[3,3,3,3,3,3,3]]

if __name__ == "__main__":
    main()
