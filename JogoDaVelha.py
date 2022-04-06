import sys
import time

import pygame

pygame.init()

size = width, height = 300, 300
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.display.set_caption("Jogo da velha")

class iniciarJogo:
    RODADA = 1
    QUADRANTES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        self.screen = pygame.display.set_mode(size)

        pygame.draw.line(self.screen, WHITE, (100, 0), (100, 300))
        pygame.draw.line(self.screen, WHITE, (200, 0), (200, 300))
        pygame.draw.line(self.screen, WHITE, (0, 100), (300, 100))
        pygame.draw.line(self.screen, WHITE, (0, 200), (300, 200))

    def marcar(self, pos):
        if 0 < pos[0] < 100 and 0 < pos[1] < 100:
            if self.QUADRANTES[1] == 1:
                if self.RODADA % 2:
                    pygame.draw.line(self.screen, WHITE, (0, 0), (100, 100))
                    pygame.draw.line(self.screen, WHITE, (0, 100), (100, 0))
                    self.QUADRANTES[1] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(self.screen, WHITE, (50, 50), 20)
                    self.QUADRANTES[1] = 'o'
                    self.RODADA += 1
        elif 200 > pos[0] > 100 > pos[1] > 0:
            if self.QUADRANTES[2] == 2:
                if self.RODADA % 2:
                    pygame.draw.line(self.screen, WHITE, (100, 0), (200, 100))
                    pygame.draw.line(self.screen, WHITE, (100, 100), (200, 0))
                    self.QUADRANTES[2] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(self.screen, WHITE, (150, 50), 20)
                    self.QUADRANTES[2] = 'o'
                    self.RODADA += 1

        elif 200 < pos[0] < 300 and 0 < pos[1] < 100:
            if self.QUADRANTES[3] == 3:
                if self.RODADA % 2:
                    pygame.draw.line(self.screen, WHITE, (200, 0), (300, 100))
                    pygame.draw.line(self.screen, WHITE, (200, 100), (300, 0))
                    self.QUADRANTES[3] = 'x'
                    self.RODADA += 1
                else:
                    pygame.draw.circle(self.screen, WHITE, (250, 50), 20)
                    self.QUADRANTES[3] = 'o'
                    self.RODADA += 1
        elif 0 < pos[0] < 100 < pos[1] < 200:
            if self.QUADRANTES[4] == 4:
                if self.RODADA % 2:
                    pygame.draw.line(self.screen, WHITE, (0, 100), (100, 200))
                    pygame.draw.line(self.screen, WHITE, (0, 200), (100, 100))
                    self.QUADRANTES[4] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(self.screen, WHITE, (50, 150), 20)
                    self.QUADRANTES[4] = 'o'
                    self.RODADA += 1
        elif 100 < pos[0] < 200 and 100 < pos[1] < 200:
            if self.QUADRANTES[5] == 5:
                if self.RODADA % 2:
                    pygame.draw.line(self.screen, WHITE, (100, 100), (200, 200))
                    pygame.draw.line(self.screen, WHITE, (100, 200), (200, 100))
                    self.QUADRANTES[5] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(self.screen, WHITE, (150, 150), 20)
                    self.QUADRANTES[5] = 'o'
                    self.RODADA += 1
        elif 300 > pos[0] > 200 > pos[1] > 100:
            if self.QUADRANTES[6] == 6:
                if self.RODADA % 2:
                    pygame.draw.line(self.screen, WHITE, (200, 100), (300, 200))
                    pygame.draw.line(self.screen, WHITE, (200, 200), (300, 100))
                    self.QUADRANTES[6] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(self.screen, WHITE, (250, 150), 20)
                    self.QUADRANTES[6] = 'o'
                    self.RODADA += 1
        elif 0 < pos[0] < 100 and 200 < pos[1] < 300:
            if self.QUADRANTES[7] == 7:
                if self.RODADA % 2:
                    pygame.draw.line(self.screen, WHITE, (0, 200), (100, 300))
                    pygame.draw.line(self.screen, WHITE, (0, 300), (100, 200))
                    self.QUADRANTES[7] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(self.screen, WHITE, (50, 250), 20)
                    self.QUADRANTES[7] = 'o'
                    self.RODADA += 1
        elif 100 < pos[0] < 200 < pos[1] < 300:
            if self.QUADRANTES[8] == 8:
                if self.RODADA % 2:
                    pygame.draw.line(self.screen, WHITE, (100, 200), (200, 300))
                    pygame.draw.line(self.screen, WHITE, (100, 300), (200, 200))
                    self.QUADRANTES[8] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(self.screen, WHITE, (150, 250), 20)
                    self.QUADRANTES[8] = 'o'
                    self.RODADA += 1
        elif 200 < pos[0] < 300 and 200 < pos[1] < 300:
            if self.QUADRANTES[9] == 9:
                if self.RODADA % 2:
                    pygame.draw.line(self.screen, WHITE, (200, 200), (300, 300))
                    pygame.draw.line(self.screen, WHITE, (200, 300), (300, 200))
                    self.QUADRANTES[9] = 'x'
                    self.RODADA += 1
                else:
                    pygame.draw.circle(self.screen, WHITE, (250, 250), 20)
                    self.QUADRANTES[9] = 'o'
                    self.RODADA += 1

    def verficar_ganhador(self):
            if self.QUADRANTES[1] == self.QUADRANTES[2] == self.QUADRANTES[3]:
                print(self.QUADRANTES[1], self.QUADRANTES[4])
                return True
            elif self.QUADRANTES[4] == self.QUADRANTES[5] == self.QUADRANTES[6]:
                 print('ganhador')
                 return True
            elif self.QUADRANTES[7] == self.QUADRANTES[8] == self.QUADRANTES[9]:
                print('ganhador')
                return True
            elif self.QUADRANTES[1] == self.QUADRANTES[4] == self.QUADRANTES[7]:
                print('ganhador')
                return True
            elif self.QUADRANTES[2] == self.QUADRANTES[5] == self.QUADRANTES[8]:
                print('ganhador')
                return True
            elif self.QUADRANTES[3] == self.QUADRANTES[6] == self.QUADRANTES[9]:
                print('ganhador')
                return True
            elif self.QUADRANTES[1] == self.QUADRANTES[5] == self.QUADRANTES[9]:
                print('ganhador')
                return True
            elif self.QUADRANTES[7] == self.QUADRANTES[5] == self.QUADRANTES[3]:
                print('ganhador')
                return True
            elif self.RODADA == 10:
                print('Empate')
                return True

    def reiniciar(self):
        self.QUADRANTES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.RODADA = 1
        pygame.display.set_caption("Jogo da velha jogador x")
        jogodavelha = iniciarJogo()



jogodavelha = iniciarJogo()


while 1:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            jogodavelha.marcar(pos)
            if jogodavelha.verficar_ganhador():
                pygame.display.update()
                pygame.display.update()
                jogodavelha.reiniciar()

    pygame.display.update()