import pygame
import random

def musica(nome_da_musica):
    pygame.mixer.music.load(nome_da_musica)
    pygame.mixer.music.play(-1)

pygame.init()

branco = (255, 255, 255)
prateado = (192, 192, 192)
preto = (0, 0, 0)

fonte = pygame.font.SysFont("Comic Sams MS", 30)

lado_celula = 150
num_linhas = 4

largura = 800
altura = 600

# Resolução = Numeros de linhas por colunas

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Tesla VS Edison")

# Imagens de fundo

tela_inicio = pygame.image.load('./imagens/inicio.png')
tela_inicio1 = pygame.image.load('./imagens/fala1.png')
tela_inicio2 = pygame.image.load('./imagens/fala2.png')
tela_inicio3 = pygame.image.load('./imagens/fala3.png')

tela.blit(tela_inicio, (0, 0))
musica('acdcinstrumental.mp3')

pygame.display.update()

# Tela inicial
jogo_principal = False
jogo_inicio = False
tela1 = True
tela2 = True
tela3 = True

while not jogo_inicio:
    inicio = False
    while not inicio:
        tela.blit(tela_inicio, (0, 0))
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                inicio = True
                jogo_inicio = True
                jogo_principal = True
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE or (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
                inicio = True
                tela1 = False

    while not tela1:
        tela.blit(tela_inicio1, (0, 0))
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                tela_inicio1 = True
                jogo_inicio = True
                jogo_principal = True
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE or (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
                tela1 = True
                tela2 = False

    while not tela2:
        tela.blit(tela_inicio2, (0, 0))
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                tela2 = True
                jogo_inicio = True
                jogo_principal = True
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE or (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
                tela2 = True
                tela3 = False

    while not tela3:
        tela.blit(tela_inicio3, (0, 0))
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                tela3 = True
                jogo_inicio = True
                jogo_principal = True
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE or (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
                tela3 = True
                jogo_inicio = True

while not jogo_principal:

    tela.fill(prateado)
    fundo_do_jogo = pygame.image.load("./imagens/telapontuacao.png")
    tela.blit(fundo_do_jogo, (600, 0))
    tela_ponto = pygame.image.load("./imagens/telapontos.png")
    for i in range(0, num_linhas):
        for j in range(0, num_linhas):
            pygame.draw.rect(tela, preto, (i * lado_celula, j * lado_celula, lado_celula, lado_celula), 1)
    pygame.display.update()

    num_falhas = 0
    num_ideias = 0
    cont_falhas = 0
    cont_ideias = 0
    conteudo_celula = [[None for i in range(num_linhas)] for j in range(num_linhas)]

    # vai marcar com 'X' 18.75% das celulas
    # vai marcar com 'Y' 37.5% das celulas

    for i in range(0, num_linhas):
        for j in range(0, num_linhas):
            if random.randint(1, 100) <= 18.75 and cont_falhas < 3:
                conteudo_celula[i][j] = "X"
                num_falhas += 1
                cont_falhas += 1

            elif random.randint(1, 100) > 18.75 and random.randint(1, 100) <= 56.26 and cont_ideias < 6:
                conteudo_celula[i][j] = "Y"
                num_ideias += 1
                cont_ideias += 1

    # Para cada uma das celulas, verifica o numero de 'Y' ao redor

    for i in range(0, num_linhas):
        for j in range(0, num_linhas):
            if conteudo_celula[i][j] != "Y" and conteudo_celula[i][j] != "X":
                num_bau_redor = 0

                # Acima
                if (i - 1 >= 0 and conteudo_celula[i - 1][j]) == 'Y':
                    num_bau_redor += 1

                # Esquerda
                if (j - 1 >= 0 and conteudo_celula[i][j - 1]) == "Y":
                    num_bau_redor += 1

                # Direita
                if (j + 1 < num_linhas and conteudo_celula[i][j + 1]) == "Y":
                    num_bau_redor += 1

                # Abaixo
                if (i + 1 < num_linhas and conteudo_celula[i + 1][j]) == "Y":
                    num_bau_redor += 1

                conteudo_celula[i][j] = str(num_bau_redor)

    celula_revelada = [[False for i in range(num_linhas)] for j in range(num_linhas)]

    jogo_cancelado = False
    jogador1 = False
    jogador2 = False
    jogadores_empate = False
    pontos1 = 0
    pontos2 = 0
    num_celulas_abertas = 0
    while not jogo_cancelado:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                jogo_cancelado = True
                break

            tela_mudou = False

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

                # Pega as coordenadas do ponto de clique e calcula a celula
                # celula_x  e celula_y são as coordenadas dos pixels na matriz, parasaber qual quadrado foi clicado

                mouse_x, mouse_y = evento.pos

                celula_x = mouse_x // lado_celula
                celula_y = mouse_y // lado_celula

                # Cliquou fora da tela
                if celula_x > num_linhas-1 or celula_y > num_linhas -1:
                    continue
                # Entrada no if se a celula foi clicada pela primeira vez
                if not celula_revelada[celula_x][celula_y]:
                    tela_mudou = True
                    num_celulas_abertas += 1
                    celula_revelada[celula_x][celula_y] = True

                    # Verificação dos pontos do jogador 1

                    if conteudo_celula[celula_x][celula_y] == "Y" and pontos1 >= 0 and num_celulas_abertas % 2 == 1:
                        pontos1 += 100
                    elif conteudo_celula[celula_x][celula_y] == "X" and pontos1 >= 50 and num_celulas_abertas % 2 == 1:
                        pontos1 -= 50

                    # Verificação dos pontos do jogador 2

                    if conteudo_celula[celula_x][celula_y] == "Y" and pontos2 >= 0 and num_celulas_abertas % 2 == 0:
                        pontos2 += 100
                    elif conteudo_celula[celula_x][celula_y] == "X" and pontos2 >= 50 and num_celulas_abertas % 2 == 0:
                        pontos2 -= 50


            if tela_mudou:
                i, j = celula_x, celula_y

                if conteudo_celula[i][j] == "X":
                    falha = pygame.image.load("./imagens/falha.png")
                    falha = pygame.transform.scale(falha, (lado_celula - 2, lado_celula - 2))

                    tela.blit(falha, (lado_celula*i + 1, lado_celula*j + 1))

                elif conteudo_celula[i][j] == "Y":
                    ideia = pygame.image.load("./imagens/ideia.png")
                    ideia = pygame.transform.scale(ideia, (lado_celula - 2, lado_celula - 2))

                    tela.blit(ideia, (lado_celula*i + 1, lado_celula*j + 1))

                else:
                    texto = fonte.render(conteudo_celula[i][j], False, preto)
                    tela.blit(texto, (lado_celula*i + 0.4*lado_celula, lado_celula * j + 0.4 * lado_celula))

            #Pontuação na tela

            tela.blit(tela_ponto, (640, 220))
            texto1 = fonte.render("%d" % pontos1, True, branco)
            tela.blit(texto1, (640, 220))

            tela.blit(tela_ponto, (640, 380))
            texto2 = fonte.render('%d' % pontos2, True, branco)
            tela.blit(texto2, (640, 380))
            pygame.display.update()

            # Verificar quem ganhou o jogo

            if num_celulas_abertas == 16:
                if pontos1 > pontos2:
                    jogador1 = True
                    jogo_cancelado = True

                elif pontos2 > pontos1:
                    jogador2 = True
                    jogo_cancelado = True

                elif pontos1 == pontos2:
                    jogadores_empate = True
                    jogo_cancelado = True

    # Aprensentaçao de quem ganhou ou perdeu
    jogo_final = False

    while not jogo_final:
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                jogo_final = True
                jogo_principal = True
                break
            if jogador1 == True:
                jogador1_tela = pygame.image.load("./imagens/nikolateslawin.png")
                tela.blit(jogador1_tela, (0, 0))
                pygame.display.update()

            if jogador2 == True:
                jogador2_tela = pygame.image.load('./imagens/thomasedisonwin.png')
                tela.blit(jogador2_tela, (0, 0))
                pygame.display.update()


            if jogadores_empate == True:
                empate_tela = pygame.image.load("./imagens/empataram.png")
                tela.blit(empate_tela, (0, 0))
                pygame.display.update()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    jogo_final = True

                if evento.key == pygame.K_n:
                    jogo_principal = True
                    jogo_final = True

pygame.quit()
