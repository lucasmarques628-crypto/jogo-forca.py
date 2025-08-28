import random  # Importa o módulo random para gerar escolhas aleatórias

# ASCII art da forca, cada elemento é um estágio do boneco na forca
HANGMAN_STAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# Lista de palavras possíveis para o jogo
WORDS = ['python','programador','computador','barbearia','chave','janela','carro','teclado','monitor','internet','algoritmo','variavel']

# Função para escolher palavra aleatória
def escolher_palavra(palavras):
    """
    random.choice(lista) escolhe um elemento aleatório da lista
    .lower() transforma a palavra em minúsculas
    """
    return random.choice(palavras).lower()

# Função principal do jogo
def jogar():
    palavra = escolher_palavra(WORDS)  # Palavra secreta
    letras_descobertas = ['_' for _ in palavra]  # Cria lista de underscores do tamanho da palavra
    erros = 0  # Contador de erros
    letras_usadas = set()  # Conjunto para checar letras já usadas
    letras_erradas = []  # Lista para guardar letras erradas separadamente
    max_erros = len(HANGMAN_STAGES) - 1  # Número máximo de erros antes de perder

    # Loop do jogo, enquanto não houver vitória ou derrota
    while True:
        print(HANGMAN_STAGES[erros])  # Mostra a forca correspondente ao número de erros
        print('\nPalavra: ' + ' '.join(letras_descobertas))  # Mostra a palavra com letras descobertas e underscores
        print('Letras erradas: ' + ', '.join(letras_erradas))  # Mostra as letras erradas separadas
        # Barra de progresso da palavra: mostra quantas letras já foram descobertas
        progresso = int(((len([l for l in letras_descobertas if l != '_']) / len(palavra)) * 20))
        print('Progresso: [' + '#' * progresso + '-' * (20 - progresso) + ']')  # # = letras descobertas, - = restantes

        # Pede uma letra ao usuário
        chute = input('\nDigite uma letra: ').strip().lower()  # .strip() remove espaços, .lower() minúscula

        # Validação: garante que o chute seja apenas uma letra
        if not chute or len(chute) != 1 or not chute.isalpha():
            print('Por favor, digite apenas UMA letra (a-z).')
            continue  # Volta para o começo do while

        # Checa se letra já foi usada
        if chute in letras_usadas:
            print('Você já tentou essa letra. Tente outra.')
            continue  # Volta para o começo do while

        letras_usadas.add(chute)  # Adiciona ao conjunto de letras usadas

        # Se letra correta
        if chute in palavra:
            for i, c in enumerate(palavra):  # Percorre cada letra da palavra
                if c == chute:
                    letras_descobertas[i] = chute  # Revela a letra na posição correta
            print(f'Boa! A letra "{chute}" está na palavra!')
        else:  # Se letra incorreta
            erros += 1  # Incrementa o número de erros
            letras_erradas.append(chute)  # Adiciona a letra à lista de letras erradas
            print(f'Errou! A letra "{chute}" não está na palavra. Restam {max_erros - erros} tentativas.')

        # Checa vitória
        if '_' not in letras_descobertas:
            print('\nParabéns — você ganhou! 🎉')
            print('A palavra era:', palavra)
            break  # Sai do loop

        # Checa derrota
        if erros >= max_erros:
            print(HANGMAN_STAGES[erros])  # Mostra a forca completa
            print('\nVocê perdeu. 😢')
            print('A palavra era:', palavra)
            break  # Sai do loop

# Loop externo para permitir jogar novamente
while True:
    jogar()  # Chama a função jogar

    # Pergunta ao usuário se deseja jogar novamente
    print("\nDeseja jogar novamente?")
    print("1 - Sim")
    print("2 - Não")
    resposta = input("Digite 1 ou 2: ").strip()  # Remove espaços extras

    # Estrutura de decisão:
    # if: condição verdadeira executa este bloco
    if resposta == "1":
        continue  # Reinicia o loop, o jogo recomeça
    # elif: "else if", executa se o if anterior não for verdadeiro
    elif resposta == "2":
        print("Obrigado por jogar! Até a próxima! 👋")
        break  # Sai do loop, encerra o programa
    # else: executa se nenhuma das condições anteriores for verdadeira
    else:
        print("Resposta inválida. Saindo do jogo.")
        break  # Encerra o programa


