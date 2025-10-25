# Autor: João Victor da Paixão Reis Soares Dias
# Componente Curricular: MI Algoritmos
# Concluído em: 15/09/2024, às 23:00
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

# Apresentação do sistema
print("Sejam bem vindos ao sistema de notas!")

print("Por favor, insira o valor da dificuldade de cada tipo de questão.")
valor_questoes_faceis = int(input("Digite o valor para as questões fáceis: "))
valor_questoes_medias = int(input("Digite o valor para as questões médias: "))
valor_questoes_dificeis = int(input("Digite o valor para as questões difíceis: "))


# Equipe 1
e1 = ''
qf1 = 0
qm1 = 0
qd1 = 0
t1 = 0
pe1 = 0

# Equipe 2
e2 = ''
qf2 = 0
qm2 = 0
qd2 = 0
t2 = 0
pe2 = 0

# Equipe 3
e3 = ''
qf3 = 0
qm3 = 0
qd3 = 0
t3 = 0
pe3 = 0

# Equipe 4
e4 = ''
qf4 = 0
qm4 = 0
qd4 = 0
t4 = 0
pe4 = 0

# Equipe 5
e5 = ''
qf5 = 0
qm5 = 0
qd5 = 0
t5 = 0
pe5 = 0

# Questoes dificeis
maisDificeis = 0
equipeMaisDificeis = ''

# Inserindo informações com laço de repetição
for i in range(1,6):
    equipe = str(input(f"Insira o nome da equipe {i}: "))
    questoes_faceis = int(input("Digite a quantidade de questões fáceis: "))
    questoes_medias = int(input("Digite a quantidade de questões médias: "))
    questoes_dificeis = int(input("Digite a quantidade de questões difíceis: "))
    tempo = int(input("Digite o tempo (em minutos) percorrido até o fim da tarefa: "))
    pontuacao = (questoes_faceis * valor_questoes_faceis) + (questoes_medias * valor_questoes_medias) 
    + (questoes_dificeis * valor_questoes_dificeis)

    # Estabelecendo rankeamento
    if questoes_dificeis > maisDificeis:
        maisDificeis = questoes_dificeis
        equipeMaisDificeis = equipe

    if pontuacao > pe1 or pontuacao == pe1 and (questoes_dificeis > qd1 or (questoes_dificeis == qd1 and tempo < t1)):
        e1, e2, e3, e4, e5 = equipe, e1, e2, e3, e4
        qf1, qf2, qf3, qf4, qf5 = questoes_faceis, qf1, qf2, qf3, qf4
        qm1, qm2, qm3, qm4, qm5 = questoes_medias, qm1, qm2, qm3, qm4
        qd1, qd2, qd3, qd4, qd5 = questoes_dificeis, qd1, qd2, qd3, qd4
        t1, t2, t3, t4, t5 = tempo, t1, t2, t3, t4
        pe1, pe2, pe3, pe4, pe5 = pontuacao, pe1, pe2, pe3, pe4

    elif pontuacao > pe2 or pontuacao == pe2 and (questoes_dificeis > qd2 or (questoes_dificeis == qd2 and tempo < t2)):
        e1, e2, e3, e4, e5 = e1, equipe, e2, e3, e4
        qf1, qf2, qf3, qf4, qf5 = qf1, questoes_faceis, qf2, qf3, qf4
        qm1, qm2, qm3, qm4, qm5 = qm1, questoes_medias, qm2, qm3, qm4
        qd1, qd2, qd3, qd4, qd5 = qd1, questoes_dificeis, qd2, qd3, qd4
        t1, t2, t3, t4, t5 = t1, tempo, t2, t3, t4
        pe1, pe2, pe3, pe4, pe5 = pe1, pontuacao, pe2, pe3, pe4

    elif pontuacao > pe3 or pontuacao == pe3 and (questoes_dificeis > qd3 or (questoes_dificeis == qd3 and tempo < t3)):
        e1, e2, e3, e4, e5 = e1, e2, equipe, e3, e4
        qf1, qf2, qf3, qf4, qf5 = qf1, qf2, questoes_faceis, qf3, qf4
        qm1, qm2, qm3, qm4, qm5 = qm1, qm2, questoes_medias, qm3, qm4
        qd1, qd2, qd3, qd4, qd5 = qd1, qd2, questoes_dificeis, qd3, qd4
        t1, t2, t3, t4, t5 = t1, t2, tempo, t3, t4
        pe1, pe2, pe3, pe4, pe5 = pe1, pe2, pontuacao, pe3, pe4

    elif pontuacao > pe4 or pontuacao == pe4 and (questoes_dificeis > qd4 or (questoes_dificeis == qd4 and tempo < t4)):
        e1, e2, e3, e4, e5 = e1, e2, e3, equipe, e4
        qf1, qf2, qf3, qf4, qf5 = qf1, qf2, qf3, questoes_faceis, qf4
        qm1, qm2, qm3, qm4, qm5 = qm1, qm2, qm3, questoes_medias, qm4
        qd1, qd2, qd3, qd4, qd5 = qd1, qd2, qd3, questoes_dificeis, qd4
        t1, t2, t3, t4, t5 = t1, t2, t3, tempo, t4
        pe1, pe2, pe3, pe4, pe5 = pe1, pe2, pe3, pontuacao, pe4
    
    else:
        e1, e2, e3, e4, e5 = e1, e2, e3, e4, equipe
        qf1, qf2, qf3, qf4, qf5 = qf1, qf2, qf3, qf4, questoes_faceis
        qm1, qm2, qm3, qm4, qm5 = qm1, qm2, qm3, qm4, questoes_medias
        qd1, qd2, qd3, qd4, qd5 = qd1, qd2, qd3, qd4, questoes_dificeis
        t1, t2, t3, t4, t5 = t1, t2, t3, t4, tempo
        pe1, pe2, pe3, pe4, pe5 = pe1, pe2, pe3, pe4, pontuacao

print('\t-----------------------RANKING GERAL-----------------------')
print()
print ('-----------------------------------------------------------------------------------------------------------------')
print("|\tRank\t|\tEqp\t|\tPont.\t|\tQuesF\t|\tQuesM\t|\tQuesD\t|\tTemp\t|")
print(f'|\t1º\t|\t{e1}\t|\t{pe1}\t|\t{qf1}\t|\t{qm1}\t|\t{qd1}\t|\t{t1}\t|')
print(f'|\t2º\t|\t{e2}\t|\t{pe2}\t|\t{qf2}\t|\t{qm2}\t|\t{qd2}\t|\t{t2}\t|')
print(f'|\t3º\t|\t{e3}\t|\t{pe3}\t|\t{qf3}\t|\t{qm3}\t|\t{qd3}\t|\t{t3}\t|')
print(f'|\t4º\t|\t{e4}\t|\t{pe4}\t|\t{qf4}\t|\t{qm4}\t|\t{qd4}\t|\t{t4}\t|')
print(f'|\t5º\t|\t{e5}\t|\t{pe5}\t|\t{qf5}\t|\t{qm5}\t|\t{qd5}\t|\t{t5}\t|')
print ('-----------------------------------------------------------------------------------------------------------------')
print()

print(f'Parabéns, a equipe "{e1}" é a vencedora, com {pe1} pontos e em {t1} minutos!')

# Cálculo da média de pontos por equipe

media = (pe1 + pe2 + pe3 + pe4 + pe5)/5
print(f'A média de pontos por equipe é {media}')
print(f' A equipe {equipeMaisDificeis} que fez mais questões difíceis: {maisDificeis} questões')