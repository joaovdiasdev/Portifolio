# Autor: João Victor da Paixão Reis Soares Dias
# Componente Curricular: MI Algoritmos
# Concluído em: 26/10/2024, às 16:00
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

# Sistema Operacional: Windows 10 (código de limpeza = os.system('cls'))
# Bibliotecas importadas (O Numpy e a Keyboard não são nativas do Python, é necessário baixá-las.)
# Para isso, escreva no terminal "pip install" e nome da biblioteca
import os, random, time, keyboard, numpy as np

# Criar o tabuleiro usando numpy
tabuleiro = np.full((20, 10), '⬜')

# Peças do tetris como arrays numpy
pecas = {
    'T': np.array([['⬜', '🟪', '⬜'], 
                   ['🟪', '🟪', '🟪']]),
    
    'I': np.array([['🟦', '🟦', '🟦', '🟦']]),
    
    'S': np.array([['⬜', '🟩', '🟩'], 
                   ['🟩', '🟩', '⬜']]),
    
    'J': np.array([['🟦', '⬜', '⬜'], 
                   ['🟦', '🟦', '🟦']]),
    
    'L': np.array([['⬜', '⬜', '🟧'], 
                   ['🟧', '🟧', '🟧']]),
    
    'Z': np.array([['🟥', '🟥', '⬜'], 
                   ['⬜', '🟥', '🟥']]),
    
    'O': np.array([['🟨', '🟨'], 
                   ['🟨', '🟨']]),
    
    'B': np.array([['💣']])
}

# Função que exibe o tabuleiro e a pontuação
def mostrar_tabuleiro(tabuleiro, pontuacao):
    os.system('cls')
    print(f"Pontuação: {pontuacao}")
    for linha in tabuleiro:
        print("".join(linha))

# Função que desenha uma peça no tabuleiro
def colocar_peca(tabuleiro, peca, x, y):
    tabuleiro2 = tabuleiro.copy()
    for i in range(peca.shape[0]):
        for j in range(peca.shape[1]):
            if peca[i, j] != '⬜': 
                tabuleiro2[y + i, x + j] = peca[i, j]
    return tabuleiro2

# Função que checa colisão da peça com o tabuleiro e retorna True (se tiver colisão) ou False (se não tiver)
def colisao(tabuleiro, peca, x, y):
    for i in range(peca.shape[0]):
        for j in range(peca.shape[1]):
            if peca[i, j] != '⬜':
                if y + i >= 20:
                    return True
                if x + j < 0:
                    return True
                if x + j >= 10:
                    return True
                if tabuleiro[y + i, x + j] != '⬜':
                    return True
    return False

# Função que gira a peça no sentido anti-horário
def girar_peca(peca):
    
    return np.rot90(peca)

# Função que remove as linhas completas do tabuleiro
def remover_linhas(tabuleiro):
    linhas_removidas = 0
    linhas_restantes = tabuleiro[np.any(tabuleiro == '⬜', axis=1)]
    linhas_removidas = 20 - len(linhas_restantes)
    novas_linhas = np.full((linhas_removidas, 10), '⬜')
    tabuleiro_novo = np.vstack((novas_linhas, linhas_restantes))
    
    return tabuleiro_novo, 100 * linhas_removidas

# Função que explode a bomba
def explodir_bomba(tabuleiro, x, y):
    for i in range(max(0, y - 1), min(20, y + 2)):
        for j in range(max(0, x - 1), min(10, x + 2)):
            tabuleiro[i, j] = '⬜'


# CÓDIGO PRINCIPAL #
# Início do jogo: Menu
print("Olá, seja bem vindo ao Super Tetris!")
manual = input("Gostaria de verificar o manual antes de jogar? \n[S]im/[N]ão: ")
print()

if manual in ['S', 's', 'SIM', 'Sim']:
    print('Para jogar esse tetris, utilize as teclas (⬆, ⬇, <- , ->) do seu teclado:')
    print('Segure ( ⬆ ) para rotacionar')
    print('Segure ( <- ) para mover para a esquerda')
    print('Segure ( -> ) para mover para a direita')
    print('Segure ( ⬇ ) para descer mais rápido')
    print('Dica: Apertar ( ⬇ ) e outra tecla ao mesmo tempo ajuda a acelerar o movimento desejado')

dificuldade = input("\n[F]ácil\n[N]ormal\n[D]ifícil\n[S]uper Tetris\nSelecione uma dificuldade para seu jogo: ")
print()
ligar_jogo = input("Pressione [ON] para ligar o jogo: ")

velocidade_queda = 1.0

# Definindo condições de dificuldade
if dificuldade in ['F', 'f', 'Fácil', 'FÁCIL']:
    velocidade_queda = 1.2

elif dificuldade in ['N', 'n', 'Normal', 'NORMAL']:
    velocidade_queda = 0.8

elif dificuldade in ['D', 'd', 'Difícil', 'DIFÍCIL']:
    velocidade_queda = 0.4

elif dificuldade in ['S', 's', 'Super', 'SUPER']:
    velocidade_queda = 0.1

# Definição do tabuleiro, randomização de peças e declaração de variáveis
tabuleiro = np.full((20, 10), '⬜')
peca_atual = random.choice(list(pecas.values()))
x = random.randint(0, 10 - peca_atual.shape[1])
y = 0
pontuacao = 0

# Laço de repetição de ativação

while ligar_jogo in ['ON', 'on', 'On', 'oN']:
    tabuleiro_com_peca = colocar_peca(tabuleiro, peca_atual, x, y)
    mostrar_tabuleiro(tabuleiro_com_peca, pontuacao)

    # Acelerar a peça
    if keyboard.is_pressed('down'):
        time.sleep(0.05)
    else:
        time.sleep(velocidade_queda)

    # Mover a peça para baixo
    if colisao(tabuleiro, peca_atual, x, y + 1) == False:
        y += 1
    else:
        if np.array_equal(peca_atual, pecas['B']):
            explodir_bomba(tabuleiro, x, y)
        else:
            tabuleiro = colocar_peca(tabuleiro, peca_atual, x, y)

        tabuleiro, pontuacao_linhas = remover_linhas(tabuleiro)
        pontuacao += pontuacao_linhas

        # Gera uma nova peça aleatória
        peca_atual = random.choice(list(pecas.values()))
        x = random.randint(0, 10 - peca_atual.shape[1])
        y = 0

    # Checa colisão no topo
    if colisao(tabuleiro, peca_atual, x, y):
        print(f"Game Over! Pontuação final: {pontuacao}")
        ligar_jogo = 'OFF'

    # Controle de movimento e rotação
    if keyboard.is_pressed('left'):
        if not colisao(tabuleiro, peca_atual, x - 1, y):
            x -= 1
    elif keyboard.is_pressed('right'): 
        if colisao(tabuleiro, peca_atual, x + 1, y) == False:
            x += 1
    elif keyboard.is_pressed('up'):
        peca_rotacionada = girar_peca(peca_atual)
        if colisao(tabuleiro, peca_rotacionada, x, y) == False:
            peca_atual = peca_rotacionada