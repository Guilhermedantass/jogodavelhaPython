import sys

import pygame

pygame.init()

size = width, height = 300, 300
speed = [2, 2]

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Jogo da velha")

pygame.draw.line(screen, WHITE, (100, 0), (100, 300))
pygame.draw.line(screen, WHITE, (200, 0), (200, 300))
pygame.draw.line(screen, WHITE, (0, 100), (300, 100))
pygame.draw.line(screen, WHITE, (0, 200), (300, 200))


class JogoDaVelha:
    RODADA = 1
    QUADRANTES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def marcar(self, pos):
        if 0 < pos[0] < 100 and 0 < pos[1] < 100:
            print('quadrante 1')
            if self.QUADRANTES[1] == 1:
                if self.RODADA % 2:
                    pygame.draw.line(screen, WHITE, (0, 0), (100, 100))
                    pygame.draw.line(screen, WHITE, (0, 100), (100, 0))
                    self.QUADRANTES[1] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(screen, WHITE, (50, 50), 20)
                    self.QUADRANTES[1] = 'o'
                    self.RODADA += 1
        elif 200 > pos[0] > 100 > pos[1] > 0:
            print('quadrante 2')
            if self.QUADRANTES[2] == 2:
                if self.RODADA % 2:
                    pygame.draw.line(screen, WHITE, (100, 0), (200, 100))
                    pygame.draw.line(screen, WHITE, (100, 100), (200, 0))
                    self.QUADRANTES[2] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(screen, WHITE, (150, 50), 20)
                    self.QUADRANTES[2] = 'o'
                    self.RODADA += 1

        elif 200 < pos[0] < 300 and 0 < pos[1] < 100:
            print('quadrante 3')
            if self.QUADRANTES[3] == 3:
                if self.RODADA % 2:
                    pygame.draw.line(screen, WHITE, (200, 0), (300, 100))
                    pygame.draw.line(screen, WHITE, (200, 100), (300, 0))
                    self.QUADRANTES[3] = 'x'
                    self.RODADA += 1
                else:
                    pygame.draw.circle(screen, WHITE, (250, 50), 20)
                    self.QUADRANTES[3] = 'o'
                    self.RODADA += 1
        elif 0 < pos[0] < 100 < pos[1] < 200:
            print('quadrante 4')
            if self.QUADRANTES[4] == 4:
                if self.RODADA % 2:
                    pygame.draw.line(screen, WHITE, (0, 100), (100, 200))
                    pygame.draw.line(screen, WHITE, (0, 200), (100, 100))
                    self.QUADRANTES[4] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(screen, WHITE, (50, 150), 20)
                    self.QUADRANTES[4] = 'o'
                    self.RODADA += 1
        elif 100 < pos[0] < 200 and 100 < pos[1] < 200:
            print('quadrante 5')
            if self.QUADRANTES[5] == 5:
                if self.RODADA % 2:
                    pygame.draw.line(screen, WHITE, (100, 100), (200, 200))
                    pygame.draw.line(screen, WHITE, (100, 200), (200, 100))
                    self.QUADRANTES[5] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(screen, WHITE, (150, 150), 20)
                    self.QUADRANTES[5] = 'o'
                    self.RODADA += 1
        elif 300 > pos[0] > 200 > pos[1] > 100:
            print('quadrante 6')
            if self.QUADRANTES[6] == 6:
                if self.RODADA % 2:
                    pygame.draw.line(screen, WHITE, (200, 100), (300, 200))
                    pygame.draw.line(screen, WHITE, (200, 200), (300, 100))
                    self.QUADRANTES[6] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(screen, WHITE, (250, 150), 20)
                    self.QUADRANTES[6] = 'o'
                    self.RODADA += 1
        elif 0 < pos[0] < 100 and 200 < pos[1] < 300:
            print('quadrante 7')
            if self.QUADRANTES[7] == 7:
                if self.RODADA % 2:
                    pygame.draw.line(screen, WHITE, (0, 200), (100, 300))
                    pygame.draw.line(screen, WHITE, (0, 300), (100, 200))
                    self.QUADRANTES[7] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(screen, WHITE, (50, 250), 20)
                    self.QUADRANTES[7] = 'o'
                    self.RODADA += 1
        elif 100 < pos[0] < 200 < pos[1] < 300:
            print('quadrante 8')
            if self.QUADRANTES[8] == 8:
                if self.RODADA % 2:
                    pygame.draw.line(screen, WHITE, (100, 200), (200, 300))
                    pygame.draw.line(screen, WHITE, (100, 300), (200, 200))
                    self.QUADRANTES[8] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(screen, WHITE, (150, 250), 20)
                    self.QUADRANTES[8] = 'o'
                    self.RODADA += 1
        elif 200 < pos[0] < 300 and 200 < pos[1] < 300:
            print('quadrante 9')
            if self.QUADRANTES[9] == 9:
                if self.RODADA % 2:
                    pygame.draw.line(screen, WHITE, (200, 200), (300, 300))
                    pygame.draw.line(screen, WHITE, (200, 300), (300, 200))
                    self.QUADRANTES[9] = 'x'
                    self.RODADA += 1

                else:
                    pygame.draw.circle(screen, WHITE, (250, 250), 20)
                    self.QUADRANTES[9] = 'o'
                    self.RODADA += 1

    def verficar_ganhador(self):
            if self.QUADRANTES[1] == self.QUADRANTES[2] == self.QUADRANTES[3]:
                print('ganhador')
            elif self.QUADRANTES[4] == self.QUADRANTES[5] == self.QUADRANTES[6]:
                 print('ganhador')
            elif self.QUADRANTES[7] == self.QUADRANTES[8] == self.QUADRANTES[9]:
                print('ganhador')
            elif self.QUADRANTES[1] == self.QUADRANTES[4] == self.QUADRANTES[7]:
                print('ganhador')
            elif self.QUADRANTES[2] == self.QUADRANTES[5] == self.QUADRANTES[8]:
                print('ganhador')
            elif self.QUADRANTES[3] == self.QUADRANTES[6] == self.QUADRANTES[9]:
                print('ganhador')
            elif self.QUADRANTES[1] == self.QUADRANTES[5] == self.QUADRANTES[9]:
                print('ganhador')
            elif self.QUADRANTES[7] == self.QUADRANTES[5] == self.QUADRANTES[3]:
                print('ganhador')


jogodavelha = JogoDaVelha()

while 1:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            jogodavelha.marcar(pos)
            jogodavelha.verficar_ganhador()