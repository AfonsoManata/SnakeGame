import pygame
import random
import sys

pygame.init()
pygame.display.set_caption("Snake Game Python")
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura,altura))
relogio = pygame.time.Clock()

#Cores usando Rgb
preta = (0,0,0)
branca = (255,255,255)
vermelha = (255,0,0)
verde = (0,255,0)

#Parametros da cobra
tamanho_quadrado = 20
velocidade_jogo = 7

#Sair do jogo
sair_jogo = False

#Foto Cobra
foto_cobra = pygame.image.load("foto_cobra2.png")
coordenadas = (350, 550)


#Sons
comeu_som = pygame.mixer.Sound("comeu_som.mp3")
morreu_som = pygame.mixer.Sound("morreu_som.mp3")
def gerar_comida ():
    comida_x = round(random.randrange(0,largura - 3 * tamanho_quadrado)/ 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - 3 * tamanho_quadrado)/ 20.0) * 20.0
    return comida_x, comida_y



def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])


def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])



def tela_final():
    tela.fill(preta)
    fonte = pygame.font.SysFont("Helvetica", 35)
    fonte1 = pygame.font.SysFont("TT Lakes Neue", 75)
    fonte2 = pygame.font.SysFont("Helvetica", 25)
    texto = fonte.render("Parabéns conseguiste sobreviver durante muito tempo!", True, verde)
    texto2 = fonte.render("Se quiseres sair clica duas vezes na tecla ESCAPE!", True, verde)
    texto3 = fonte.render("Se quiseres jogar novamente clica noutra tecla qualquer!", True, verde)
    texto4 = fonte1.render("Snake Game", True, verde)
    texto5 = fonte2.render("Afonso Manata 12ºCT1 Aplicações Informáticas", True, verde)
    texto6 = fonte2.render("Escola Secundária Lima de Faria 28/05/2024", True, verde)
    tela.blit(texto, [240, 250])
    tela.blit(texto2, [240, 350])
    tela.blit(texto3, [240, 450])
    tela.blit(texto4,[400, 100])
    tela.blit(foto_cobra, coordenadas)
    tela.blit(texto5, [650, 700])
    tela.blit(texto6,[650, 750])
    pygame.display.update()

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [1, 1])




def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
        velocidade_x = 0
        velocidade_y = 0
    else:
        velocidade_x = 0
        velocidade_y = 0
    return velocidade_x, velocidade_y

def rodar_jogo():
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    velocidade_x = 0
    velocidade_y = 0

    tamanho_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)


        #desenhar a comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # atualizar a posição da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
            morreu_som.play()
            #Som de morrer
        x += velocidade_x
        y += velocidade_y

        # desenhar a cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra :
            del pixels[0]

        # verificar se bateu nela mesma
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
                morreu_som.play()
                #Som de morrer
        desenhar_cobra(tamanho_quadrado, pixels)

        # desenhar pontuação
        desenhar_pontuacao(tamanho_cobra - 1)

        #atualizar a tela
        pygame.display.update()


        # criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            comeu_som.play()
            #Som de comer
            comida_x, comida_y = gerar_comida()

        relogio.tick(velocidade_jogo + tamanho_cobra / 2)




while True:
    sair_jogo = False
    rodar_jogo()
    tela_final()
    while not sair_jogo:
        relogio.tick(1)
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                sair_jogo = True

