# Jogo da Velha em Python com Pygame

Este é um simples jogo da velha implementado em Python usando a biblioteca Pygame. O jogo permite que dois jogadores joguem alternadamente até que haja um vencedor ou empate.

## Requisitos

- Python 3.x
- Pygame (instalado via `pip install pygame`)

## Como Jogar

1. Clone o repositório ou faça o download dos arquivos em seu computador.

2. Certifique-se de ter o Python e o Pygame instalados corretamente.

3. Abra um terminal ou prompt de comando e navegue até o diretório onde os arquivos do jogo estão localizados.

4. Execute o seguinte comando para iniciar o jogo:
5. O jogo será iniciado em uma nova janela.

6. As marcações no tabuleiro são feitas clicando nas células vazias com o botão esquerdo do mouse. O jogador 'X' sempre começa o jogo.

7. O objetivo é obter três de suas marcas (X ou O) em uma linha horizontal, vertical ou diagonal. O jogo termina quando há um vencedor ou um empate.

8. Após o término de uma partida, você pode reiniciar o jogo clicando em qualquer célula vazia.

## Detalhes de Implementação

O código do jogo é estruturado em uma classe chamada `iniciarJogo`. A classe é responsável por criar a janela do jogo, desenhar o tabuleiro, processar os cliques do mouse e verificar se há um vencedor.

O tabuleiro é representado por uma lista `QUADRANTES` com valores de 1 a 9, onde cada valor representa uma célula do tabuleiro. Inicialmente, todas as células estão vazias.

As marcações 'X' e 'O' são desenhadas na tela usando as funções `pygame.draw.line()` e `pygame.draw.circle()`.

A cada clique do mouse, a função `marcar()` é chamada para verificar qual célula foi clicada e fazer a marcação apropriada. Em seguida, a função `verificar_ganhador()` é chamada para verificar se há um vencedor ou um empate.

Se houver um vencedor ou empate, a função `reiniciar()` é chamada para limpar o tabuleiro e reiniciar o jogo.

## Personalização

Você pode personalizar o jogo de acordo com suas preferências. Por exemplo, pode alterar as cores, o tamanho do tabuleiro, a fonte utilizada ou adicionar recursos adicionais, como sons.

Divirta-se jogando o jogo da velha!

