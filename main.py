import pygame
#ger
# Import the android module. If we can't import it, set it to None - this
# lets us test it, and check to see if we want android-specific behavior.
try:
    import android
except ImportError:
    android = None

# Event constant.
TIMEREVENT = pygame.USEREVENT

# The FPS the game runs at.
FPS = 30

# Color constants.
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
VERDE = 0
AMARELO = 1
VERMELHO = 2
AZUL = 3

# Imagem das cartas
cardsImage = pygame.image.load("cards.jpg")
cardsImage1 = pygame.image.load("cartainv1.jpg")
cardsImage1.subsurface(10, 10, 10, 10)

# Constantes de tamanho de carta
TAMANHO_CARTA_X = 44.4
TAMANHO_CARTA_Y = 68.16

# verifica se dedo esta tocando na tela
isPressed = False

# Classe carta
class Card:
    def __init__(self, i, c, n):
        self.image = i
        self.color = c
        self.number = n
        self.pos = None

def isInArea(mouse, card):
    if mouse[0] > card[0] and mouse[0] < card[0]+TAMANHO_CARTA_X and mouse[1] > card[1] and mouse[1] < card[1]+TAMANHO_CARTA_Y:
        return True
    else:
        return False

def swipeUp(ev):
    if ev.type == pygame.MOUSEBUTTONDOWN:
        pInicial = pygame.mouse.get_pos()[1]
        while ev.type != pygame.MOUSEBUTTONUP:
            ev = pygame.event.wait()
        pFinal = pygame.mouse.get_pos()[1]
        if pFinal < pInicial - 50:
            return True
        else:
            return False
    else:
        return False

#Sintaxe do subsurface(xi, yi, pixelsNaHorizoltalAPartirDeXi,
#pixelsNaVerticalAPartirDeYi)
cards = (
	Card(cardsImage.subsurface(753.1, 340.5, 44.4, 68.16), VERMELHO, 0),
	Card(cardsImage.subsurface(17*TAMANHO_CARTA_X, 5*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERMELHO, 0),
	Card(cardsImage.subsurface(17*TAMANHO_CARTA_X, 4*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERMELHO, 1), 
	Card(cardsImage.subsurface(17*TAMANHO_CARTA_X, 3*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERMELHO, 1),
	Card(cardsImage.subsurface(17*TAMANHO_CARTA_X, 2*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERMELHO, 2),
	Card(cardsImage.subsurface(17*TAMANHO_CARTA_X, 1*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERMELHO, 2),
	Card(cardsImage.subsurface(17*TAMANHO_CARTA_X, 0*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERMELHO, 3),
	Card(cardsImage.subsurface(11*TAMANHO_CARTA_X, 5*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERMELHO, 3),
	Card(cardsImage.subsurface(11*TAMANHO_CARTA_X, 4*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERMELHO, 4),
	Card(cardsImage.subsurface(11*TAMANHO_CARTA_X, 3*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERMELHO, 4),
	Card(cardsImage.subsurface(14*TAMANHO_CARTA_X, 5*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AZUL, 0),
	Card(cardsImage.subsurface(14*TAMANHO_CARTA_X, 4*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AZUL, 1),
	Card(cardsImage.subsurface(14*TAMANHO_CARTA_X, 3*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AZUL, 1),
	Card(cardsImage.subsurface(14*TAMANHO_CARTA_X, 2*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AZUL, 2),
	Card(cardsImage.subsurface(14*TAMANHO_CARTA_X, 1*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AZUL, 2),
	Card(cardsImage.subsurface(14*TAMANHO_CARTA_X, 0*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AZUL, 3),
	Card(cardsImage.subsurface(8*TAMANHO_CARTA_X, 5*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AZUL, 3),
	Card(cardsImage.subsurface(8*TAMANHO_CARTA_X, 4*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AZUL, 4),
	Card(cardsImage.subsurface(8*TAMANHO_CARTA_X, 3*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AZUL, 4),
	Card(cardsImage.subsurface(11*TAMANHO_CARTA_X, 2*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AMARELO,0),
	Card(cardsImage.subsurface(11*TAMANHO_CARTA_X, 1*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AMARELO, 1),
	Card(cardsImage.subsurface(11*TAMANHO_CARTA_X, 0*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AMARELO, 1),
	Card(cardsImage.subsurface(5*TAMANHO_CARTA_X, 5*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AMARELO, 2),
	Card(cardsImage.subsurface(5*TAMANHO_CARTA_X, 4*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AMARELO, 2),
	Card(cardsImage.subsurface(5*TAMANHO_CARTA_X, 3*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AMARELO, 3),
	Card(cardsImage.subsurface(5*TAMANHO_CARTA_X, 2*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AMARELO, 3),
	Card(cardsImage.subsurface(5*TAMANHO_CARTA_X, 1*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AMARELO, 4),
	Card(cardsImage.subsurface(5*TAMANHO_CARTA_X, 0*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), AMARELO, 4),
	Card(cardsImage.subsurface(8*TAMANHO_CARTA_X, 2*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERDE,0),
	Card(cardsImage.subsurface(8*TAMANHO_CARTA_X, 1*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERDE, 1),
	Card(cardsImage.subsurface(8*TAMANHO_CARTA_X, 0*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERDE, 1),
	Card(cardsImage.subsurface(2*TAMANHO_CARTA_X, 5*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERDE, 2),
	Card(cardsImage.subsurface(2*TAMANHO_CARTA_X, 4*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERDE, 2),
	Card(cardsImage.subsurface(2*TAMANHO_CARTA_X, 3*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERDE, 3),
	Card(cardsImage.subsurface(2*TAMANHO_CARTA_X, 2*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERDE, 3),
	Card(cardsImage.subsurface(2*TAMANHO_CARTA_X, 1*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERDE, 4),
	Card(cardsImage.subsurface(2*TAMANHO_CARTA_X, 0*TAMANHO_CARTA_Y, TAMANHO_CARTA_X, TAMANHO_CARTA_Y), VERDE, 4),
    )
for i in range(4):
    for j in range(10):
        if i*10+j < 36:
            cards[i*10+j].pos = (j*TAMANHO_CARTA_X, i*TAMANHO_CARTA_Y)

def main():
    pygame.init()

    # Set the screen size.
    screen = pygame.display.set_mode((480, 800))


    # Map the back button to the escape key.
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

    # Use a timer to control FPS.
    pygame.time.set_timer(TIMEREVENT, 1000 / FPS)

    # The color of the screen.
    color = RED

    while True:


        screen.blit(cardsImage1, (200,400))
        for card in cards:
            if card.pos is not None:
                screen.blit(card.image, card.pos)
        pygame.display.flip()

    	ev = pygame.event.wait()

        # Android-specific:
        if android:
            if android.check_pause():
                android.wait_for_resume()


        # Draw the screen based on the timer.
        if ev.type == TIMEREVENT:
            screen.fill(color)

        # When the touchscreen is pressed, change the color to green.
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            isPressed = True

        # When it's released, change the color to RED.
        elif ev.type == pygame.MOUSEBUTTONUP:
            isPressed = False
            print pygame.MOUSEBUTTONDOWN

        # When the user hits back, ESCAPE is sent. Handle it and end
        # the game.
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
            break

        #movimenta a carta com o dedo
#        if pygame.mouse.get_pressed()[0]:
#            for i in xrange(len(cards)-5):
#                if isInArea(pygame.mouse.get_pos(), cards[i].pos):
#                    cards[i].pos = pygame.mouse.get_pos()

        if swipeUp(ev):
            if color is RED:
                color = GREEN
            else:
                color = RED

# This isn't run on Android.
if __name__ == "__main__":
    main()
