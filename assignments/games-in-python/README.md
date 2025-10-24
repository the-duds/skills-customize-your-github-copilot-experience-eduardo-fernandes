
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objetivo

Construa o jogo clássico Hangman (Forca) em Python para praticar manipulação de strings, laços, condicionais e entrada do usuário. O aluno deverá implementar a lógica do jogo, apresentação do progresso e controle de tentativas.

## 📝 Tarefas

### 🛠️ Hangman Game

#### Description
Implemente um jogo de Hangman onde o programa escolhe uma palavra aleatória e o jogador tenta adivinhar letra por letra antes de esgotar as tentativas.

#### Requirements
Completed program should:

- Selecionar palavras aleatoriamente de uma lista pré-definida (ou de um arquivo opcional `words.txt`).
- Aceitar palpites de letra do usuário e mostrar o progresso atual no formato _ _ _ (underscore para letras não adivinhadas).
- Rastrear o número de palpites incorretos restantes e mostrar ao jogador.
- Encerrar quando a palavra for totalmente descoberta ou quando as tentativas se esgotarem.
- Exibir mensagens claras de vitória ou derrota e oferecer a opção de jogar novamente.

Exemplo de exibição durante o jogo:

```
Palavra: _ a _ _ _
Letras erradas: a, e
Tentativas restantes: 4
Digite uma letra: 
```

### 🛠️ Optional: Melhorias e Extensões

#### Description
Adicione uma ou mais melhorias para tornar o desafio mais avançado.

#### Requirements

- Carregar palavras a partir de um arquivo `words.txt` na pasta da tarefa.
- Implementar pontuação ou modo com dicas.
- Tratar entradas inválidas (mais de uma letra, caracteres não alfabéticos) com mensagens amigáveis.
- (Opcional) Implementar uma interface gráfica simples usando `tkinter` ou similar.

## Onde começar

Use o arquivo de início `starter-code.py` dentro desta pasta como ponto de partida. Garanta que o programa rode em Python 3.8+.

---

Arquivo(s) de suporte:

- `starter-code.py` — código inicial fornecido na pasta `assignments/games-in-python/`.
- (opcional) `words.txt` — lista de palavras para o jogo.

Boa sorte — divirta-se codando!
