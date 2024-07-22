import pygame,sys
from game import Game
from colors import Colors
pygame.init()
title_font = pygame.font.Font(None,40)
score_surface = title_font.render("Score",True,Colors.white)
next_surface = title_font.render("Next",True,Colors.white)
game_over_surface =title_font.render("Game over",True,Colors.white)
score_rect = pygame.Rect(320,55,170,60)
next_rect = pygame.Rect(320,215,170,180)
# creating a game window with width and height 
screen = pygame.display.set_mode((500,620))
#display title 
pygame.display.set_caption("Python Tetris")
#game time frame
clock = pygame.time.Clock()
game = Game()
GAME_UPDATE = pygame.USEREVENT #used to create custom event
pygame.time.set_timer(GAME_UPDATE,200)
# runs continously until close the game 
while True:
    for event in pygame.event.get():#get the event put into list
        if event.type == pygame.QUIT:# exe  if click the close btn
            pygame.quit()
            sys.exit()
        if event.type ==pygame.KEYDOWN:#key controls
            if game.game_over == True:
                game.game_over = False
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0,1)
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:#automatic down movement
                game.move_down()
    #drawing with color
    score_value_surface = title_font.render(str(game.score),True,Colors.white)
    screen.fill(Colors.dark_blue)#filling the game with dark_blue color
    screen.blit(score_surface,(365,20,50,50))
    screen.blit(next_surface, (375,180, 50, 50))
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))
    pygame.draw.rect(screen,Colors.light_blue,score_rect,0,10)
    screen.blit(score_value_surface,score_value_surface.get_rect(centerx = score_rect.centerx,centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)
    pygame.display.update() # if any updates occur
    clock.tick(60)# 60 framerate/sec of game