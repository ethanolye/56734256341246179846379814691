import pygame
import random 
import math
import time 
pygame.init()
width, height = 1500, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("BlackJack")
RED = (255,0,0)
GREEN = (0,128,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
GREY = (128,128,128)
BLACK = (0,0,0)
WHITE  = (255,255,255)
pygame.display.update() 
#BlackJack Logic ------------------------------------------------------------------------------------
'''if event.type == pygame.KEYDOWN:
            screen.fill(WHITE)
            screen.blit(img2,(400,100))
            time.sleep(0.02)
            Screen()
            if event.key == pygame.K_h:
                player_hand.append(deck.pop())
                pscore = calculate_score(player_hand)
                print(player_hand)
'''

def pre():
    screen.fill(RED)
    font1 = pygame.font.SysFont('chalkduster.ttf', 72)
    img1 = font1.render('Press ENTER TO START', True, BLUE)
    
    screen.blit(img1, (500, 500))
    deck = []
    player_hand = []
    dealer_hand = []
    
   
    


    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10,'jack','queen','king','ace']
    suits = ["clubs", "spades", "diamonds", "hearts"]
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    def deal():
        for _ in range(2):
            player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())

    def calculate_score(cards):
        score = 0
        has_ace = False
        for card in cards:
            rank = card[0]
            if rank == "ace":
                score += 11
                has_ace = True
            elif rank in ["king", "queen", "jack"]:
                score += 10
            else:
                score += int(rank)
        if has_ace and score > 21:
            score -= 10
        return score

    pscore = calculate_score(player_hand)


    deal()
    
#-----------------------------Ingame Graphics-------------------------------------------------------------------
    def Screen():
        x = len(player_hand)
        for i in range(x):
            w = (f'{player_hand[i][0]}_of_{player_hand[i][1]}.png') 
            y = pygame.image.load(w)
            z = pygame.transform.scale(y, (100,200))      
            screen.blit(z,(600+i*100,300))
    def dscreen(liste):
        x = len(liste)
        for i in range(x):
            w = (f'{dealer_hand[i][0]}_of_{dealer_hand[i][1]}.png') 
            y = pygame.image.load(w)
            z = pygame.transform.scale(y, (100,200))      
            screen.blit(z,(100+i*100,300))

   
    font1 = pygame.font.SysFont('chalkduster.ttf', 62)
    
    img2 = font1.render('Press H to hit',True,BLACK)
    img7 = font1.render('Press S to Stand',True,BLACK)
    img3 = font1.render('Game Over',True,BLACK)
    img4 = font1.render('Dealer Hand',True, BLUE)
    img5 = font1.render('Press F12 for Menu',True, RED)
    img6 = font1.render('Player Hand',True, BLUE)

    def gameover(x):
        img3 = font1.render(f'Game Over:{x}',True,BLACK)
        screen.blit(img3,(700,500))
        screen.blit(img5,(700,600))
        
        

    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                screen.fill(WHITE)
                screen.blit(img2,(100,700))
                screen.blit(img4,(100,100))
                screen.blit(img6,(600,100))
                screen.blit(img7, (100,800))
                dscreen(dealer_hand)
                Screen()
                if pscore == 21:
                        e = True
                        while e:
                            print(f'Dealer hand:{dealer_hand}')
                            if dscore>=17:
                                e = False
                            dealer_hand.append(deck.pop())
                            dscore = calculate_score(dealer_hand)
                            if dscore>21:
                                gameover("Dealer Busted")
                                e = False
                            elif dscore>=17:
                                print(dealer_hand)
                                e = False
                        if pscore >dscore:
                            gameover("player wins")
                        if pscore == dscore:
                            gameover("PUSH(same value)")
                        if dscore>pscore:
                            gameover("Dealer Busted, PLayer wins")
                if event.key == pygame.K_h:
                    player_hand.append(deck.pop())
                    pscore = calculate_score(player_hand)
                    dscore = calculate_score(dealer_hand)
                    print(player_hand)
                    if pscore >21: 
                        gameover("Player Busted")
                    if pscore == 21:
                        e = True
                        while e:
                            print(f'Dealer hand:{dealer_hand}')
                            if dscore>=17:
                                e = False
                            dealer_hand.append(deck.pop())
                            dscore = calculate_score(dealer_hand)
                            if dscore>21:
                                gameover("Dealer Busted")
                                e = False
                            elif dscore>=17:
                                print(dealer_hand)
                                e = False
                        if pscore >dscore:
                            gameover("player wins")
                        if pscore == dscore:
                            gameover("PUSH(same value)")
                        if dscore>pscore:
                            gameover("Dealer Busted, PLayer wins")
                        
                    
                    Screen()
                if event.key == pygame.K_s:
                    print(player_hand)
                    print(dealer_hand)
                    pscore = calculate_score(player_hand)
                    dscore = calculate_score(dealer_hand)
                    e = True
                    while e:
                        print(f'Dealer hand:{dealer_hand}')
                        if dscore>=17:
                            e = False
                        dealer_hand.append(deck.pop())
                        dscore = calculate_score(dealer_hand)
                        if dscore>21:
                            print("Player Wins")
                            print(dealer_hand)
                            e = False
                        elif dscore>=17:
                            print(dealer_hand)
                            e = False
                    dscreen(dealer_hand)
                    
                    if dscore == pscore:
                        gameover("push")
                    elif dscore > pscore and dscore <=21:
                        gameover("dealer Wins")
                    elif pscore >dscore:
                        gameover("player wins")
                if event.key == pygame.K_F12:
                    pre()
                if event.key == pygame.K_F1:
                    print("help menu")
        
                
    
                
                
        pygame.display.update()
    pygame.quit()
pre()


   
        
            
    
