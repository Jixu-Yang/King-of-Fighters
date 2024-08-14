import os
import pygame

from modules.config import SCREEN_WIDTH, SCREEN_HEIGHT, Config
from modules.role import Role
from modules.utils import *


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("King of Fighters")

bg = load_background(os.path.join('assets', 'background'))
role1_config = Config('kyo', True)
role1 = Role('kyo', False, role1_config)
role2_config = Config('chris', False)
role2 = Role('kyo', True, role2_config)

cur_key = None
frame = 0
winner = 0
while True:
    frame += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        if event.type in [pygame.KEYDOWN, pygame.KEYUP]:
            role1.process_key(event)
            role2.process_key(event)
 
    
    role1.update(role2)
    role2.update(role1)

    draw_background(screen, bg, frame)
    role1.show(screen)
    role2.show(screen)
    draw_lifebar(screen, role1, role2, ((30, 30), 200, 20))
    
    pygame.display.update()

    if role1.rest_life <= 0:
        winner = 2
    elif role2.rest_life <= 0:
        winner = 1
    if winner:
        pygame.time.wait(1000)
        show_result_screen(screen, winner)
        pygame.time.wait(2000)
        quit_game()

    pygame.time.Clock().tick(30)
