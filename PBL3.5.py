#Autor: João Victor da Paixão Reis Soares Dias
# Componente Curricular: MI Algoritmos
# Concluído em: 07/12/2024, às 23:00
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

# Importação das bibliotecas utilizadas
import re, json, random, time, os

# Dicionários de configurações básicas e de ajudas a serem implementadas
configuracoes = {
    "num_questoes": 15,
    "limite_tempo": 300,
    "acertos_dica": 1,
}

ajudas = {
    "pular_ajuda": True,
    "dica_ajuda": True,
    "eliminar_opcoes_ajuda": True
}

# Função para adicionar aspas ao redor das chaves no texto
def adicionar_aspas_chaves(texto):
    texto_corrigido = re.sub(r'(\w+):', r'"\1":', texto)  # Adiciona aspas nas chaves
    return texto_corrigido

# Função para processar o conteúdo do arquivo, colocando os requisitos necessários para ser transformado em txt
def processar_arquivo(entrada="Banco_de_Questões.txt", saida="1.txt"):
    with open(entrada, 'r', encoding='utf-8') as file:
        conteudo = file.read()
    conteudo_corrigido = adicionar_aspas_chaves(conteudo)
    with open(saida, 'w', encoding='utf-8') as file:
        file.write(conteudo_corrigido)
    print("Arquivo processado com sucesso!")

# Função para converter arquivo txt para JSON, lendo as linhas do arquivo e os transformando em dicionário 
def txt_para_json(caminho_txt="1.txt", caminho_json="Banco_de_Questões.json"):
    with open(caminho_txt, 'r', encoding='utf-8') as arquivo_txt:
        linhas = arquivo_txt.readlines()

    dados = []
    for linha in linhas:
        if ':' in linha:
            chave, valor = linha.strip().split(':', 1)
            dados.append({chave.strip(): valor.strip()})

    with open(caminho_json, 'w', encoding='utf-8') as arquivo_json:
        json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)

# Configuração inicial do Hall da Fama
HALL_OF_FAME_FILE = "hall_of_fame.json"

# Com inicialização
def inicializar_hall_da_fama():
    if not os.path.exists(HALL_OF_FAME_FILE):
        with open(HALL_OF_FAME_FILE, 'w', encoding='utf-8') as f:
            json.dump({"questoes_fixas": [], "limite_tempo": [], "tente_nao_errar": []}, f)

# Carregamento
def carregar_hall_da_fama():
    with open(HALL_OF_FAME_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# Salvamento
def salvar_hall_da_fama(hall_of_fama):
    with open(HALL_OF_FAME_FILE, 'w', encoding='utf-8') as f:
        json.dump(hall_of_fama, f, indent=4)

# E atualização de acordo com os parâmetros de pontos, modo e nome do jogador fornecidos
def atualizar_hall_da_fama(modo, nome, pontuacao):
    hall_of_fama = carregar_hall_da_fama()
    hall_of_fama[modo].append({"nome": nome, "pontuacao": pontuacao})
    hall_of_fama[modo] = sorted(hall_of_fama[modo], key=lambda x: x["pontuacao"], reverse=True)[:10]
    salvar_hall_da_fama(hall_of_fama)

# Sistema de leitura e carregamento de perguntas do arquivo json
def carregar_perguntas(caminho_json):
    with open(caminho_json, 'r', encoding='utf-8') as arquivo_json:
        dados = json.load(arquivo_json)

    perguntas = []
    pergunta_atual = {}
    for item in dados:
        chave, valor = list(item.items())[0]  # Pega a única chave-valor no dicionário
        chave = chave.strip('"')  # Remove as aspas extras da chave
        valor = valor.strip('"')  # Remove as aspas extras do valor

        if chave == "category":
            pergunta_atual["categoria"] = valor
        elif chave == "questionText":
            pergunta_atual["pergunta"] = valor
        elif chave.startswith("option"):
            if "opcoes" not in pergunta_atual:
                pergunta_atual["opcoes"] = []
            pergunta_atual["opcoes"].append(valor)
        elif chave == "answer":
            pergunta_atual["resposta"] = valor
        elif chave == "hint":
            pergunta_atual["dica"] = valor
        elif chave == "explanation":
            pergunta_atual["explicacao"] = valor

        # Finaliza uma pergunta completa e reinicia para a próxima
        if chave == "answer":
            perguntas.append(pergunta_atual)
            pergunta_atual = {}

    return perguntas

# Criação da função para jogar as questões fixas, com os parâmetros de entrada + definição das variáveis
def jogar_questoes_fixas(perguntas, num_questoes):
    print("\nModo: Questões Fixas")
    random.shuffle(perguntas)  # Embaralha as perguntas
    acertos = 0
    pontuacao_total = 0
    pular_ajuda = True
    dica_ajuda = True
    eliminar_opcoes_ajuda = True
    pontos = [10, 20, 30]

    # Seleção aleatória de perguntas + criação do menu de ajudas + validação das respostas
    for i, pergunta in enumerate(perguntas[:num_questoes]):
        print(f"\nPergunta {i + 1}: {pergunta['pergunta']}")
        opcoes = pergunta['opcoes'][:]
        for j, opcao in enumerate(opcoes, start=1):
            print(f"{j}. {opcao}")

        resposta_valida = False
        while not resposta_valida:
            print("\nEscolha uma opção:")
            print("1-5. Responder")
            if pular_ajuda:
                print("P. Pular questão")
            if dica_ajuda:
                print("D. Pedir dica")
            if eliminar_opcoes_ajuda:
                print("E. Eliminar três opções")

            # "Refil" de ajudas a partir de uma pontuação for alcançada
            if pontuacao_total >= 60 and any(not valor for valor in ajudas.values()):  # Verifica se ainda existem ajudas não liberadas
                for chave, valor in ajudas.items():
                    if not valor:  # Se a ajuda ainda não foi liberada
                        ajudas[chave] = True  # Libera essa ajuda
                print(f"A ajuda {chave} foi liberada!")
                return  # Sai da função para garantir que apenas uma ajuda seja liberada

            resposta = input("Escolha: ").upper()
            # Contabilização dos pontos + definição das condições de uso de cada ajuda
            if resposta.isdigit() and 1 <= int(resposta) <= len(opcoes):
                resposta_usuario = opcoes[int(resposta) - 1]
                if resposta_usuario == pergunta['resposta']:
                    print("Correto!")
                    acertos += 1
                    pontuacao = random.choice(pontos)
                    pontuacao_total += pontuacao
                else:
                    print(f"Errado! A resposta correta era: {pergunta['resposta']}")
                resposta_valida = True  # Resposta válida, sai do loop

            elif resposta == "P" and pular_ajuda: # Definição da pulagem de questões
                print("Você pulou a questão.")
                pular_ajuda = False
                resposta_valida = True  # Sai do loop

            elif resposta == "D" and dica_ajuda: # Definição das dicas
                print(f"Dica: {pergunta['dica']}")
                dica_ajuda = False

            elif resposta == "E" and eliminar_opcoes_ajuda: # Definição das eliminações e estruturação da mecânica dela
                eliminar_opcoes_ajuda = False
                opcoes_restantes = [
                    opcao for opcao in opcoes if opcao == pergunta['resposta'] or random.random() > 0.5
                ]
                if len(opcoes_restantes) > 2: 
                    opcoes_restantes = opcoes_restantes[:2]
                print("Opções restantes:")
                for j, opcao in enumerate(opcoes_restantes, start=1):
                    print(f"{j}. {opcao}")
                opcoes = opcoes_restantes

            else:
                print("Opção inválida. Tente novamente.")

    print(f"\nVocê acertou {acertos} questões e acumulou {pontuacao_total} pontos!")
    return pontuacao_total

# Criação da função para o modo de tentar não errar + declaração de variáveis
def jogar_tente_nao_errar(perguntas):
    print("\nModo: Tente Não Errar")
    random.shuffle(perguntas)
    acertos = 0
    pontuacao_total = 0
    pular_ajuda = True
    dica_ajuda = True
    eliminar_opcoes_ajuda = True
    pontos = [10, 20, 30]

    for i, pergunta in enumerate(perguntas): # Laço de repetição para a seleção da pergunta e suas opções
        print(f"\nPergunta {i + 1}: {pergunta['pergunta']}")
        opcoes = pergunta['opcoes'][:]
        for j, opcao in enumerate(opcoes, start=1): # Enumeração das opções
            print(f"{j}. {opcao}")

        resposta_valida = False 
        while not resposta_valida: # Laço para a continuidade e fluidez do jogo
            print("\nEscolha uma opção:") # Menu de ajudas
            print("1-5. Responder")
            if pular_ajuda:
                print("P. Pular questão")
            if dica_ajuda:
                print("D. Pedir dica")
            if eliminar_opcoes_ajuda:
                print("E. Eliminar três opções")

            if pontuacao_total >= 60 and any(not valor for valor in ajudas.values()):  # Verifica se ainda existem ajudas não liberadas
                for chave, valor in ajudas.items():
                    if not valor:  # Se a ajuda ainda não foi liberada
                        ajudas[chave] = True  # Libera essa ajuda
                print(f"A ajuda {chave} foi liberada!")
                return  # Sai da função para garantir que apenas uma ajuda seja liberada

            resposta = input("Escolha: ").upper()

            if resposta.isdigit() and 1 <= int(resposta) <= len(opcoes):
                resposta_usuario = opcoes[int(resposta) - 1]
                if resposta_usuario == pergunta['resposta']:
                    print("Correto!")
                    acertos += 1
                    pontuacao = random.choice(pontos)
                    pontuacao_total += pontuacao
                else:
                    print(f"Errado! A resposta correta era: {pergunta['resposta']}")
                    print("Você perdeu!")
                    return pontuacao_total
                resposta_valida = True  # Resposta válida, sai do loop

            elif resposta == "P" and pular_ajuda:
                print("Você pulou a questão.")
                pular_ajuda = False
                resposta_valida = True  # Sai do loop

            elif resposta == "D" and dica_ajuda:
                print(f"Dica: {pergunta['dica']}")
                dica_ajuda = False

            elif resposta == "E" and eliminar_opcoes_ajuda: # Segue o mesmo padrão da primeira eliminação mostrada
                eliminar_opcoes_ajuda = False
                opcoes_restantes = [
                    opcao for opcao in opcoes if opcao == pergunta['resposta'] or random.random() > 0.5
                ]
                if len(opcoes_restantes) > 2:
                    opcoes_restantes = opcoes_restantes[:2]
                print("Opções restantes:")
                for j, opcao in enumerate(opcoes_restantes, start=1):
                    print(f"{j}. {opcao}")
                opcoes = opcoes_restantes

            else:
                print("Opção inválida. Tente novamente.")

    print(f"\nVocê acertou {acertos} questões e acumulou {pontuacao_total} pontos!")
    return pontuacao_total

# Definição da função do jogo com limite de tempo + definição de variáveis + inicialização do tempo
def jogar_limite_tempo(perguntas, limite_tempo):
    print("\nModo: Limite de Tempo")
    random.shuffle(perguntas)
    acertos = 0
    pontuacao_total = 0
    tempo_inicial = time.time()
    pular_ajuda = True
    dica_ajuda = True
    eliminar_opcoes_ajuda = True
    pontos = [10, 20, 30]

    for i, pergunta in enumerate(perguntas):
        tempo_restante = limite_tempo - (time.time() - tempo_inicial)
        if tempo_restante <= 0:
            print("\nTempo esgotado!")
            return pontuacao_total  # Sai da função se o tempo acabar

        print(f"\nPergunta {i + 1}: {pergunta['pergunta']}")
        opcoes = pergunta['opcoes'][:]
        for j, opcao in enumerate(opcoes, start=1):
            print(f"{j}. {opcao}")

        resposta_valida = False
        while not resposta_valida and tempo_restante > 0:
            print(f"\nTempo restante: {int(tempo_restante)} segundos")
            print("Escolha uma opção:")
            print("1-5. Responder")
            if pular_ajuda:
                print("P. Pular questão")
            if dica_ajuda:
                print("D. Pedir dica")
            if eliminar_opcoes_ajuda:
                print("E. Eliminar duas opções")

            if pontuacao_total >= 60 and any(not valor for valor in ajudas.values()):  # Verifica se ainda existem ajudas não liberadas
                for chave, valor in ajudas.items():
                    if not valor:  # Se a ajuda ainda não foi liberada
                        ajudas[chave] = True  # Libera essa ajuda
                print(f"A ajuda {chave} foi liberada!")
                return  # Sai da função para garantir que apenas uma ajuda seja liberada

            resposta = input("Escolha: ").upper()

            if resposta.isdigit() and 1 <= int(resposta) <= len(opcoes):
                resposta_usuario = opcoes[int(resposta) - 1]
                if resposta_usuario == pergunta['resposta']:
                    print("Correto!")
                    acertos += 1
                    pontuacao = random.choice(pontos)
                    pontuacao_total += pontuacao
                else:
                    print(f"Errado! A resposta correta era: {pergunta['resposta']}")
                resposta_valida = True  # Resposta válida, sai do loop

            elif resposta == "P" and pular_ajuda:
                print("Você pulou a questão.")
                pular_ajuda = False
                resposta_valida = True  # Resposta válida, sai do loop

            elif resposta == "D" and dica_ajuda:
                print(f"Dica: {pergunta['dica']}")
                dica_ajuda = False

            elif resposta == "E" and eliminar_opcoes_ajuda:
                eliminar_opcoes_ajuda = False
                opcoes_restantes = [
                    opcao for opcao in opcoes if opcao == pergunta['resposta'] or random.random() > 0.5
                ]
                if len(opcoes_restantes) > 2:
                    opcoes_restantes = opcoes_restantes[:2]
                print("Opções restantes:")
                for j, opcao in enumerate(opcoes_restantes, start=1):
                    print(f"{j}. {opcao}")
                opcoes = opcoes_restantes

            # Condicional de "refil" de perguntas com base na pontuação e verificação de erros de entrada
            elif pontuacao == 60:
                for chave, valor in ajudas.items():
                    if not valor:  # Se o valor for False
                         ajudas[chave] = True  # Muda para True

            else:
                print("Opção inválida. Tente novamente.")

            # Atualiza o tempo restante
            tempo_restante = limite_tempo - (time.time() - tempo_inicial)
            if tempo_restante <= 0:
                print("\nTempo esgotado!")
                return pontuacao_total  # Sai da função se o tempo acabar

    print(f"\nVocê acertou {acertos} questões e acumulou {pontuacao_total} pontos!")
    return pontuacao_total

# Modo de tente não errar e definição das variáveis iniciais

# Código principal

# Menu de inicialização do jogo
inicializar_hall_da_fama()
print("Olá, seja bem vindo ao AskMe!")
perguntas = carregar_perguntas("Banco_de_Questões.json")

print("\nEscolha o modo de jogo:")
print("1. Questões Fixas")
print("2. Limite de Tempo")
print("3. Tente Não Errar")
print("4. Ver Hall da Fama")

modo = input("Escolha (1-4): ")

# Condicionais de escolha do jogo

# Modo de questões fixas e definição de pontuação para entrar no hall da fama
if modo == "1":
    pontuacao = jogar_questoes_fixas(perguntas, configuracoes["num_questoes"])
    if pontuacao >= 120:
        nome_jogador = input("Digite seu nome: ")
        atualizar_hall_da_fama("questoes_fixas", nome_jogador, pontuacao)

# Modo de mais questões com limite de tempo e definição de pontuação para entrar no hall da fama
elif modo == "2":
    pontuacao = jogar_limite_tempo(perguntas, configuracoes["limite_tempo"])
    if pontuacao >= 120:
        nome_jogador = input("Digite seu nome: ")
        atualizar_hall_da_fama("questoes_fixas", nome_jogador, pontuacao)

# Modo de tente não errar e definição de pontuação para entrar no hall da fama
elif modo == "3":
    pontuacao = jogar_tente_nao_errar(perguntas)
    if pontuacao >= 120:
        nome_jogador = input("Digite seu nome: ")
        atualizar_hall_da_fama("questoes_fixas", nome_jogador, pontuacao)

# Visita ao hall da fama
elif modo == "4":
    print("\nHall da Fama:")
    hall_of_fama = carregar_hall_da_fama()
    for modo, jogadores in hall_of_fama.items():
        print(f"\n{modo.capitalize()}:")
        for jogador in jogadores:
            print(f"{jogador['nome']} - {jogador['pontuacao']} pontos")
else:
    print("Modo inválido.")
