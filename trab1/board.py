import pygame
import math

# Definir as cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
COR_PECA_1 = (255, 0, 0)  # Vermelho
COR_PECA_2 = (0, 0, 255)  # Azul
COR_PECA_6 = (128,128,128) # cinzento

# Definir o tamanho do tabuleiro
TAMANHO_TABULEIRO = 500

# Criar a tela
tela = pygame.display.set_mode((TAMANHO_TABULEIRO, TAMANHO_TABULEIRO))

# Preencher a tela com branco
tela.fill(BRANCO)

# Desenhar as linhas do tabuleiro
for i in range(1, 5):
    pygame.draw.line(tela, PRETO, (i * TAMANHO_TABULEIRO // 5, 0), (i * TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO))
    pygame.draw.line(tela, PRETO, (0, i * TAMANHO_TABULEIRO // 5), (TAMANHO_TABULEIRO, i * TAMANHO_TABULEIRO // 5))

# Criar as peças
pecas = {
    (3, 0): COR_PECA_1,
    (2, 1): COR_PECA_2,
}
pecas_fixas = {
    (1, 0): COR_PECA_6,
    (3, 1): COR_PECA_6,
    (1, 2): COR_PECA_6,
    (2, 2): COR_PECA_6
}
pecas_circulo = {
    (0, 1): COR_PECA_1,
    (2, 0): COR_PECA_2,
}
# Desenhar as peças
for posicao, cor in pecas.items():
    x, y = posicao
    # Calcular o centro da peça
    centro_x = x * TAMANHO_TABULEIRO // 5 + TAMANHO_TABULEIRO // 10
    centro_y = y * TAMANHO_TABULEIRO // 5 + TAMANHO_TABULEIRO // 10
    pygame.draw.rect(tela, cor, (x * TAMANHO_TABULEIRO // 5, y * TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5))
    pygame.draw.rect(tela, PRETO, (x * TAMANHO_TABULEIRO // 5, y * TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5, TAMANHO_TABULEIRO // 5),2)
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

# Atualizar a tela
pygame.display.update()

# Manter a tela aberta até que o usuário feche
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
