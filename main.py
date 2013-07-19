import pygame
import random

# Import the android module. If we can't import it, set it to None - this
# lets us test it, and check to see if we want android-specific behavior.
try:
    import android
except ImportError:
    android = None

# Classe carta
class Card:
    def __init__(self, i, c, n):
        self.image = i
        self.color = c
        self.number = n
        self.pos = None

# Constantes de tamanho de carta
TAMANHO_CARTA_X = 44.4
TAMANHO_CARTA_Y = 68.16

# Imagem das cartas
cardsImage = pygame.image.load("cards.jpg")
verso = pygame.image.load("cartainv1.jpg")
miniVerso = pygame.transform.scale(verso, (int(0.8*TAMANHO_CARTA_X),
                                   int(0.8*TAMANHO_CARTA_Y)))
background = pygame.image.load("table.jpg")
back = pygame.transform.scale(background, (480,800))

# Color constants.
RED = (255, 0, 0, 255)
GREEN = (0, 255, 0, 255)
VERDE = 0
AMARELO = 1
VERMELHO = 2
AZUL = 3

#Numero de jogadores
NUM_PLAYERS = 2

#Sintaxe do subsurface(xi, yi, pixelsNaHorizoltalAPartirDeXi,
#pixelsNaVerticalAPartirDeYi)
#Definicao de lista com todas as cartas
cards = [
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
    ]

buyDeck = []
throwDeck = []

BUYDECK_POS = (260, 300) 
BUYDECK_WIDTH = 72 
BUYDECK_HEIGHT = 118

#imagem da carta selecionada
selectedCard = None

# Event constant.
TIMEREVENT = pygame.USEREVENT

# The FPS the game runs at.
FPS = 30

# Definindo players
class Player:
    def __init__(self, vez):
        self.cards = list()
        self.myturn = vez

# Retorna True se o clique do mouse esta dentro da area da carta passada
def isInArea(mouse, card, width, height):
    if mouse[0] > card[0] and mouse[0] < card[0]+width and mouse[1] > card[1] and mouse[1] < card[1]+height:
        return True
    else:
        return False

def swipeUp(ev):
    if ev.type == pygame.MOUSEBUTTONDOWN:
        pInicial = pygame.mouse.get_pos()[1]
        while ev.type != pygame.MOUSEBUTTONUP:
            ev = pygame.event.wait()
        pFinal = pygame.mouse.get_pos()[1]
        if pFinal < pInicial - 100:
            return True
        else:
            return False
    else:
        return False

for i in range(4):
    for j in range(10):
        if i*10+j < 36:
            cards[i*10+j].pos = (j*TAMANHO_CARTA_X, i*TAMANHO_CARTA_Y)

player = list()
for i in range(NUM_PLAYERS):
    if i is 0:
        player.append(Player(True))
    else:
        player.append(Player(False))
        

#Funcao de distribuicao de cartas
for i in range(len(player)):
    for j in range(7):
        index = random.randint(0,len(cards)-1)
        player[i].cards.append(cards.pop(index))

#Distribui randomicamente pro monte de compra
for i in xrange(len(cards)):
    buyDeck.append(cards.pop(random.randint(0,len(cards)-1)))

def compraCarta():
    if isInArea(pygame.mouse.get_pos(), BUYDECK_POS, BUYDECK_WIDTH,BUYDECK_HEIGHT):
        if len(buyDeck) > 0:
            player[0].cards.append(buyDeck.pop())

def drawThrowDeck(screen):
    screen.blit(pygame.transform.scale(throwDeck[len(throwDeck)-1].image,
                                       (BUYDECK_WIDTH, BUYDECK_HEIGHT)),
                (BUYDECK_POS[0]-BUYDECK_WIDTH-50,BUYDECK_POS[1]))

def drawPlayerCards(screen):
    posicaoCartas = 480/len(player[0].cards)
    for i in xrange(len(player[0].cards)):
        player[0].cards[i].pos = (i*posicaoCartas, 720)
        screen.blit(player[0].cards[i].image, player[0].cards[i].pos)

def main():
    pygame.init()

    # Set the screen size.  
    screen = pygame.display.set_mode((480, 800))

    #Definicao de texto
    myFont = pygame.font.Font(None, 30)
    texto = myFont.render(str(len(player[0].cards)), 1,(255,255,0))

    # Map the back button to the escape key.
    if android:
        android.init()
        android.map_key(android.KEYCODE_BACK, pygame.K_ESCAPE)

    # Use a timer to control FPS.
    pygame.time.set_timer(TIMEREVENT, 1000 / FPS)

    # The color of the screen.
    #color = RED

    # Inicializar o monte de descartes
    throwDeck.append(buyDeck.pop())

    while True:
        #Desenha tela
        screen.blit(back, (0, 0))
        screen.blit(texto, (285,97))
        screen.blit(verso, BUYDECK_POS)
        screen.blit(miniVerso, (240, 80))
        drawPlayerCards(screen)
        drawThrowDeck(screen)
        
        #Desenha carta selecionada
        if selectedCard != None:
            screen.blit(selectedCard, (0,0))
        pygame.display.flip()
        
        #espera por evento
    	ev = pygame.event.wait()

        # Android-specific:
        if android:
            if android.check_pause():
                android.wait_for_resume()


        # Draw the screen based on the timer.
        #if ev.type == TIMEREVENT:
            #screen.fill(color)

        # When the touchscreen is pressed, change the color to green.
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            compraCarta()
#            for card in player[0].cards:
#                if isInArea(pygame.mouse.get_pos, card.pos, TAMANHO_CARTA_X,
#                            TAMANHO_CARTA_Y)


        # When it's released, change the color to RED.
        elif ev.type == pygame.MOUSEBUTTONUP:   
            None

        # When the user hits back, ESCAPE is sent. Handle it and end
        # the game.
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
            break
	
	#movimenta carta com o dedo
#        if pygame.mouse.get_pressed()[0]:
#            for i in xrange(len(cards)-5):
#                if isInArea(pygame.mouse.get_pos(), cards[i].pos):
#                    cards[i].pos = pygame.mouse.get_pos()

	if swipeUp(ev):
            print player[0].cards[0].color
	    #if color is RED:
	        #color = GREEN
	    #else:
	        #color = RED

        #Jogar carta
	if pygame.mouse.get_pressed()[0]:
            if isInArea(pygame.mouse.get_pos(),
                        player[0].cards[1].pos,TAMANHO_CARTA_X, TAMANHO_CARTA_Y):
                color = GREEN
            else:
                color = RED
                
# This isn't run on Android.
if __name__ == "__main__":
    main()
